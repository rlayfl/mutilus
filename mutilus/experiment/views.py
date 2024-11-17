from django.http import HttpResponse
from django.template import loader

import requests

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

def upload_experiment_data_to_firebase():

    URL = 'https://mutilus-7d3b1-default-rtdb.europe-west1.firebasedatabase.app/Experiments/.json?auth=AIzaSyAQt-LmICWeHMo8tNGDgvh8a0_2OS-nnP0'

    experimentData = {

    }

    response = requests.post(URL, data=experimentData,headers={"Content-Type": "application/json"})

    if (response.status_code != 200) :
            raise Exception("An error occurred pushing to Firebase: " + response.text)
