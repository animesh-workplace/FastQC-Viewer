from django.db import models


SEQUENCE_CHOICE = (
    ('DNA', 'DNA'),
    ('FFPE', 'FFPE'),
    ('RNA', 'RNA'),
    ('null', 'null'),
)


class Data1(models.Model):
    Project = models.CharField(max_length=200)
    Patient = models.CharField(max_length=200)
    Sequence = models.CharField(choices=SEQUENCE_CHOICE, max_length=200, null=True)
    Fastqcfol = models.CharField(max_length=100, null=True)
    Samplename = models.CharField(max_length=100, null=True)
    Sample = models.CharField(null=True, max_length=150)

    def __str__(self):
        return str(self.id)


class Data2(models.Model):
    Sequence = models.CharField(choices=SEQUENCE_CHOICE, max_length=100)
    FastQc = models.CharField(max_length=200)
    Sample_name = models.CharField(max_length=200)
    Path_name = models.CharField(max_length=200)
    Tru_Sequence = models.CharField(max_length=200)
    Flowcell = models.CharField(max_length=200)
    Lane = models.CharField(max_length=200)
    Row = models.CharField(max_length=200)
    BS = models.CharField(max_length=200)
    PBSQ = models.CharField(max_length=200)
    PTSQ = models.CharField(max_length=200)
    PSQS = models.CharField(max_length=200)
    PBSC = models.CharField(max_length=200)
    PSGC = models.CharField(max_length=200)
    PBNC = models.CharField(max_length=200)
    SLD = models.CharField(max_length=200)
    SDL = models.CharField(max_length=200)
    OS = models.CharField(max_length=200)
    AC = models.CharField(max_length=200)
    Total_Sequence = models.CharField(max_length=200)
    Sequence_length = models.CharField(max_length=200)
    GC = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)
