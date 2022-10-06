from django.urls import path

from shortener.views import CreateLinkAPI, UrlsListAPI, UrlDetailAPI, url_redirect

app_name = "shortener"
urlpatterns = [
    path("api/create/", CreateLinkAPI.as_view(), name="create-link"),
    path("api/get-urls-list/", UrlsListAPI.as_view(), name="create-link"),
    path("api/url-detail/<int:pk>/", UrlDetailAPI.as_view(), name="url-detail"),
    path("api/<slug:short_link>/", url_redirect, name="url-redirect"),
]
