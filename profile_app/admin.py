from django.contrib import admin
from .models import Profile, ProfileResourceRule, Treatment


admin.site.register(Profile)
admin.site.register(ProfileResourceRule)
admin.site.register(Treatment)
