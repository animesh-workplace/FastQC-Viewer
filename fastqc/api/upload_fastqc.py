import os
import pandas as pd
from fastqc.models import Fastqc
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
rootDir = "/home/nsm-07/Desktop/FastQ_Storage_Repository/Project"
def fastqcfolder():
    fastqc = [];multiqc = [];lst = [];lst1 = [];l = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            if fname == 'fastqc_report.html':
                fastqc.append(dirName + "/" +fname)
            if fname == 'multiqc_report.html':
                multiqc.append(dirName + "/" +fname)
            if fname == 'summary.txt':
                df = pd.read_csv(dirName+'/'+fname, header=None,delimiter = "\t", names=["a", "b", "c"])
                lst.append(dirName)
                a = df['a'].tolist()
                lst1.append(a)
            if fname == 'fastqc_data.txt':
                df1 = pd.read_csv(dirName+'/'+fname,delimiter = "\t", header=None, names=["a"])
                df1 = df1.loc[['Total Sequences','Sequence length','%GC']]
                b = df1['a'].tolist()
                l.append(b)
    df2 = pd.DataFrame(l)
    a = []
    for i in lst:
        a.append(i.split('/'))
    df = pd.DataFrame(a)
    df = df.iloc[:,6:12]
    df1 = pd.DataFrame(lst1)
    df = pd.concat([df, df1, df2], axis=1)
    df.columns = ['project_name', 'patient_id','sequence','Folder_name','sample_type','path_name',
    'BS','PBSQ','PTSQ','PSQS','PBSC','PSGC','PBNC','SLD','SDL','OS','AC','total_sequences','sequence_length','GC']
    df[['sample_name','true_sequence', 'flowcell','lane','row','extra']] = df['path_name'].str.split('_', n=5, expand=True)
    b = []
    for i in multiqc:
        b.append(i.split('/'))
    df1 = pd.DataFrame(b)
    df1 = df1.iloc[:,6:11]
    df1['new'] = multiqc
    df1.columns = ['project_name', 'patient_id','sequence','Folder_name','sample_type','multiqc_report',]
    df = pd.merge(df, df1, how="left", on=['project_name', 'patient_id','sequence','sample_type'])
    df['fastqc_report'] = fastqc
    Fastqc.objects.all().delete()
    objs = [
            Fastqc(
                index=index,project_name=row.project_name,patient_id=row.patient_id,
                sequence=row.sequence,sample_type=row.sample_type,path_name=row.path_name,
                basic_statistics=row.BS,per_base_sequence_quality=row.PBSQ,per_tile_sequence_quality=row.PTSQ,
                per_sequence_quality_scores=row.PSQS,Per_base_sequence_content=row.PBSC,
                per_sequence_gc_content=row.PSGC,per_base_n_content=row.PBNC,sequence_length_distribution=row.SLD,
                sequence_duplication_levels=row.SDL,overrepresented_sequences=row.OS,adapter_content=row.AC,
                total_sequences=row.total_sequences,sequence_length=row.sequence_length,GC=row.GC,
                sample_name=row.sample_name,true_sequence=row.true_sequence,flowcell=row.flowcell,
                lane=row.lane,row=row.row,multiqc_report=row.multiqc_report,fastqc_report=row.fastqc_report,
            )
            for index, row in df.iterrows()
            ]
    Fastqc.objects.bulk_create(objs)
    returnmsg = {"message": "success"}
    return Response(returnmsg)

class upload_fastqc(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        return fastqcfolder()