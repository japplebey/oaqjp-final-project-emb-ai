# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request 
from EmotionDetection import emotion_detector

#Initiate the flask app : Emotion Detector
app = Flask("Emotion Detector")

@app.route("\emotionDetector")
def (get_emotions):
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to Emotion Detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Format HTTP output
    output = "For the given statemeent, the system response is"
    dominant = response['dominant_emotion']
 
    # 
    response_length = response.len();
    count = 0
    for key, value in response.items():
        if (key != 'dominant_emotion'):
            a = ' \'' + key + '\': ' + value + ','
            output += entry
        output
    
    return output

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
