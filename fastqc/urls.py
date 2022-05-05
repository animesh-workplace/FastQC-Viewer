from django.urls import path
from fastqc.api.upload_fastqc import upload_fastqc
from fastqc.api.get_fastqc_data import (fastqc_data, multiqc_report, fastqc_report, fastqc_report1, patient_data)


urlpatterns = [
    path('uploadfastqc/', upload_fastqc.as_view(), name='upload'),
    path('fastqcdata/', fastqc_data.as_view(), name='fastqcdata'),
    path('patientdata/', patient_data.as_view(), name='patientdata'),
    path('multiqc_report/<str:project>/<str:pid>/<str:sname>/<str:stype>', multiqc_report, name='multiqc_report'),
    path('fastqc_report/<str:project>/<str:pid>/<str:sname>/<str:stype>/<str:path>', fastqc_report, name='fastqc_report'),
    path('fastqc_report1/', fastqc_report1.as_view(), name='fastqc_report1'),
]