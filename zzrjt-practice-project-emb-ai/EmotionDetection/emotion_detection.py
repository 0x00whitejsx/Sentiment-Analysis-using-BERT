import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=payload, headers=headers)
    
    # Convert response text to dictionary
    response_dict = json.loads(response.text)
    
    # Extract required emotions and their scores
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    emotion_scores = {emotion: response_dict['emotion'][emotion]['score'] for emotion in emotions}
    
    # Find dominant emotion
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Create output dictionary
    output = {
        'anger': emotion_scores['anger'],
        'disgust': emotion_scores['disgust'],
        'fear': emotion_scores['fear'],
        'joy': emotion_scores['joy'],
        'sadness': emotion_scores['sadness'],
        'dominant_emotion': dominant_emotion
    }
    
    return output
