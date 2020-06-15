from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Validation

@login_required
def validate(request):
    if request.method == 'POST':
        if request.POST['nome'] and request.POST['sobrenome'] and request.POST['birth_date'] and request.POST['cpf'] and request.FILES['profile_picture'] and request.FILES['profile_validation']:
            validation = Validation()
            validation.user = request.user
            validation.name = request.POST['name']
            validation.surname = request.POST['surname']
            validation.birth_date = request.POST['birth_date']
            validation.cpf = request.POST['cpf']            
            validation.profile_picture = request.FILES['profile_picture']
            validation.profile_validation = request.FILES['profile_validation']
            validation.save()
            return redirect ('/services/main')
        else:   
            return render(request, 'validate.html', {'error': 'All fields are required'})
    else:    
        return render(request, 'validation/validate.html')