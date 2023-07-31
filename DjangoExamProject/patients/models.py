from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()
class Patients(models.Model):
    NAME_MAX_LEN = 30
    personal_photo = models.URLField(
        blank=False,
        null=False,
    )
    first_name = models.CharField(
        max_length=NAME_MAX_LEN,

    )
    last_name = models.CharField(
        max_length=NAME_MAX_LEN,

    )
    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    diagnosis = models.CharField(

    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )