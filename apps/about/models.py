from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField
from apps.common.models import BaseModel
from apps.dashboard.models import User


class Feedback(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    email = models.EmailField(unique=True, verbose_name=_('Email'), blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name=_('Phone number'), blank=True, null=True)
    message = RichTextField(verbose_name=_('Feedback message'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"


class Notification(BaseModel):
    title = models.CharField(max_length=100, verbose_name=_('Title'), blank=True, null=True)
    context = RichTextField(verbose_name=_('Context'), blank=True, null=True)
    scheduled_at = models.DateTimeField(verbose_name=_('schedule time'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"


class NotificationView(BaseModel):
    notification = models.ForeignKey(
        Notification, on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    device_id = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.notification.title[:20]}... | {self.user} | {self.device_id}"


class Advertisement(BaseModel):
    title = models.CharField(max_length=150, null=True, blank=True)
    image = ImageField(upload_to="photos/advertisement/%Y/%m/%d/")
    content = RichTextField(verbose_name=_('Content'))
    phone = PhoneNumberField(verbose_name=_('Phone number'))

    def __str__(self):
        return "Advertisement"

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"


class UseTerm(BaseModel):
    title = models.CharField(max_length=150, null=True, blank=True)
    image = ImageField(upload_to="photos/notification_images/%Y/%m/%d/")
    content = RichTextField(verbose_name=_('Content'))

    def __str__(self):
        return "UseTerm"

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"


class Contact(BaseModel):
    phone = PhoneNumberField(verbose_name=_('Phone number'))
    email = models.EmailField()
    address = models.CharField(max_length=150)
    long = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return "UseTerm"

    class Meta:
        verbose_name = "Advertisement"
        verbose_name_plural = "Advertisements"