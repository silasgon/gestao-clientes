from django.urls import path, include
from .views import persons_list
from .views import persons_new
from .views import persons_update
from .views import persons_delete
from .views import PersonList
from .views import PersonDetail


urlpatterns = [
    path('list/', persons_list, name="person_list"),
    path('new/', persons_new, name="person_new"),
    path('update/<int:id>/', persons_update, name="person_update"),
    path('delete/<int:id>/', persons_delete, name="person_delete"),
    path('person_list/', PersonList.as_view()),
    path('person_detail/<int:pk>/', PersonDetail.as_view(), name="person_detail_cbv"),
]

