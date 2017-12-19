from django.contrib import admin
from .models import Domain, Resource, Instance


admin.site.register(Domain)
admin.site.register(Resource)
admin.site.register(Instance)
