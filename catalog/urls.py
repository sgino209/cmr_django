# (c) Shahar Gino, April-2018, sgino209@gmail.com
#
# Catalog URLs

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.PersonListView.as_view(), name='persons'),
    path('persons/exportcsv', views.PersonExportCsvView, name='persons_exportcsv'),
    path('persons/exportpdf', views.PersonExportPdfView, name='persons_exportpdf'),
    path('persons/sendsms', views.PersonSendSmsView, name='persons_sendsms'),
    path('person/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
    path('person/create/', views.PersonCreate.as_view(), name='person_create'),
    path('person/<int:pk>/update/', views.PersonUpdate.as_view(), name='person_update'),
    path('person/<int:pk>/delete/', views.PersonDelete.as_view(), name='person_delete'),
]
