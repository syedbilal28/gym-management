from django.contrib import admin
from .models import Attendance, Service,Profile,Payment
# Register your models here.

admin.site.register(Service)
admin.site.register(Attendance)
admin.site.register(Payment)
admin.site.register(Profile)
