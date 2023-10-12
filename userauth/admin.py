from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Patient)
admin.site.register(NextOfKin)
admin.site.register(Expert)
admin.site.register(ExpertHospitalDetails)
admin.site.register(Hospital)
