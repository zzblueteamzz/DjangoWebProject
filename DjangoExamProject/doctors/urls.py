from django.urls import path, include

from DjangoExamProject.doctors.views import add_doctor, show_doctor_details, edit_doctor, delete_doctor

urlpatterns = (
    path('add/', add_doctor, name='add_doctor'),
    path('<str:username>/pet/<slug:pet_slug>/', include(
        [
            path('', show_doctor_details, name='show_pet_details'),
            path('edit/', edit_doctor, name='edit_pet'),
            path('delete/', delete_doctor, name='delete_pet'),
        ]
    )),
)
