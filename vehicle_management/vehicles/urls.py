from django.urls import path
from vehicles.views import VehicleListView, VehicleCreateView, VehicleUpdateView, VehicleDeleteView,HomeView,VehicleListView1,VehicleListView2,VehicleListView3
app_name="vehicles"
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('view1/',VehicleListView1.as_view(), name='view1'),
    path('view2/', VehicleListView2.as_view(), name='view2'),
    path('view3/', VehicleListView3.as_view(), name='view3'),

    path('vehicles/', VehicleListView.as_view(), name='vehicle_list'),
    path('create/', VehicleCreateView.as_view(), name='vehicle_create'),
    path('update/<int:pk>/', VehicleUpdateView.as_view(), name='vehicle_update'),
    path('delete/<int:pk>/', VehicleDeleteView.as_view(), name='vehicle_delete'),
]