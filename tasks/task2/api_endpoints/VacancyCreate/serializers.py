from rest_framework.serializers import ModelSerializer

from tasks.task2.models import Vacancy


class VacancyListCreateSerializer(ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('name', 'salary')
