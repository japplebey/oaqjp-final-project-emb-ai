from flask import Flask, render_template, request 
from EmotionDetection import emotion_detector

#Initiate the flask app : Emotion Detector
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def get_emotions():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to Emotion Detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Format output
    output = format_output(response)    
    return output


@app.route("/")
def render_index_page():
    return render_template('index.html')


def format_output(emotions):
    dominant_emotion = emotions['dominant_emotion']

    # Get number of entries in dictionary
    emotions_length = len(emotions);
 
    # Build output
    count = 0
    output = "For the given statement, the system response is "
    for key, value in emotions.items():
        ++count
        fmt = ""
        if (key != 'dominant_emotion'):
            if (count == (emotions_length-1)):
                fmt = 'and \'' + key + '\': ' + str(value) + '. '
            elif (count == emotions_length):
                fmt = 'The dominant emotion is ' + dominant_emotion + '.'
            else:                
                a = '\'' + key + '\': ' + str(value) + ', '
        output = output + fmt

    print(output)        
    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

