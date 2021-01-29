from django.shortcuts import render, reverse, redirect
from .forms import ContactMessageForm
# from django.views.generic import CreateView
from django.contrib import messages

# Create your views here.


def contact(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            messages.success(request, f'Mesajiniz gonderildi, tezlikle sizinle elaqe saxlanilacaq!')
            return redirect('index_page')
    else:
        form = ContactMessageForm
    return render(request, 'contact/contact_page.html', {'form': form})


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # username = form.cleaned_data.get('username')
#             messages.success(request, f'Mesajiniz gonderildi, tezlikle sizinle elaqe saxlanilacaq!')
#             return redirect('stories-index')
#     else:
#         form = ContactForm
#     return render(request, 'stories/contact.html', {'form': form})



# class ContactCreateView(CreateView):
#     form_class = ContactMessageForm
#     template_name = 'contact/contact_page.html'
#     success_url = reverse('index_page')
