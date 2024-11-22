from tortoise.models import Model
from tortoise import fields
from datetime import date

class UserModel (Model):
    
    # the user id of the task
    user_id = fields.CharField(primary_key=True, max_length=255)
    
    # if the user has the quota to call free tongyi api.
    has_quota = fields.BooleanField(default=False)

    # the date of the call
    call_date = fields.DateField(default=date.today())
    
    # the count of the call
    call_count = fields.IntField(default=0)

    timestamp = fields.DatetimeField(auto_now_add=True)

    # represent of model in debugger and interpreter
    def __str__(self):
        return f"UserID: {self.user_id}, hasQuota: {self.has_quota}, CallDate: {self.call_date}, CallCount: {self.call_count}"
    def to_json(self):
        return {
            "user_id": self.user_id,
            "has_quota": self.has_quota,
            "call_date": self.call_date,
            "call_count": self.call_count,
            "timestamp": str(self.timestamp)
        }



        