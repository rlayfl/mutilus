from django.http import HttpResponse
from django.template import loader

from mutilus_classes import marker_buoy

def main(request):
    template = loader.get_template('markerbuoys.html')

    buoy_cm_north = marker_buoy.MarkerBuoy("Cardinal Mark North")
    buoy_cm_east = marker_buoy.MarkerBuoy("Cardinal Mark East")
    buoy_cm_south = marker_buoy.MarkerBuoy("Cardinal Mark South")
    buoy_cm_west = marker_buoy.MarkerBuoy("Cardinal Mark West")

    context = {
        'buoys' : [buoy_cm_north, buoy_cm_east, buoy_cm_south, buoy_cm_west]
    }

    return HttpResponse(template.render(context, request))
