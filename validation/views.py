from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Validation

@login_required
def validate(request):
    if request.method == 'POST':
        if request.POST['name'] and request.POST['surname'] and request.POST['birth_date'] and request.POST['cpf'] and request.FILES['profile_picture'] and request.FILES['profile_validation']:
            validation = Validation()
            validation.uservalid = request.user
            validation.name = request.POST['name']
            validation.surname = request.POST['surname']
            validation.birth_date = request.POST['birth_date']
            validation.cpf = request.POST['cpf']            
            validation.rg = request.POST['rg']
            validation.cel = request.POST['cel']
            validation.cep = request.POST['cep']
            validation.adress = request.POST['adress']
            validation.num = request.POST['num']
            validation.district = request.POST['district']
            validation.city = request.POST['city']
            validation.state = request.POST['state']           
            validation.profile_picture = request.FILES['profile_picture']
            validation.profile_validation = request.FILES['profile_validation']
            validation.save()
            return redirect ('home')
        else:   
            return render(request, 'validate.html', {'error': 'All fields are required'})
    else:    
        return render(request, 'validation/validate.html')