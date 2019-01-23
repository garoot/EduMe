from django.shortcuts import render

# Create your views here.
def broadcast_station(request):
    return render(request, 'EduControl/broadcast_station.html')

def index(request):
    return render(request, 'EduMe/index.html')
