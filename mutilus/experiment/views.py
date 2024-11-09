from django.http import HttpResponse
from django.template import loader

def experiment(request):
    template = loader.get_template('experiment.html')
    return HttpResponse(template.render())


def begin(request):
    template = loader.get_template('begin.html')
    return HttpResponse(template.render())