from django.urls import path
from . import views
from . import pdf
urlpatterns = [
    path('addres/<int:id>/', views.addresult, name='addres'),
    path('pdf/<int:id>/', pdf.pdfres, name='pdf'),
    path('result/<int:id>/', views.showresult, name='result'),
    path('details/<int:id>/', views.detailsres, name='details'),
 
]