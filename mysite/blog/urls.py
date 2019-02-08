from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('artem/', views.artem, name='artem'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='post_list.html'), name='home'),
    path('signup/', views.signup, name='signup')
]