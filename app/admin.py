from django.contrib import admin
from.models import Address, Partners,Donors,Volunteers
# Register your models here.
admin.site.register(Volunteers)
admin.site.register(Donors)
admin.site.register(Partners)
admin.site.register(Address)