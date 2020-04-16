from django.conf.urls import url
from . import views

app_name = "login"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new$', views.new, name="new"),
    url(r'^create$', views.create, name="create"),  
    url(r'^show$', views.show, name="show"),  
    url(r'^destroy$', views.destroy, name="destroy"),    
]