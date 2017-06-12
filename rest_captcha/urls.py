from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.RestCapthaView.as_view(), name='rest_captcha'),
]
