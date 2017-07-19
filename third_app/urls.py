from django.conf.urls import url

from third_app import views

# Template tagging
app_name = 'third_app'

urlpatterns = [
    url(r'^$', views.index, name='third_index'),
    url(r'^other', views.other, name='third_other'),
    url(r'^relative', views.relative, name='third_relative')
    ]