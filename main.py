from flask import Flask, render_template




app = Flask(__name__)

@app.route('/')
def home():
    example_embed='This string is from python'
    return render_template('index.html', embed=example_embed) 


if __name__ == "__main__":
    app.run(debug=True)


