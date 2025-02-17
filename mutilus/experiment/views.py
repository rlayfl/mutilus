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

    # Define the path to the images directories
    real_images_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'marker_buoys', 'real', 'cardinal_mark_north')
    synthetic_images_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'marker_buoys', 'synthetic', 'cardinal_mark_north')

    # Get the list of image files for real and fake images
    real_image_files = [f for f in os.listdir(real_images_path) if os.path.isfile(os.path.join(real_images_path, f))]
    synthetic_image_files = [f for f in os.listdir(synthetic_images_path) if os.path.isfile(os.path.join(synthetic_images_path, f))]

    # Create an array to hold image information
    images_info = []
    buoy_type = 1
    image_number = 1

    # Loop through the real image files and get their resolution
    for image_file in real_image_files:
        image_path = os.path.join(real_images_path, image_file)
        with Image.open(image_path) as img:
            width, height = img.size
            images_info.append({
                'filename': image_file,
                'width': width,
                'height': height,
                'type': buoy_type,
                'is_synthetic': False,
                'image_number': image_number
            })
            image_number += 1

    # Loop through the synthetic image files and get their resolution
    for image_file in synthetic_image_files:
        image_path = os.path.join(synthetic_images_path, image_file)
        with Image.open(image_path) as img:
            width, height = img.size
            images_info.append({
                'filename': image_file,
                'width': width,
                'height': height,
                'type': buoy_type,
                'is_synthetic': True,
                'image_number': image_number
            })
            image_number += 1

    # Shuffle the order of images_info
    random.shuffle(images_info)

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

def upload_experiment_answer_to_firebase(request):
    uid = request.POST['uid']
    answer = request.POST['answer']
    realAnswer = request.POST['realAnswer']
    timeElapsed = request.POST['timeElapsed']
    imageNumber = request.POST['imageNumber']
    imageHeight = request.POST['imageHeight']
    imageWidth = request.POST['imageWidth']
    isSynthetic = request.POST['isSynthetic']
    filename = request.POST['filename']
    answerNumber = request.POST['answerNumber']

    URL = f'https://mutilus-7d3b1-default-rtdb.europe-west1.firebasedatabase.app/answers/{uid}.json?auth=AIzaSyAQt-LmICWeHMo8tNGDgvh8a0_2OS-nnP0'

    jsondata = {
        "answer": answer,
        "realAnswer": realAnswer,
        "timeElapsed": timeElapsed,
        "imageNumber": imageNumber,
        "imageHeight": imageHeight,
        "imageWidth": imageWidth,
        "isSynthetic": isSynthetic,
        "filename": filename,
        "answerNumber": answerNumber
    }

    response = requests.post(URL, json=jsondata, headers={"Content-Type": "application/json"})

    if response.status_code != 200:
        raise Exception("An error occurred pushing to Firebase: " + response.text)

    return JsonResponse({
        "message": "Data successfully uploaded to Firebase",
        "uid": uid,
        "status_code": response.status_code
    })