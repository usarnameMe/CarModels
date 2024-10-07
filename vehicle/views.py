from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle
from .forms import VehicleForm


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})


def vehicle_detail(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})


def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'add_vehicle.html', {'form': form})


def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_detail', pk=vehicle.pk)
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'edit_vehicle.html', {'form': form, 'vehicle': vehicle})
