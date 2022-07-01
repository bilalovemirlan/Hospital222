from django.shortcuts import render

from hospital.models import Hospital


def index(request):
    return render(request, 'hospital/index.html')

def hospitals(request):
    if request.method == 'GET':
        hospitals = Hospital.objects.all()
        context = {'hospitals': hospitals}
        return render(request, 'hospital/Hospitals.html', context)
