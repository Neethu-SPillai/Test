from django.views.generic import  TemplateView,ListView, CreateView, UpdateView, DeleteView,View,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Vehicle
from django.urls import reverse_lazy


class HomeView(TemplateView):
    template_name = 'home.html'

class VehicleListView1(ListView):
    model = Vehicle
    template_name = 'view1.html'
    context_object_name = 'vehicles'

class VehicleListView2(ListView):
    model = Vehicle
    template_name = 'view2.html'
    context_object_name = 'vehicles'

class VehicleListView3(ListView):
    model = Vehicle
    template_name = 'view3.html'
    context_object_name = 'vehicles'

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'view.html'
    context_object_name = 'vehicles'

class VehicleCreateView(CreateView):
    model = Vehicle
    template_name = 'add.html'
    fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url = reverse_lazy('vehicles:vehicle_list')


class VehicleUpdateView(UpdateView):
    model = Vehicle
    template_name = 'add.html'
    fields = ['vehicle_number', 'vehicle_type', 'vehicle_model', 'vehicle_description']
    success_url = reverse_lazy('vehicles:vehicle_list')

    # def test_func(self):
    #     return self.request.user.user_access in ['superadmin', 'admin']

class VehicleDeleteView(DeleteView):
    model = Vehicle
    template_name = 'delete.html'
    success_url=reverse_lazy('vehicles:vehicle_list')

    # def test_func(self):
    #     return self.request.user.user_access == 'superadmin'