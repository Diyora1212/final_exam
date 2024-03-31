from django.urls import path
from tasks.task2.views import VacancyList
from tasks.task2.api_endpoints.VacancyCreate.views import VacancyListCreateView

urlpatterns = [
    path('vacancies-filter/', VacancyList.as_view(), name='vacancy-list-filter'),
    path('vacancy-list/', VacancyListCreateView.as_view(), name='vacancy-list-create'),

]
