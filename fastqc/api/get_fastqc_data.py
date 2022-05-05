from fastqc.models import Fastqc
from users.models import User
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'

class dataserializer(serializers.ModelSerializer):
    class Meta:
        model = Fastqc
        fields = ('project_name','patient_id')

class fastqc_data(ListAPIView):
    queryset = Fastqc.objects.values('project_name','patient_id').order_by('patient_id').distinct()
    serializer_class = dataserializer
    filter_backends = (DjangoFilterBackend,SearchFilter )
    permission_classes = (AllowAny,)
    pagination_class = LargeResultsSetPagination
    filter_fields = ('project_name','patient_id')
    search_fields = ('project_name','patient_id')

from django_filters.rest_framework import DjangoFilterBackend
class patientserializer1(serializers.ModelSerializer):
    class Meta:
        model = Fastqc
        fields = '__all__'



class AdvancedFilter(filters.FilterSet):
    project_name = filters.CharFilter(lookup_expr='icontains')
    patient_id = filters.CharFilter(lookup_expr='icontains')
    sequence = filters.CharFilter(lookup_expr='icontains')
    sample_type = filters.CharFilter(lookup_expr='icontains')
    basic_statistics = filters.CharFilter(lookup_expr='icontains')
    per_base_sequence_quality = filters.CharFilter(lookup_expr='icontains')
    per_tile_sequence_quality = filters.CharFilter(lookup_expr='icontains')
    per_sequence_quality_scores = filters.CharFilter(lookup_expr='icontains')
    Per_base_sequence_content = filters.CharFilter(lookup_expr='icontains')
    per_sequence_gc_content = filters.CharFilter(lookup_expr='icontains')

    per_base_n_content = filters.CharFilter(lookup_expr='icontains')
    sequence_length_distribution = filters.CharFilter(lookup_expr='icontains')
    sequence_duplication_levels = filters.CharFilter(lookup_expr='icontains')
    overrepresented_sequences = filters.CharFilter(lookup_expr='icontains')
    adapter_content = filters.CharFilter(lookup_expr='icontains')
    sample_name = filters.CharFilter(lookup_expr='icontains')
    flowcell = filters.CharFilter(lookup_expr='icontains')
    lane = filters.CharFilter(lookup_expr='icontains')
    row = filters.CharFilter(lookup_expr='icontains')
    total_sequences = filters.CharFilter(lookup_expr='icontains')
    sequence_length = filters.CharFilter(lookup_expr='icontains')
    GC = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Fastqc
        fields = ['project_name','patient_id','sequence','sample_type','basic_statistics','per_base_sequence_quality',
        'per_tile_sequence_quality','per_sequence_quality_scores','Per_base_sequence_content','per_sequence_gc_content',
        'per_base_n_content','sequence_length_distribution','sequence_duplication_levels','overrepresented_sequences',
        'adapter_content','sample_name','flowcell','lane','row','total_sequences','sequence_length','GC' ]


class patient_data(ListAPIView):
    serializer_class = patientserializer1
    filter_backends = (DjangoFilterBackend, SearchFilter )
    permission_classes = (AllowAny,)
    pagination_class = LargeResultsSetPagination
    filter_class = AdvancedFilter
    filter_fields = ('project_name','patient_id','sequence','sample_type','basic_statistics','per_base_sequence_quality',
        'per_tile_sequence_quality','per_sequence_quality_scores','Per_base_sequence_content','per_sequence_gc_content',
        'per_base_n_content','sequence_length_distribution','sequence_duplication_levels','overrepresented_sequences',
        'adapter_content','sample_name','flowcell','lane','row','total_sequences','sequence_length','GC')
    search_fields = ('basic_statistics','per_base_sequence_quality',
        'per_tile_sequence_quality','per_sequence_quality_scores','Per_base_sequence_content','per_sequence_gc_content',
        'per_base_n_content','sequence_length_distribution','sequence_duplication_levels','overrepresented_sequences',
        'adapter_content','sample_name','flowcell','lane','row','total_sequences','sequence_length','GC')
    def get_queryset(self):
        QuerySet = Fastqc.objects.all()
        return QuerySet

def multiqc_report(request, project=None, pid=None, sname=None, stype=None):
    if request.method == 'GET':
        path_name = '../FastQ_Storage_Repository/Project/' + project + '/' + pid + '/' + sname + \
                        '/Fastqc_folder' + '/' + stype + '/multiqc_report.html'
        return render(request, path_name)


def fastqc_report(request, project=None, pid=None, sname=None, stype=None, path=None):
    if request.method == 'GET':
        path_name = '../FastQ_Storage_Repository/Project/' + project + '/' + pid + '/' + sname + '/' + \
            '/Fastqc_folder' + '/' + stype + '/' + path + '/' + 'fastqc_report.html'
        return render(request, path_name)
        
class fastqc_report1(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        path_name = 'Project/ICGC/6/DNA/Fastqc_folder/Normal/00060131_TruseqNano_HGWGGDSXY_L1_R1_fastqc/fastqc_report.html'
        return render(request, path_name)