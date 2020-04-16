from django.conf.urls import url
from . import views
from django.views.generic import RedirectView
app_name = "bjj"
urlpatterns = [
    url(r'^index$', views.index, name="index"),
    url(r'^new/(?P<move_id>\d+)$', views.new, name="new"),
    url(r'^create$', views.create, name="create"),
    url(r'^show$', views.show, name="show"),
    url(r'^edit/(?P<move_id>\d+)$', views.edit, name="edit"),
    url(r'^update/(?P<move_id>\d+)$', views.update, name="update"),
    url(r'^destroy/(?P<move_id>\d+)$', views.destroy, name="destroy"),
    url(r'^new_search$', views.new_search, name="new_search"),
    url(r'^move_api$', views.move_api, name="move_api"),
]