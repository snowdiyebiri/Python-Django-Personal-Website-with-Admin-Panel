from django.shortcuts import render
from .forms import ContactForm
from .models import Message

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save message to database
            Message.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                content=form.cleaned_data['message']
            )
            return render(request, 'contact/success.html', {'name': form.cleaned_data['name']})
    
    context = {
        'form': form
    }
    return render(request, 'contact/contact.html', context)
