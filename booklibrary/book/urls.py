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
    url(r'^user_info/$',views.user_info,name="user_info"),
    url(r'^user_info_update/(\d+)/$',views.user_info_update,name="user_info_update"),
    url(r'^querybook/$',views.querybook,name="querybook"),
    url(r'^book_info/(\d+)/$',views.book_info,name="book_info"),
    url(r'^borrow_info/$',views.borrow_info,name="borrow_info"),
    url(r'^edit/$',views.edit,name="edit"),
]