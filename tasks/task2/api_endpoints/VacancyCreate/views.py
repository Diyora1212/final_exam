from rest_framework.generics import ListCreateAPIView
from tasks.task2.api_endpoints.VacancyCreate.serializers import VacancyListCreateSerializer
from tasks.task2.models import Vacancy


class VacancyListCreateView(ListCreateAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancyListCreateSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


__all__ = ('VacancyListCreateView',)
