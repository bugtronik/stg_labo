
# Create your views here.
from django.shortcuts import render
from status.models import Status
from status.forms import StatusForm

def status(request):

    statuts = Status.objects.all()
    save_data = ''
    
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            save_data = 'ok'
    else:
        form = StatusForm()
    
    return render(request, 
                  'status/status.html',
                   {'form': form,
                    'statuts': statuts,
                    'save_data': save_data})

def status_update(request, id):
    status = Status.objects.get(id=id)
    statuts = Status.objects.all()
    form = StatusForm()
    update_data = ''

    if request.method == 'POST':
        form_update = StatusForm(request.POST, instance=status)
        if form_update.is_valid():
            form_update.save()
            update_data = 'ok'
    else:
        form_update = StatusForm(instance=status)
    return render(request, 
                  'status/status.html',
                  {'form_update': form_update,
                   'form': form,
                  'statuts': statuts,
                  'update_data': update_data})
