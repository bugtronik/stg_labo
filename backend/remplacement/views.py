from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from remplacement.models import Remplacement
from remplacement.forms import RemplacementForm 
@login_required
def remplacement(request):

    remplacements = models.Remplacement.objects.all()
    save_data = ''

    
    if request.method == 'POST':
        form = forms.RemplacementForm(request.POST)
        if form.is_valid():
            remplacement_form = form.save(commit=False)
            remplacement_form.user = request.user
            # on récupère la source, la localité avec leur id
            remplacement_form.save()
            save_data = 'ok'
            
    else:
        form = forms.RemplacementForm()
    
    return render(request, 
                  'remplacement/remplacement.html',
                   {'form': form,
                    'remplacements': remplacements,
                    'save_data': save_data})


def remplacement_update(request, id):
    remplacement = Remplacement.objects.get(id=id)
    remplacements = Remplacement.objects.all()
    form = forms.RemplacementForm()
    update_data = ''

    if request.method == 'POST':
        form_update = forms.RemplacementForm(request.POST, instance=remplacement)
        if form_update.is_valid():
            remplacement_form = form.save(commit=False)
            remplacement_form.user = request.user
            
            form_update.save()
            update_data = 'ok'
            
    else:    
        form_update = RemplacementForm(instance=remplacement)

    return render(request, 
                  'remplacement/remplacement.html',
                  {'form_update': form_update,
                   'form': form,
                  'remplacements': remplacements,
                  'update_data': update_data})


