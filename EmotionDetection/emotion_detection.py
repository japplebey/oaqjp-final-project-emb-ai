import requests
import json

def emotion_detector(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # Emotion Detecctor URL
  # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
  # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
   
   # If the response status code is 400, return dictionary of None's
    if response.status_code == 400:
        error_dict = {'anger':None, 'disgust':None, 'fear':None, 'joy':None, 'sadness':None, 'dominant_emotion':None }
        return error_dict
        
     # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    # Extracting emotions and scores dictionary from the response
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # Get max score
    max_value = max(emotions.values())

    # Set dominant emotion
    dominant_emotion = ""
    for key, value in emotions.items():
        if value == max_value:
          dominant_emotion = key
          break  # Stop after finding the first match
    emotions["dominant_emotion"] = dominant_emotion
    
    return emotions
 
