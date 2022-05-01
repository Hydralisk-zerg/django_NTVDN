from django.shortcuts import render
from django.http import HttpResponse, FileResponse, HttpResponseRedirect,  HttpResponseNotAllowed, JsonResponse
from django.templatetags.static import static

from django.views import View

from django.template import loader

class MyView(View):

    def get(self, request):
        print(request.GET)
        return HttpResponse('This is GET')

    def post(self, request):
        print(request.POST)
        return HttpResponse('This is POST')

    

def main(request):
    test_template = loader.get_template(template_name='main.html')
    return render(request, 'main.html')


def text(request):
    return HttpResponse('Htis is text in lesson 3')


def file(request):
    # print(static('download.jpg'))
    return FileResponse(open(static("img/download.jpg"), "rb"))


def redirect(request):
    return HttpResponseRedirect('http://www.google.com')


def not_allowed(request):
    return HttpResponseNotAllowed('nyama nishtu')


def json(request):
    return JsonResponse({i: i + i for i in range(1, 20)}, safe=False)
    