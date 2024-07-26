from django.urls import path
from .Controllers import NewtonController,SecanteController

urlpatterns = [
    path('',                  NewtonController.Index,             name='Index'             ),
    path('UserManual',        NewtonController.UserManual,        name='UserManual'        ),
    path('ShowNewtonRaphson', NewtonController.ShowNewtonRaphson, name='ShowNewtonRaphson' ),
    path('SaveNewtonRaphson', NewtonController.SaveNewtonRaphson, name='SaveNewtonRaphson' ),
    path('ShowSecante',       SecanteController.ShowSecante,      name='ShowSecante'       ),
    path('SaveSecante',       SecanteController.SaveSecante,      name='SaveSecante'       ),

]
