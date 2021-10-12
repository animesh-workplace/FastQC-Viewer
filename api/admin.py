from django.contrib import admin

# Register your models here.

from .models import (
    ProjectTable,
    Data1,
    Data2
)


@admin.register(ProjectTable)
class ProjectTableModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Project', 'Patient']


@admin.register(Data1)
class Data1ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'Project', 'Patient', 'Sequence', 'Fastqcfol', 'Samplename']


@admin.register(Data2)
class Data2ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'DNA', 'FFPE', 'RNA', 'FastQc', 'SEQUENCE', 'Sample_name', 'Tru_Sequence',
                    'Flowcell', 'Lane', 'Row', 'BS', 'PBSQ', 'PTSQ', 'PSQS', 'PBSC', 'PSGC', 'PBNC',
                    'SLD', 'SDL', 'OS', 'AC']
