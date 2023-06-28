import uuid
from django.db import models


class UserManager(models.Manager):
    def create_user(self, phone_number):
        user = self.create(phone_number=phone_number)
        return user

    def isPhoneNumberSaved(self,phone_number):

        return super().get_queryset().filter(phone_number=phone_number)

     
class WAUsers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True, name='id'),
    user_name = models.CharField(max_length=30,null=True,unique=True,editable=False)
    phone_number = models.CharField(max_length=15,null=False)
    IsRegistered = models.BooleanField(default=False)
    IsBlocked = models.BooleanField(default=False) 
    createdAt = models.DateTimeField(auto_now_add=True)
    my_objects = UserManager()

    class Meta:
        db_table = 'tbl_wa_users'
    def __str__(self):
        return self.phone_number
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

