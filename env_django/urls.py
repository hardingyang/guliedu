#from django.contrib import admin
from django.urls import path,re_path,include
from extra_apps import xadmin
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('users/',include(('users.urls','users'),namespace='users')),
    path('courses/',include(('courses.urls','courses'),namespace='courses')),
    path('orgs/',include(('orgs.urls','orgs'),namespace='orgs')),
    path('operations/',include(('operations.urls','operations'),namespace='operations')),
]
