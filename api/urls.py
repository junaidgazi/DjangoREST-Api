from django.contrib import admin
from django.urls import include, path

from api.views import ComampanyViewSet, EmployeeViewSet
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'companies', ComampanyViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]


# companies /{companyId}/employees