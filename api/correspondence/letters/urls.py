# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import (
    ContentTemplateViewSet,
    LetterTextViewSet,
    LetterFileViewSet,
    LetterVariableViewSet
)
 
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'content-templates', ContentTemplateViewSet)
router.register(r'letters', LetterTextViewSet)
router.register(r'letter-files', LetterFileViewSet)
router.register(r'letter-variables', LetterVariableViewSet)
 
# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
]
