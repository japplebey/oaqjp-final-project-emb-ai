from flask import Flask, render_template, request 
from EmotionDetection import emotion_detector

#Initiate the flask app : Emotion Detector
app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    return render_template('index.html')


@app.route("/emotionDetector")
def get_emotions():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if (text_to_analyze == None or text_to_analyze == ""):
        return "Invalid text! Please try again!"

    # Pass the text to Emotion Detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Handle empty response
    if(response['dominant_emotion' == None]):
        return "Invalid text! Please try again!"

    # Format output
    output = format_output(response)    
    return output


def format_output(emotions):
    dominant_emotion = emotions['dominant_emotion']

    # Get number of entries in dictionary
    emotions_length = len(emotions);

    # Build output string
    count = 0
    output = "For the given statement, the system response is "
    for key, value in emotions.items():
        count += 1
        if (key != 'dominant_emotion'):
            if (count == (emotions_length-1)):
                output = output[:-2]   # take out extra comma
                fmt = ' and \'' + key + '\': ' + str(value) + '. '
            else:                
                fmt = '\'' + key + '\': ' + str(value) + ', '
            output = output + fmt

    output = output + 'The dominant emotion is ' + dominant_emotion + '.'

    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

