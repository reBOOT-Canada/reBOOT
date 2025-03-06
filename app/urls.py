"""
reboot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.urls import re_path
from django.contrib import admin

from app.views import api_views, data_view, views

admin.autodiscover()

urlpatterns = [
    re_path(r'^', admin.site.urls),
    re_path(r'^analytics$', views.get_analytics, name='get_analytics'),
    re_path(r'^upload/csv$', views.import_csv, name='import_csv'),
    re_path(r'^upload/poll_state$', views.poll_state, name='poll_state'),
    re_path(r'^download/csv$', views.export_csv, name='export_csv'),
    re_path(r'^download/pdf$', views.download_receipt, name='download_receipt'),
    re_path(r'^download$', views.download_file, name='download_file'),
    re_path(r'^error$', views.error, name='error'),
]

# API urlpatterns
urlpatterns += [
    re_path(r'^api/autocomplete_name$', api_views.autocomplete_name),
    re_path(r'^api/donor_info_auto_complete$', api_views.donor_info_auto_complete),
    re_path(r'^api/device_info_auto_complete$',
        api_views.device_info_auto_complete),
    re_path(r'^api/related_donations$', api_views.related_donations),
    re_path(r'^api/related_items$', api_views.related_items),
    re_path(r'^api/quantity$', data_view.aggregate_quantity,
        name='aggregate_quantity'),
    re_path(r'^api/value$', data_view.aggregate_value, name='aggregate_value'),
    re_path(r'^api/status$', data_view.aggregate_status, name='aggregate_status'),
    re_path(r'^api/location$', data_view.aggregate_location,
        name='aggregate_location'),
]
