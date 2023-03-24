from flask  import Flask, render_template, request
import remove

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        text = request.form["text"]
        for input in request.form:
            if input == "puntuaction-marks":
                text = remove.remove_punctuation_marks(text)
            elif input == "adverbs":
                text = remove.remove_adverbs(text)
            elif input == "adjectives":
                text = remove.remove_adjetives(text)
            elif input == "verbs":
                text = remove.remove_verbs(text)
                
    return render_template("index.html")
