from django import forms

from DjangoExamProject.core.form_mixins import DisabledFormMixin
from DjangoExamProject.patients.models import Patients


# `ModelForm` and `Form`:
# - `ModelForm` binds to models
# - `Form` is detached from models

class PetBaseForm(forms.ModelForm):
    class Meta:
        model = Patients
        # fields = '__all__' (not the case, we want to skip `slug`
        fields = ('first_name', 'last_name', 'date_of_birth', 'diagnosis')
        # exclude = ('slug',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'personal_photo': 'Link to Image',
            'date_of_birth': 'Date of Birth',
            'diagnosis': 'Diagnosis',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Pet firstname'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Patient lastname'
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'placeholder': 'mm/dd/yyyy',
                    'type': 'date',
                }
            ),
            'diagnosis': forms.TextInput(
                attrs={
                    'placeholder': 'Patient diagnosis'
                }
            ),

        }


class PetCreateForm(PetBaseForm):
    pass


class PetEditForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class PetDeleteForm(DisabledFormMixin, PetBaseForm):
    disabled_fields = ('name', 'date_of_birth', 'personal_photo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
