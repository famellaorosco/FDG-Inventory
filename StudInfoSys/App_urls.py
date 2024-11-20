from django.urls import path #If maging sabaw ka self locate mo sa views.py -CIMC
from . import views  # Ensure to import your views

# URL CONFIGURATION
urlpatterns = [
    path('', views.admin_homepage),
    path('Admin_Home.html', views.admin_homepage),
    path('Depreciated_Inv.html', views.depreciated_inventory),
    path('Purchase_Req.html', views.purchase_request),
    path('Add_Purch.html', views.add_purchase),
    path('Eval_Req.html', views.evaluation_request),
    path('Add_Supplier.html', views.add_supplier),
    path('Supplier_List.html', views.supplier_list),
    path('Equip_Maintenance.html', views.equipment_maintenance),
    path('Edit_Supplier.html', views.edit_supplier),
    path('update-stock/<int:facility_id>/', views.update_facility_stock, name='update_facility_stock'),
    path('add-inventory/', views.add_inventory, name='add_inventory'),
    path('add-inv/', views.add_inventory, name='add_inv'), # for Add_Inv html
    path('depart-inv/', views.facility_stock_list, name='depart_inv'),  # for Depart_Inv html
    path('update-stock/<int:facility_id>/', views.update_facility_stock, name='update_facility_stock'), #for View in list
]
