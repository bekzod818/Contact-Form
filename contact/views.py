from django.shortcuts import render, redirect
from .forms import ContactForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contactform.html', context)


def success_view(request):
    return render(request, 'success.html')
