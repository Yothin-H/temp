# created by ourselves

from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('subscription',views.subscription, name='subscription'),
    path(
        'subscription/thankyou',
        views.subscription_thankyou,
        name='thankyou'
    ),
    path(
        'change-theme',
        views.change_theme,
        name='change_theme'
    )

]