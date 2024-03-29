from django.db import models

# Create your models here.


class Participant(models.Model):
    registration_date_time = models.DateTimeField('date and time of registration')
    full_name = models.CharField(max_length=256)
    email = models.EmailField(max_length=128, blank=True, null=True)
    phone_number = models.CharField(max_length=64)
    occupation = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    organization = models.CharField(max_length=256)
    invitation_required = models.BooleanField()
    is_checked_in = models.BooleanField(default=False)
    check_in_time = models.TimeField('check-in time', null=True)

    def __str__(self):
        return self.full_name
