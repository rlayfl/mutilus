from django.http import HttpResponse
from django.template import loader

def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def experiment(request):
    template = loader.get_template('experiment.html')
    return HttpResponse(template.render())