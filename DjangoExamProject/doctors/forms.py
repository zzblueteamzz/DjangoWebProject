from django import forms

from DjangoExamProject.core.form_mixins import DisabledFormMixin
from DjangoExamProject.doctors.models import Doctor


# `ModelForm` and `Form`:
# - `ModelForm` binds to models
# - `Form` is detached from models

class DoctorBaseForm(forms.ModelForm):
    class Meta:
        model = Doctor
        # fields = '__all__' (not the case, we want to skip `slug`
        fields = ('first_name', 'last_name', 'specialization')
        # exclude = ('slug',)
        labels = {
            'first_name': 'Doctor First Name',
            'last_name': 'Doctor Last Name',
            'specialization': 'Specialization',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Doctor First Name'
                }
            ),
            'last_name': forms.DateInput(
                attrs={
                    'placeholder': 'Doctor Last Name',

                }
            ),
            'specialization': forms.URLInput(
                attrs={
                    'placeholder': 'Specialization',
                }
            )
        }


class DoctorCreateForm(DoctorBaseForm):
    pass


class DoctorEditForm(DisabledFormMixin, DoctorBaseForm):
    disabled_fields = ('name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


class DoctorDeleteForm(DisabledFormMixin, DoctorBaseForm):
    disabled_fields = ('first_name', 'last_name', 'specialization')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
