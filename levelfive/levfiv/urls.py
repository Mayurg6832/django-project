from django.urls import path
from levfiv import views

app_name = 'levfiv'

urlpatterns=[
	path('register/',views.register,name='register'),
	path('user_login/',views.user_login,name='user_login'),
]