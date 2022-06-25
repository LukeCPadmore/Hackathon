import cohere
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate_title', methods=["POST"])
def generate_titles():
    youtube_tags = request.form.get("youtube_tags_text_area")
    print(youtube_tags)
    #prediction = callCohereAPI("Hello",1234)
    return render_template("generate_title.html")

@app.route('/generate_again')
def generate_again():
    if prediction!=None:
        return render_template("generate_title.html")
    else:
        return render_template("index.html")

def callCohereAPI(tags, APIkey):
    co = cohere.Client('{apiKey}')
    prediction = co.generate(
        model='large',
        prompt=tags,
        max_tokens=50,
        temperature=0.75,
        k=0,
        p=0.75,
        frequency_penalty=0,
        presence_penalty=0,
        stop_sequences=[],
        return_likelihoods='NONE')
    return prediction

prediction = None
if __name__ == '__main__':
    app.run()