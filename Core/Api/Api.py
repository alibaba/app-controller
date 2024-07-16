import json


class Api:
    def __init__(self, config, name, arguments, tool_call_id=None, dependency_apis=None, api_config_json=None):
        self.config = config
        self.name = name
        self.arguments = arguments
        self.tool_call_id = tool_call_id
        self.dependency_apis = dependency_apis

        self.api_config_json = json.dumps(api_config_json) if api_config_json is not None else None

    @classmethod
    def from_config_json(cls, config, data):
        dependency_apis = list(data["dependencyApis"].keys()) if "dependencyApis" in data else None
        return Api(config, data["name"], data["parameters"], dependency_apis=dependency_apis, api_config_json=data)

    def has_parameters(self):
        return len(self.arguments) > 0

    def __str__(self):
        return f"Api: {self.name}, Arguments: {self.arguments}, DependencyApis: {self.dependency_apis}"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def parameterized_api(self, to_str=False):
        res = {
            "name": self.name,
            "arguments": self.arguments
        }
        return json.dumps(res) if to_str else res
