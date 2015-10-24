from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url(r'^$', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)

