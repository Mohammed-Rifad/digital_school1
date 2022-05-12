from django.urls import path
from . import views
urlpatterns=[

    path('auth-check',views.teacher_auth),
    path('view-teachers',views.view_teachers)
]