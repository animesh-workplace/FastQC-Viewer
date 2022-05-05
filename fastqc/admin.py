from django.contrib import admin
from fastqc.models import Fastqc

class Fastqc_admin(admin.ModelAdmin):
	search_fields = ('project_name', 'patient_id','sequence','sample_type','path_name')
	list_display = ('project_name', 'patient_id','sequence','sample_type','path_name',)

	fieldsets = ()
        
admin.site.register(Fastqc, Fastqc_admin)