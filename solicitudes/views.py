from django.shortcuts import render
from django.contrib import messages
from .forms import solicitudForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .logic.logic_solicitudes import getSolicitudes, createSolicitud

def solicitudesList(request):
    listaSol = getSolicitudes()
    context = {
        'solicitudesList':listaSol
    }
    return render(request, 'solicitudes/solicitudes.html', context)

def postSolicitud(request):
    if request.method == 'POST':
        form = solicitudForm(request.POST)
        if form.is_valid():
            createSolicitud(form)
            messages.add_message(request, messages.SUCCESS, 'Solicitud created successful')
            return HttpResponseRedirect(reverse('createSolicitud'))
        else:
            print(form.errors)
    else:
        form = solicitudForm()

    context = {
        'form': form,
    }

    return render(request, 'solicitudes/createSolicitudes.html', context)