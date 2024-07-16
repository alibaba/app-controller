from tortoise.models import Model
from tortoise import fields


class SessionModel(Model):
    # Defining `id` field is optional, it will be defined automatically, if you haven't done it yourself
    id = fields.IntField(primary_key=True)
    # the session id of the task
    session_id = fields.CharField(max_length=255)

    # the file path of execution pipeline
    pipeline = fields.TextField()

    # user input
    user_input = fields.TextField()

    # whether the task is success
    feedback = fields.CharField(max_length=50)

    timestamp = fields.DatetimeField(auto_now_add=True)

    # Defining ``__str__`` is also optional, but gives you pretty
    # represent of model in debugger and interpreter
    def __str__(self):
        return self.user_input

    def to_json(self):
        return {
            "session_id": self.session_id,
            "pipeline": self.pipeline,
            "user_input": self.user_input,
            "feedback": self.feedback,
            "timestamp": str(self.timestamp)
        }
