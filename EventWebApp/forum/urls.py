from django.urls import path, include
from .views import home_view, signup_view, activation_sent_view, activate
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('', home_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
    path('forum/', include('django.contrib.auth.urls')), 
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

]


