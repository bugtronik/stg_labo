
# Create your views here.
from django.shortcuts import render
from locality.models import Locality
from locality.forms import LocalityForm

def locality(request):

    localities = Locality.objects.all()
    save_data = ''
    
    if request.method == 'POST':
        form = LocalityForm(request.POST)
        if form.is_valid():
            form.save()
            save_data = 'ok'
    else:
        form = LocalityForm()
    
    return render(request, 
                  'locality/locality.html',
                   {'form': form,
                    'localities': localities,
                    'save_data': save_data})


def locality_update(request, id):
    locality = Locality.objects.get(id=id)
    localities = Locality.objects.all()
    form = LocalityForm()
    update_data = ''

    if request.method == 'POST':
        form_update = LocalityForm(request.POST, instance=locality)
        if form_update.is_valid():
            form_update.save()
            update_data = 'ok'
    else:
        form_update = LocalityForm(instance=locality)
    return render(request, 
                  'locality/locality.html',
                  {'form_update': form_update,
                   'form': form,
                  'localities': localities,
                  'update_data': update_data})
