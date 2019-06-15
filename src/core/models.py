from django.db import models
from djchoices import DjangoChoices, ChoiceItem


class UserStatuses(DjangoChoices):
    enter_address = ChoiceItem()
    enter_name = ChoiceItem()
    start = ChoiceItem()
    allowed = ChoiceItem()

    # enter_family = ChoiceItem()


class UserData(models.Model):
    address = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    vk_id = models.IntegerField()


class VkSession(models.Model):
    user = models.ForeignKey(UserData, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, choices=UserStatuses.choices, default=UserStatuses.start)
