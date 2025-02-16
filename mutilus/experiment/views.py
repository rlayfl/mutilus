from django.http import HttpResponse, JsonResponse
from django.template import loader

import requests
import time
import json
import random
import os
from django.conf import settings
from PIL import Image

def experiment(request, experimentNumber):

    # Define the path to the images directory
    images_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'marker_buoys', 'real', 'cardinal_mark_north')

    print(images_path)

    # Get the list of image files
    image_files = [f for f in os.listdir(images_path) if os. path.isfile(os.path.join(images_path, f))]

    # Create an array to hold image information
    images_info = []

    # Loop through the image files and get their resolution
    for image_file in image_files:
        image_path = os.path.join(images_path, image_file)
        with Image.open(image_path) as img:
            width, height = img.size
            images_info.append({
                'filename': image_file,
                'width': width,
                'height': height,
                'type': '1'
            })

    # Define the buttons list
    buttons = [
        {'id': 'cmn', 'data_value': 1, 'text': 'Cardinal Mark North'},
        {'id': 'cme', 'data_value': 2, 'text': 'Cardinal Mark East'},
        {'id': 'cms', 'data_value': 3, 'text': 'Cardinal Mark South'},
        {'id': 'cmw', 'data_value': 4, 'text': 'Cardinal Mark West'},
        {'id': 'smc2s', 'data_value': 5, 'text': 'Special Mark Class 2 Solar'},
        {'id': 'idm', 'data_value': 6, 'text': 'Isolated Danger Mark'},
        {'id': 'swmt2', 'data_value': 7, 'text': 'Safe Water Mark Type 2'},
        {'id': 'psm', 'data_value': 8, 'text': 'Port (Left) Side Marker'},
        {'id': 'ssm', 'data_value': 9, 'text': 'Starboard (Right) Side Marker'}
    ]
    
    # Shuffle the buttons list
    random.shuffle(buttons)

    # Load the experiment template
    template = loader.get_template('experiment.html')
    # Context with experimentNumber, buttons, and images_info
    context = {
        'experimentNumber': experimentNumber,
        'buttons': buttons,
        'images_info': images_info
    }

    print(images_info)

    # Render the template with context
    return HttpResponse(template.render(context, request))


def begin(request, experimentNumber):
    # Load the begin template
    template = loader.get_template('begin.html')
    # Context with experimentNumber
    context = {'experimentNumber': experimentNumber}
    # Render the template with context
    return HttpResponse(template.render(context, request))

def upload_experiment_data_to_firebase(formData):

    uid = formData.POST['uid']
    password = formData.POST['password']

    URL = 'https://mutilus-7d3b1-default-rtdb.europe-west1.firebasedatabase.app/experiments/.json?auth=AIzaSyAQt-LmICWeHMo8tNGDgvh8a0_2OS-nnP0'

    jsondata = {
        "uid": uid,
        "password": password
    }

    response = requests.post(URL, json=jsondata, headers={"Content-Type": "application/json"})

    print("RESPONSEEEE")
    print(response.text)
    print(response.status_code)

    if (response.status_code != 200) :
             raise Exception("An error occurred pushing to Firebase: " + response.text)    
    
    return JsonResponse({
        "message": "Data successfully uploaded to Firebase",
        "uid": uid,
        "status_code": response.status_code
    })

def upload_experiment_answer_to_firebase(formData):
     
    uid = formData.POST['uid']
    answer = formData.POST['answer']
    realAnswer = formData.POST['realAnswer']
    timeElapsed = formData.POST['timeElapsed']

    URL = 'https://mutilus-7d3b1-default-rtdb.europe-west1.firebasedatabase.app/answers/'+uid+'.json?auth=AIzaSyAQt-LmICWeHMo8tNGDgvh8a0_2OS-nnP0'

    jsondata = {
        "answer": answer,
        "realAnswer": realAnswer,
        "timeElapsed": timeElapsed
    }
     
    response = requests.post(URL, json=jsondata, headers={"Content-Type": "application/json"})

    if (response.status_code != 200) :
             raise Exception("An error occurred pushing to Firebase: " + response.text)    
    
    return JsonResponse({
        "message": "Data successfully uploaded to Firebase",
        "uid": uid,
        "status_code": response.status_code
    })