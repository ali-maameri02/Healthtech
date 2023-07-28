from django.urls import path
from . import views
from .views import UserLoginView, ProfileView

urlpatterns = [
   path("signup/", views.signup, name="singup"),
   path("", views.home, name="home"),
   path("login/", UserLoginView.as_view() , name="login"),
   path("profile/", ProfileView.as_view(), name="profile"),
   path("patient/", views.patient, name="patient"),
   path("doctor/", views.doctor, name="doctor"),
   path("patient_details/", views.patient_details, name="patient_details"),

]