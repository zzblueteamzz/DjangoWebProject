from django.urls import path, include

from DjangoExamProject.accounts.views import to_github, SignInView, SingInView, SignOutView, \
    UserDetailsView, UserEditView, UserDeleteView

# accounts/urls.py

urlpatterns = (
    path('register/', SingInView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),

    path('profile/<int:pk>/', include(
        [
            path('', UserDetailsView.as_view(), name='profile details'),
            path('edit/', UserEditView.as_view(), name='profile edit'),
            path('delete/', UserDeleteView.as_view(), name='profile delete'),
        ]
    )),

    path('to_github/', to_github, name='go to github'),
)

# need to add this to work with signals->
#from .signals import *