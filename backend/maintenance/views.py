from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from maintenance.models import Maintenance
from maintenance.forms import MaintenanceForm 
@login_required
def maintenance(request):

    maintenances = models.Maintenance.objects.all()
    sources = models.Source.objects.all()
    localities = models.Locality.objects.all()
    save_data = ''

    
    if request.method == 'POST':
        form = forms.MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance_form = form.save(commit=False)
            maintenance_form.user = request.user
            # on récupère la source, la localité avec leur id
            source = models.Source.objects.get(id=request.POST.get('source'))
            locality = models.Locality.objects.get(id=request.POST.get('locality'))

            maintenance_form.source = source
            maintenance_form.locality = locality
            maintenance_form.save()
            save_data = 'ok'
            
    else:
        form = forms.MaintenanceForm()
    
    return render(request, 
                  'maintenance/maintenance.html',
                   {'form': form,
                    'maintenances': maintenances,
                    'sources': sources,
                    'localities': localities,
                    'save_data': save_data})


def maintenance_update(request, id):
    maintenance = Maintenance.objects.get(id=id)
    maintenances = Maintenance.objects.all()
    sources = models.Source.objects.all()
    localities = models.Locality.objects.all()
    form = forms.MaintenanceForm()
    update_data = ''

    if request.method == 'POST':
        form_update = forms.MaintenanceForm(request.POST, instance=maintenance)
        if form_update.is_valid():
            maintenance_form = form.save(commit=False)
            maintenance_form.user = request.user
            
            source = models.Source.objects.get(id=request.POST.get('source'))
            locality = models.Locality.objects.get(id=request.POST.get('locality'))
            maintenance_form.source = source
            maintenance_form.locality = locality
            form_update.save()
            update_data = 'ok'
            
    else:    
        form_update = MaintenanceForm(instance=maintenance)

    return render(request, 
                  'maintenance/maintenance.html',
                  {'form_update': form_update,
                   'form': form,
                  'maintenances': maintenances,
                  'sources': sources,
                  'localities': localities,
                  'update_data': update_data})

