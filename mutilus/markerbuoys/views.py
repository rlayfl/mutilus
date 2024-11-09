from django.http import HttpResponse
from django.template import loader

def main(request):
    template = loader.get_template('markerbuoys.html')

    context = {
        'buoys' : ['north', 'east', 'south', 'west']
    }

    return HttpResponse(template.render(context, request))