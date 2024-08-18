from django.urls import path
from .Controllers import NewtonController,SecanteController,PolinomioNewtonController,LagrangeController

urlpatterns = [
    path('',                  NewtonController.Index,             name='Index'             ),
    path('SaveClient',        NewtonController.SaveClient,        name='SaveClient'        ),
    path('Deleteclient/<int:id>/',NewtonController.Deleteclient,      name='Deleteclient'  ),
    path('ShowNewtonRaphson', NewtonController.ShowNewtonRaphson, name='ShowNewtonRaphson' ),
    path('SaveNewtonRaphson', NewtonController.SaveNewtonRaphson, name='SaveNewtonRaphson' ),
    path('ShowSecante',       SecanteController.ShowSecante,      name='ShowSecante'       ),
    path('SaveSecante',       SecanteController.SaveSecante,      name='SaveSecante'       ),
    path('ShowPolinomioNewton',PolinomioNewtonController.ShowPolinomioNewton,name='ShowPolinomioNewton'),
    path('SavePolinomioNewton',PolinomioNewtonController.SavePolinomioNewton,name='SavePolinomioNewton'),
    path('downloadchartlagrange',LagrangeController.DownloadChart,name='downloadchartlagrange'),
    path('langrange',          LagrangeController.calculate_cost,          name='langrange'         ),
]

