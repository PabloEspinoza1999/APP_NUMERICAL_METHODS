from django.urls import path
from .Controllers import NewtonController,SecanteController,PolinomioNewtonController,LagrangeController

urlpatterns = [
    path('',                  NewtonController.Index,             name='Index'             ),
    path('UserManual',        NewtonController.UserManual,        name='UserManual'        ),
    path('ShowNewtonRaphson', NewtonController.ShowNewtonRaphson, name='ShowNewtonRaphson' ),
    path('SaveNewtonRaphson', NewtonController.SaveNewtonRaphson, name='SaveNewtonRaphson' ),
    path('ShowSecante',       SecanteController.ShowSecante,      name='ShowSecante'       ),
    path('SaveSecante',       SecanteController.SaveSecante,      name='SaveSecante'       ),
    path('show_newton_raphson',NewtonController.show_newton_raphson,name='show_newton_raphson'),
    path('save_newton_raphson',NewtonController.save_newton_raphson,name='save_newton_raphson'),
    path('ShowPolinomioNewton',PolinomioNewtonController.ShowPolinomioNewton,name='ShowPolinomioNewton'),
    path('SavePolinomioNewton',PolinomioNewtonController.SavePolinomioNewton,name='SavePolinomioNewton'),
    path('downloadchartlagrange',      LagrangeController.DownloadChart,name='downloadchartlagrange'),
    path('langrange',          LagrangeController.Index,name='langrange'),
]
