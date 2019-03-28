from django.contrib import admin
from django.urls import path,re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/',include('users.urls',namespace='users')),
    path('courses/',include('courses.urls',namespace='courses')),
    path('orgs/',include('orgs.urls',namespace='orgs')),
    path('operations/',include('operations.urls',namespace='operations')),
]
