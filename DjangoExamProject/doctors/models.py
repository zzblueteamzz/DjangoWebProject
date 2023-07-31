from enum import Enum
from django.contrib.auth import get_user_model
from django.db import models
from django.core import validators
from DjangoExamProject.core.validators import validate_only_letters
UserModel = get_user_model()


class ChoicesEnumMixin:
    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Specialization(ChoicesEnumMixin, Enum):
    surgeon = 'Surgeon'
    cardiologist = 'Cardiologist'
    gynecologist = 'Gynecologist'
    urologist = 'Urologist'
    dermatologist = 'dermatologist'
    neurologist = 'neurologist'
    DoNotShow = 'Do not show'


class Doctor(models.Model):
    FIRST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 2

    LAST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 2

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_only_letters,

        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_only_letters,
        )
    )

    specialization = models.CharField(
        choices=Specialization.choices(),
        max_length=Specialization.max_len(),
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )