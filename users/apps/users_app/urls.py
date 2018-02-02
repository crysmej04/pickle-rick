from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name ="index"),
    url(r'^register$', views.register, name = "register"),
    url(r'^success$', views.success, name = "success"),
    url(r'^login$', views.login, name = "login"),
    url(r'^item_info/(?P<id>\d+)$', views.item_info),
    url(r'^add_item$', views.add_item, name = "add_item"),
    url(r'^delete/(?P<id>\d+)$', views.destroy),
    url(r'^join/(?P<id>\d+)$', views.join),
    url(r'^new_item$', views.new_item, name= "new_item"),
]