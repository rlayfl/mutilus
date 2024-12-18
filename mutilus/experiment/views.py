from django.http import HttpResponse, JsonResponse
from django.template import loader

import requests
import time
import json

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

    URL = 'https://mutilus-7d3b1-default-rtdb.europe-west1.firebasedatabase.app/experiments/'+uid+'.json?auth=AIzaSyAQt-LmICWeHMo8tNGDgvh8a0_2OS-nnP0'

    jsondata = {
        "answer": answer,
        "realAnswer": realAnswer
    }
     
    response = requests.post(URL, json=jsondata, headers={"Content-Type": "application/json"})

    if (response.status_code != 200) :
             raise Exception("An error occurred pushing to Firebase: " + response.text)    
    
    return JsonResponse({
        "message": "Data successfully uploaded to Firebase",
        "uid": uid,
        "status_code": response.status_code
    })