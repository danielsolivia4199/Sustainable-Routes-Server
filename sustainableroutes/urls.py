"""sustainableroutes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from sustainableapi.views import register_user, check_user, DestinationView, ActivityView, TagView, ActivityTagView, ActivityCommentView, DestinationCommentView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'destinations', DestinationView, 'destination')
router.register(r'activities', ActivityView, 'activity')
router.register(r'tags', TagView, 'tag')
router.register(r'activity_tags', ActivityTagView, 'activity_tag')
router.register(r'activity_comments', ActivityCommentView, 'activity_comment')
router.register(r'destination_comments', DestinationCommentView, 'destination_comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('checkuser', check_user),
]
