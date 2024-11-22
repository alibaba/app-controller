from datetime import date
from Database.Models.UserModel import UserModel
    
    
class UserCallCountService:

    @classmethod
    async def enable_quota(cls, user_id: str):
        """
        Marks the user as privileged.
        
        Args:
            user_id: The unique identifier of the user.
        Returns:
            bool: Whether enable the quota for users or not.
        """
        user_model, created = await UserModel.get_or_create(user_id=user_id)
        if (user_model.has_quota):
            return True
        
        user_model.has_quota = True
        user_model.call_count = 0

        await user_model.save()
        return user_model.has_quota

    @classmethod
    async def inc_call_count(cls, user_id: str, value: int = 1):    
        """
        Update the call count for privileged users.
        Args:
            user_id: The unique identifier of the user.
        Returns:
            None
        """
        user_log, created = await UserModel.get_or_create(user_id=user_id)
        
        if not user_log.has_quota:
            return

        today = date.today()

        if user_log.call_date != today:
            user_log.call_date = today
            user_log.call_count = value  
        else:
            # If no changes, just increase call_count
            user_log.call_count += value

        await user_log.save()
    
    @classmethod
    async def get(cls, user_id: str) -> int:
        """
        Get the call count for privileged users.
        
        Args:
            user_id: The unique identifier of the user.
        Returns:
            bool: has privilege
            int: The call count for the specified date.
        """
        user_log, created = await UserModel.get_or_create(user_id=user_id)
        today = date.today()
        if user_log.call_date != today:
            user_log.call_date = today
            user_log.call_count = 0  
            await user_log.save()
        return user_log.has_quota, user_log.call_count

