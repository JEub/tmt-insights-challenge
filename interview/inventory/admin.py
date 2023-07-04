from django.contrib import admin
from rest_framework.pagination import LimitOffsetPagination

# Register your models here.


class InventoryPagination(LimitOffsetPagination):
    page_size = 3
