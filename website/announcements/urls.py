"""The routes defined by this package"""
# pylint: disable=invalid-name
from django.conf.urls import url
from django.urls import path, include

from announcements import views

#: the name of this app
app_name = "announcements"

#: the actual routes
urlpatterns = [
    path(
        "announcements/",
        include(
            [
                path(
                    "close-announcement",
                    views.close_announcement,
                    name="close-announcement",
                )
            ]
        ),
    )
]
