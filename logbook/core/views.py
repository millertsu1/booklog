from django.shortcuts import render, redirect
from .forms import MaintenanceLogForm

# Create your views here.

def home(request):
    return render(request, 'core/index.html')



def create_log(request):
    if request.method == 'POST':
        form = MaintenanceLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_success')  # Redirige a una página de éxito
    else:
        form = MaintenanceLogForm()

    return render(request, 'core/create_log.html', {'form': form})


def log_success(request):
    return render(request, 'core/success.html')

