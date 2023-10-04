from django.shortcuts import render
from .models import DDMOdel
from django.http import JsonResponse

# Create your views here.

def drop(request):
    return render(request, 'home.html')

def saveimage(request):
    if request.method == 'POST':
        image = request.FILES.get('DDimage')

        if image:
            ss = DDMOdel.objects.create(image=image)
            ssid=ss.id
            print('id',ssid)
            ssdata = DDMOdel.objects.get(id=ssid)
            return render(request, 'imagesucess.html', {'imgdb': ssdata, 'msgdb': 'Image added successfully'})

        
        else:
            return render(request,'home.html',{'msgdb':'Something wents wrong'})
    
    return JsonResponse({'message': 'Failed to save the image'})

def imagesucess(request):
    return render(request,'imagesucess.html')