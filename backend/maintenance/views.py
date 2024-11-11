from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from maintenance.models import Maintenance
from maintenance.forms import MaintenanceForm 
@login_required
def maintenance(request):

    maintenances = models.Maintenance.objects.all()
    statuts = models.Status.objects.all()
    hotlines = models.Hotline.objects.all()
    save_data = ''

    
    if request.method == 'POST':
        form = forms.MaintenanceForm(request.POST)
        print(form)
        if form.is_valid():
            maintenance_form = form.save(commit=False)
            maintenance_form.user = request.user
            # on récupère la source, la localité avec leur id
            status = models.Status.objects.get(id=request.POST.get('status'))
            hotline = models.Hotline.objects.get(id=request.POST.get('hotline'))

            maintenance_form.status = status
            maintenance_form.hotline = hotline
            maintenance_form.save()
            save_data = 'ok'
            
    else:
        form = forms.MaintenanceForm()
    
    return render(request, 
                  'maintenance/maintenance.html',
                   {'form': form,
                    'maintenances': maintenances,
                    'statuts': statuts,
                    'hotlines': hotlines,
                    'save_data': save_data})


def maintenance_update(request, id):
    maintenance = Maintenance.objects.get(id=id)
    maintenances = Maintenance.objects.all()
    statuts = models.Status.objects.all()
    hotlines = models.Hotline.objects.all()
    form = forms.MaintenanceForm()
    update_data = ''

    if request.method == 'POST':
        form_update = forms.MaintenanceForm(request.POST, instance=maintenance)
        if form_update.is_valid():
            maintenance_form = form.save(commit=False)
            maintenance_form.user = request.user
            
            status = models.Status.objects.get(id=request.POST.get('status'))
            hotline = models.Hotline.objects.get(id=request.POST.get('hotline'))
            maintenance_form.status = status
            maintenance_form.hotline = hotline
            form_update.save()
            update_data = 'ok'
            
    else:    
        form_update = MaintenanceForm(instance=maintenance)

    return render(request, 
                  'maintenance/maintenance.html',
                  {'form_update': form_update,
                   'form': form,
                  'maintenances': maintenances,
                  'statuts': statuts,
                  'hotlines': hotlines,
                  'update_data': update_data})

