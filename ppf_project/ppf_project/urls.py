"""ppf_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from ppfapp import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('jobcard/<str:station>/', views.job_card, name='jobcard'),
    path('add_item', views.add_item_in_master,name='add_item'),
    path('login', views.loginfm, name='login'),
    path('logout', views.logoutfm, name='logout'),
    path('console', views.console, name='console'),

    path('upload', views.upload,name='upload'),
    path('summary', views.production_summary,name='summary'),
    path('changes', views.changes,name='changes'),
    path('micro_mrp', views.micro_mrp, name='micro_mrp'),

    #path('item_status_change', views.item_status_change, name='item_status_change'),

    path('produced', views.production_submit,name='produced'),
    path('planning', views.planning_submit,name='planning'),
    path('opening', views.opening_bal_submit,name='opening'),
    path('damage', views.damage_submit,name='damage'),
    path('store', views.material_requisition_store, name='store'),
    path('sponge', views.material_requisition_sponge, name='sponge'),
    path('bms', views.material_requisition_bms, name='bms'),
]
