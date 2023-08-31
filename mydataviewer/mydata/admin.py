from django.contrib import admin

# Register your models here.
from .models import MongoDBConnection


admin.site.register(MongoDBConnection)
