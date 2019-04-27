from django.conf.urls import url
from . import views

app_name = "library"

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^user_login/$',views.user_login,name="user_login"),
    url(r'^user/$',views.user,name="user"),
    url(r'^user_register/$',views.user_register,name="user_register"),
    url(r'^register_tools/$',views.register_tools,name="register_tools"),
    url(r'^login_tools/$',views.login_tools,name="login_tools"),
    url(r'^logout/$',views.logout,name="logout"),
]