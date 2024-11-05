
from django.shortcuts import render
from source.models import Source
from source.forms import SourceForm

def source(request):

    sources = Source.objects.all()
    save_data = ''
    
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            save_data = 'ok'
    else:
        form = SourceForm()
    
    return render(request, 
                  'source/source.html',
                   {'form': form,
                    'sources': sources,
                    'save_data': save_data})

def source_update(request, id):
    source = Source.objects.get(id=id)
    sources = Source.objects.all()
    form = SourceForm()
    update_data = ''

    if request.method == 'POST':
        form_update = SourceForm(request.POST, instance=source)
        if form_update.is_valid():
            form_update.save()
            update_data = 'ok'
    else:
        form_update = SourceForm(instance=source)
    return render(request, 
                  'source/source.html',
                  {'form_update': form_update,
                   'form': form,
                  'sources': sources,
                  'update_data': update_data})