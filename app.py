from flask import Flask, render_template, request
from utils.vibe_model import predict_vibe

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        file = request.files["image"]
        if file:
            vibe, suggestions, caption, hashtags = predict_vibe(file)
            result = {
                "vibe": vibe,
                "suggestions": suggestions,
                "caption": caption,
                "hashtags": hashtags
            }
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
