from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_student_details, name='get_student_details'),
    path('<int:id>/', views.get_student_details, name='get_student_details'),
]