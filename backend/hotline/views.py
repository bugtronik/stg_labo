from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from . import models
from hotline.models import Hotline
from hotline.forms import HotlineForm

@login_required
def hotline(request):

    hotlines = models.Hotline.objects.all()
    sources = models.Source.objects.all()
    localities = models.Locality.objects.all()
    save_data = ''

    
    if request.method == 'POST':
        form = forms.HotlineForm(request.POST)
        if form.is_valid():
            hotline_form = form.save(commit=False)
            hotline_form.user = request.user
            # on récupère la source, la localité avec leur id
            source = models.Source.objects.get(id=request.POST.get('source'))
            locality = models.Locality.objects.get(id=request.POST.get('locality'))

            hotline_form.source = source
            hotline_form.locality = locality
            hotline_form.save()
            save_data = 'ok'
            
    else:
        form = forms.HotlineForm()
    
    return render(request, 
                  'hotline/hotline.html',
                   {'form': form,
                    'hotlines': hotlines,
                    'sources': sources,
                    'localities': localities,
                    'save_data': save_data})

def hotline_update(request, id):
    hotline = Hotline.objects.get(id=id)
    hotlines = Hotline.objects.all()
    sources = models.Source.objects.all()
    localities = models.Locality.objects.all()
    form = forms.HotlineForm()
    update_data = ''

    if request.method == 'POST':
        form_update = forms.HotlineForm(request.POST, instance=hotline)
        print(form_update)
        if form_update.is_valid():
            hotline_form = form.save(commit=False)
            hotline_form.user = request.user
            
            source = models.Source.objects.get(id=request.POST.get('source'))
            locality = models.Locality.objects.get(id=request.POST.get('locality'))
            hotline_form.source = source
            hotline_form.locality = locality
            form_update.save()
            update_data = 'ok'
            
    else:    
        form_update = HotlineForm(instance=hotline)

    return render(request, 
                  'hotline/hotline.html',
                  {'form_update': form_update,
                   'form': form,
                  'hotlines': hotlines,
                  'sources': sources,
                  'localities': localities,
                  'update_data': update_data})

