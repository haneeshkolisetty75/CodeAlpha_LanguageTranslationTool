from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    translated = ""

    if request.method == "POST":
        text = request.form.get("text")
        source = request.form.get("source")
        target = request.form.get("target")

        if text and target:
            translated = GoogleTranslator(source=source, target=target).translate(text)

    return render_template("index.html", translated=translated)


if __name__ == "__main__":
    app.run(debug=True)