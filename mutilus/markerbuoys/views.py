from django.http import HttpResponse
from django.template import loader

from markerbuoys import MarkerBuoy

def main(request):
    template = loader.get_template('markerbuoys.html')

    buoy_cm_east = MarkerBuoy("Cardinal Mark East")

    context = {
        'buoys' : [buoy_cm_east]
    }

    return HttpResponse(template.render(context, request))