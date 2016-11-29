from django.contrib import admin
from rango.models import Notice, Compared
from rango.models import UserProfile


admin.site.register(Notice)
admin.site.register(UserProfile)
admin.site.register(Compared)