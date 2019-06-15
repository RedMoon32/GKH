from django.db import models
from djchoices import DjangoChoices, ChoiceItem


class UserStatuses(DjangoChoices):
    enter_address = ChoiceItem()
    enter_name = ChoiceItem()
    start = ChoiceItem()
    allowed = ChoiceItem()
    enter_org_name = ChoiceItem()
    enter_role = ChoiceItem()
    allowed_group = ChoiceItem()
    approve = ChoiceItem()
    enter_user_org = ChoiceItem()
    # enter_family = ChoiceItem()

class Organisation(models.Model):
    vk_id = models.IntegerField()
    name = models.CharField(max_length=100, null=True, blank=True)



class UserData(models.Model):
    address = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    vk_id = models.IntegerField(null=True)
    is_organisation = models.BooleanField(default=False)
    approved = models.BooleanField(default=None, null=True)
    organisation = models.ForeignKey(to=Organisation, on_delete=models.SET_NULL, null=True)


class VkSession(models.Model):
    user = models.ForeignKey(UserData, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, choices=UserStatuses.choices, default=UserStatuses.start)
