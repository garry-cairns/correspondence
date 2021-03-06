# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from letters.views import (
    ContentTemplateViewSet,
    LetterheadViewSet,
    LetterViewSet,
    LetterVariableViewSet,
    LogoViewSet
)

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'content-templates', ContentTemplateViewSet)
router.register(r'letterheads', LetterheadViewSet)
router.register(r'letters', LetterViewSet)
router.register(r'letter-variables', LetterVariableViewSet)
router.register(r'logos', LogoViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
