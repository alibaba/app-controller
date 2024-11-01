import json
import re
import traceback

from Common.ChatReposne import Response
from Common.CustomEnum import ResponseStatusEnum



class ResultChecker:
    def __init__(self, api_gts) -> None:
        self.success = True
        self.info = ""
        self.api_gts = api_gts if isinstance(api_gts, list) else [api_gts]
        self.apis = []
        self.each_fail_reason = ["" for _ in range(len(self.api_gts))]
        self.each_fail = [False for _ in range(len(self.api_gts))]
        self.fail_reason_in_nl = ""
        self.covered_api = [set() for _ in range(len(self.api_gts))]
        self.finish = False
        self.last_fail = [{} for _ in range(len(self.api_gts))]

    def check(self, result: Response):
        if result.status == ResponseStatusEnum.TASK_API_CALL:
            self._handle_api_call(result)
            if result.data["isTerminal"]:
                self._handle_task_finished()
        elif result.status == ResponseStatusEnum.TASK_FAILED:
            self._handle_task_failed()
        elif result.status == ResponseStatusEnum.TASK_FINISHED:
            self._handle_task_finished()
        print(f"fin is set to {self.finish}", flush=True)
        if self.finish:
            self.info += self.fail_reason_in_nl

    def _handle_api_call(self, result: Response):
        apis = result.data["apis"]
        assert len(apis) == 1, "Now only one api in a single interaction turn."
        api = apis[0]
        self.apis.append(json.dumps(api))
        name = api["name"]
        for i, api_gt in enumerate(self.api_gts):
            if name in api_gt:
                res, passed = api_args_check(api_gt[name]["arguments"], api["arguments"])
                if passed:
                    self.covered_api[i].add(name)
                else:
                    self.last_fail[i][name] = res
            else:
                self.each_fail_reason[i] += f"Use unnecessary or non-existed api '{name}'. Think add this api or not.  "
                self.each_fail[i] = True

    def _handle_task_failed(self):
        self.success = False
        self.info += "Result: " + ", ".join(self.apis) + "\n"
        self.fail_reason_in_nl += f"LLM gave up the task. "
        self.finish = True

    def _handle_task_finished(self):
        self.info += "Result: " + ", ".join(self.apis) + "\n"
        success = False
        for i, api_gt in enumerate(self.api_gts):
            if not self.each_fail[i] and len(self.covered_api[i]) >= len(api_gt):
                success = True
        self.success = success
        if not self.success:
            for i, api_gt in enumerate(self.api_gts):
                self.fail_reason_in_nl += f"Option {i}:" + self.each_fail_reason[i]
                if len(self.covered_api[i]) < len(api_gt):
                    self.fail_reason_in_nl += "Not pass all api needed. "
                    for k, v in self.last_fail[i].items():
                        if k not in self.covered_api[i]:
                            self.fail_reason_in_nl += v
        self.finish = True

    def task_failed(self, errorMessage=None):
        self.success = False
        if errorMessage is not None:
            self.fail_reason_in_nl = errorMessage
        else:
            self.fail_reason_in_nl = traceback.format_exc()
        self.info += self.fail_reason_in_nl
        self.finish = True


def api_args_check(gt_args, pred_args):
    # API check rule
    # If ground truth in test_data.json is not string (is bool or null):
    #     Check the predicted value is exactly equal or not.
    # Else if ground truth in test_data.json is string s:
    #     if s starts with '@:'
    #         s is a lambda expresion (f) with variable x
    #         If f(x) is True, the test of the argument passes.
    #     else if s starts with '#:':
    #         s is a regex.
    #         if predicted string is matched, the test of the argument passes.

    err = ""
    for arg, v in gt_args.items():
        if arg not in pred_args:
            err += f"Lack argument {arg}."
        else:
            pred = pred_args[arg]
            if isinstance(v, str):
                if v.startswith("@:"):
                    f = eval("lambda x: " + v[2:])
                    if not f(pred):
                        err += f"argument {arg} check fail. pred :{pred}, lambda:{v[2:]}."
                elif v.startswith("#:"):
                    if not re.match(v[2:], pred):
                        err += f"argument {arg} do not match."
                else:
                    if pred != v:
                        err += f"argument(str) {arg} do not equal. pred :{pred}, gt :{v}. "
            elif isinstance(v, dict):
                if isinstance(pred, str):
                    pred = json.loads(pred)
                res, passed = api_args_check(v, pred)
                err += res
            else:
                if pred != v:
                    err += f"argument({type(pred)}) {arg} do not equal. pred :{pred}, gt :{v}"
    if err == "":
        return err, True
    return err, False
