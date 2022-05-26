from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from lesson_7.forms import MyForms


# def my_form(request):
#     return HttpResponse(MyForms().as_p())

def my_form(request):
    print(request.FILES)
    form = MyForms(request.POST or None, request.FILES or None)
   
    if form.is_valid():
        print(f"Valid {form.cleaned_data}") 
        file_path = os.path.join(settings.MEDIA_ROOT, form.cleaned_data['profile_picture'].name)
        
        with open(file_path, 'wb+') as local_file:
            for chunk in form.cleaned_data['profile_picture']:
                local_file.write(chunk)
    else:
        print(f"Not valid {form.errors}")  
        
        
    return render(request, 'form_page.html', context={'form':form})


# class ModelFormView(FormView):
#     form_class = MyForms
#     template_name = 'model_form_page.html'
#     success_url = reverse_lazy('modelform')
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
        
    

