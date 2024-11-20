from django.http import HttpResponse
from django.template import loader

from mutilus_classes import marker_buoy

# I think this is overkill to show 9 pictures on the page
def main(request):
    template = loader.get_template('markerbuoys.html')

    buoy_cm_north = marker_buoy.MarkerBuoy("Cardinal Mark North")
    buoy_cm_east = marker_buoy.MarkerBuoy("Cardinal Mark East")
    buoy_cm_south = marker_buoy.MarkerBuoy("Cardinal Mark South")
    buoy_cm_west = marker_buoy.MarkerBuoy("Cardinal Mark West")
    buoy_idm = marker_buoy.MarkerBuoy("Isolated Danger Mark")
    buoy_port = marker_buoy.MarkerBuoy("Port")
    buoy_starboard = marker_buoy.MarkerBuoy("Starboard")
    buoy_safe_water_mark = marker_buoy.MarkerBuoy("Safe Water Mark")
    buoy_wreck_mark = marker_buoy.MarkerBuoy("Wreck Mark")

    context = {
        'buoys' : [buoy_cm_north, buoy_cm_east, buoy_cm_south, buoy_cm_west, buoy_idm, buoy_port, buoy_starboard, buoy_safe_water_mark, buoy_wreck_mark]
    }

    return HttpResponse(template.render(context, request))
