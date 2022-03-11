from django.contrib import admin
from .models import Attendance, Service,Member,Payment
# Register your models here.

admin.site.register(Service)
admin.site.register(Attendance)
admin.site.register(Payment)
admin.site.register(Member)
