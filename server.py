""" Executing this module initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
"""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

#Initiate the flask app : Emotion Detector
app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """ Executing this function brings up the index.html page """
    return render_template('index.html')


@app.route("/emotionDetector")
def get_emotions():
    """
    Executing this function submits the request to the Watson
    Emotion Detector service and returns the response
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if text_to_analyze in (None, ""):
        return "Invalid text! Please try again!"

    # Pass the text to Emotion Detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Handle empty response
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format output
    output = format_output(response)
    return output


def format_output(emotions):
    """ This function formats the response to be returned
    to the user.
    """
    dominant_emotion = emotions['dominant_emotion']

    # Get number of entries in dictionary
    emotions_length = len(emotions)

    # Build output string
    count = 0
    output = "For the given statement, the system response is "
    for key, value in emotions.items():
        count += 1
        if key != 'dominant_emotion':
            if count == (emotions_length-1):
                output = output[:-2]   # take out extra comma
                fmt = ' and \'' + key + '\': ' + str(value) + '. '
            else:
                fmt = '\'' + key + '\': ' + str(value) + ', '
            output = output + fmt

    output = output + 'The dominant emotion is ' + dominant_emotion + '.'

    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
