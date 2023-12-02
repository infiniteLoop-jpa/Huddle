from django.urls import path
from . import views
from .views import CustomLoginView

app_name = 'Huddle_app'  # Add this line to specify the app's name

urlpatterns = [
    path('huddle/home/', views.huddle_home, name='huddle_home'),
    path('huddle/group/', views.huddle_group, name='huddle_group'),
    path('huddle/login/', CustomLoginView.as_view(), name='huddle_login'),
    path('huddle/signup/', views.huddle_signup, name='huddle_signup')
]