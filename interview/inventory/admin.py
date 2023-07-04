from django.contrib import admin
from rest_framework.pagination import LimitOffsetPagination

# Register your models here.


class InventoryPagination(LimitOffsetPagination):
    limit = 3
    page_size_query_param = 'page_size'
    max_page_size = 10
