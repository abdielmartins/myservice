from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Services
from django.utils import timezone

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.FILES['icon'] and request.FILES['image']:
            services = Services()
            services.title = request.POST['title']
            services.body = request.POST['body']
            services.icon = request.FILES['icon']
            services.image = request.FILES['image']
            services.pub_date = timezone.datetime.now()
            services.worker = request.user
            services.save()
            return redirect ('home')
        else:   
            return render(request, 'create.html', {'error': 'All fields are required'})
    else:    
        return render(request, 'services/create.html')