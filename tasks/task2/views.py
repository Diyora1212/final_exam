from rest_framework import generics
from rest_framework import django
from django_filters import rest_framework as filters
from tasks.task2.models import Vacancy
from tasks.task2.serializers import VacancySerializer
from rest_framework.response import Response
from rest_framework import status


class VacancyFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="salary", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="salary", lookup_expr='lte')

    class Meta:
        model = Vacancy
        fields = ['name', 'salary']


class VacancyList(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VacancyFilter