from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter

from apps.authentication import views

router_user = DefaultRouter()
router_user.register(r'users', views.UserViewSet, 'user')
router_user.register(r'usersAddress', views.UserAddressView, 'useraddress')
router_user.register(r'usersRating', views.UserRatingView, 'userratting')
router_user.register(r'userEvent', views.UserEventView, 'userevent')

urlpatterns = [
    url(r'^auth/email/signup/$', views.EmailSignupView.as_view(), name='email-signup'),
    url(r'^auth/email/login/$', views.EmailLoginView.as_view(), name='email-login'),

    url(r'^', include(router_user.urls)),

]
