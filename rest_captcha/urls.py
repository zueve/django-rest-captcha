from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.RestCaptchaView.as_view(), name='rest_captcha'),
]
