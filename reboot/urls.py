"""reboot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.conf.urls import include
from django.urls import re_path

urlpatterns = [
    re_path(r'^', include('app.urls'))
]
