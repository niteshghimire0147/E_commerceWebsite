from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views.generic import CreateView

from  .forms import Khaltiform
from .models import Khalti
# Create your views here.

def khalti(request):

    # if request.method == 'POST':
    #     khalti = Khaltiform(request.POST, request.FILES)
    #     userprofile = Khalti.objects.get(user=self.request.user)
    #     if khalti.is_valid():
    #         khalti.save()
    #         return redirect('/')
    # else:
    #     khalti = Khaltiform()
    # context = {'khalti':khalti}
    return render(request, 'payment.html')
