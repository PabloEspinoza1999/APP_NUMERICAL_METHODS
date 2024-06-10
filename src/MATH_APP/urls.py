from django.urls import path
from .Controllers import NewtonController

urlpatterns = [
    path('', NewtonController.Index, name='Index'),
    path('ShowNewtonRaphson',NewtonController.ShowNewtonRaphson,name='ShowNewtonRaphson'),
    path('SaveNewtonRaphson',NewtonController.SaveNewtonRaphson,name='SaveNewtonRaphson'),

    # HERE ANOTHER URLS
]
