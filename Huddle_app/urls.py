from django.urls import path
from . import views
from .views import huddle_group

app_name = 'Huddle_app'  # Add this line to specify the app's name

urlpatterns = [
    path('huddle/home/', views.huddle_home, name='huddle_home'),
    path('huddle_group/<int:huddle_group_id>/', huddle_group, name='huddle_group'),
    path('huddle/login/', views.huddle_login, name='huddle_login'),
    path('huddle/signup/', views.huddle_signup, name='huddle_signup'),
    path('create_huddle/', views.create_huddle, name='create_huddle'),
    path('save_task/', views.save_task, name='save_task'),

]
