from django.db import models
from django.core.files.storage import FileSystemStorage
# Create your models here.

def user_directory_path(instance, filename):
    return "{0}/{1}".format(filename)
fs = FileSystemStorage(location='/media')

class Fastqc(models.Model):
    index = models.BigIntegerField(primary_key=True)
    project_name = models.CharField(max_length=300,default=None,blank=True,null=True)
    patient_id = models.CharField(max_length=300,default=None,blank=True,null=True)
    sequence = models.CharField(max_length=300,default=None,blank=True,null=True)
    sample_type = models.CharField(max_length=300,default=None,blank=True,null=True)
    path_name = models.CharField(max_length=300,default=None,blank=True,null=True)
    basic_statistics = models.CharField(max_length=300,default=None,blank=True,null=True)
    per_base_sequence_quality = models.CharField(max_length=300,default=None,blank=True,null=True)
    per_tile_sequence_quality = models.CharField(max_length=300,default=None,blank=True,null=True)
    per_sequence_quality_scores = models.CharField(max_length=300,default=None,blank=True,null=True)
    Per_base_sequence_content = models.CharField(max_length=300,default=None,blank=True,null=True)
    per_sequence_gc_content = models.CharField(max_length=300,default=None,blank=True,null=True)
    per_base_n_content = models.CharField(max_length=300,default=None,blank=True,null=True)
    sequence_length_distribution = models.CharField(max_length=300,default=None,blank=True,null=True)
    sequence_duplication_levels = models.CharField(max_length=300,default=None,blank=True,null=True)
    overrepresented_sequences 	= models.CharField(max_length=300,default=None,blank=True,null=True)
    adapter_content = models.CharField(max_length=300,default=None,blank=True,null=True)
    sample_name = models.CharField(max_length=300,default=None,blank=True,null=True)
    true_sequence = models.CharField(max_length=300,default=None,blank=True,null=True)
    flowcell  = models.CharField(max_length=300,default=None,blank=True,null=True)
    lane  = models.CharField(max_length=300,default=None,blank=True,null=True)
    row = models.CharField(max_length=300,default=None,blank=True,null=True)
    total_sequences = models.CharField(max_length=300,default=None,blank=True,null=True)
    sequence_length  = models.CharField(max_length=100,default=None,blank=True,null=True)
    GC = models.CharField(max_length=50,default=None,blank=True,null=True)
    multiqc_report = models.FileField(upload_to='media',max_length=3000,null=True)
    fastqc_report = models.FileField(upload_to='media',max_length=3000,null=True)

    # def __str__(self):
    #     return str(self.project_name)
