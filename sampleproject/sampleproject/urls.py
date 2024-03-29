"""
URL configuration for sampleproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles import views
from django.urls import re_path, path, include
from first.views import hello, hello_name, courses, course, students, main, profile, contact, add_teacher, edit_teacher, add_student
from first.views import login_view, logout_view, api_view
from first.router import router

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path("hello", hello),
    path("hello/<str:name>/", hello_name),
    path("courses", courses, name="courses"),
    path("course/<int:course_id>", course),
    path("students", students, name="students"),
    path("__debug__/", include("debug_toolbar.urls")),
    path("profile", profile),
    path("contact/", contact),
    path("add_teacher", add_teacher),
    path("add_student", add_student),
    path("teacher/<int:teacher_id>/edit", edit_teacher),
    path("login", login_view),
    path("logout", logout_view),
    path("api/", api_view),
    path("drf/", include(router.urls)),
    path("", main),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns.append(re_path(r"^static/(?P<path>.*)$", views.serve))