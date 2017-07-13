from django.conf.urls import url

from second_app import views

urlpatterns = [
    url(r'^$', views.index, name='second_index'),
    url(r'^formpage/', views.form_name_view, name='form_name')
]