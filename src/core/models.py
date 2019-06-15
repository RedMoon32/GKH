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
    # enter_family = ChoiceItem()


class CSV_File(models.Model):
    file_path = models.CharField(null=True, max_length=100)


class Organisation(models.Model):
    vk_id = models.IntegerField()
    name = models.CharField(max_length=100, null=True, blank=True)
    files = models.ManyToManyField(CSV_File)


class UserData(models.Model):
    address = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    vk_id = models.IntegerField()


class VkSession(models.Model):
    user = models.ForeignKey(UserData, null=True, blank=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=100, choices=UserStatuses.choices, default=UserStatuses.enter_role)
