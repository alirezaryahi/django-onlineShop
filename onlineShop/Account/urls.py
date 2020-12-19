from django.urls import path, include
from .views import login_page, register_page, log_out, user_info, user_edit, user_edit_password

urlpatterns = [
    path('login', login_page),
    path('register', register_page),
    path('logout', log_out),
    path('user/info', user_info),
    path('user/edit', user_edit),
    path('user/resetPassword', user_edit_password),
]
