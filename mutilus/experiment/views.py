from django.http import HttpResponse
from django.template import loader

def experiment(request, experimentNumber):

    # Get the experiment information from firebase

    # Decide the list of images which are going to be shown

    # For each image, show some options to click

    # Store the result
    


    # Load the experiment template
    template = loader.get_template('experiment.html')
    # Context with experimentNumber
    context = {'experimentNumber': experimentNumber}
    # Render the template with context
    return HttpResponse(template.render(context, request))


def begin(request, experimentNumber):
    # Load the begin template
    template = loader.get_template('begin.html')
    # Context with experimentNumber
    context = {'experimentNumber': experimentNumber}
    # Render the template with context
    return HttpResponse(template.render(context, request))
