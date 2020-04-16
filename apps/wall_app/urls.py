from django.conf.urls import url
from . import views

app_name = "wall"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^new$', views.new, name="new"),
    url(r'^create$', views.create, name="create"),
    url(r'^edit/(?P<post_id>\d+)$', views.edit, name="edit"),
    url(r'^update/(?P<post_id>\d+)$', views.update, name="update"),
    url(r'^destroy/(?P<post_id>\d+)$', views.destroy, name="destroy"),
    url(r'^new_like/(?P<post_id>\d+)$', views.new_like, name="new_like"),
    url(r'^show$', views.show, name="show"),
    url(r'^new_follow/(?P<user_id>\d+)$', views.new_follow, name="new_follow"),

]