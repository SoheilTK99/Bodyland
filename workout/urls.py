from django.urls import path
from .import views

app_name = "workout"

urlpatterns = [
    path("",views.workout_list,name='workout_list'),
    path('get-workouts/', views.get_workouts_ajax, name='get_workouts_ajax'),
]