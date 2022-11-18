from flask import Flask, render_template, request
# from src.data import data




app = Flask(__name__)

@app.route('/')
def home():
    a = 3
    b = 4
    example_embed='This string is from python and the result is: {}'.format(a+b)

    example_result = 'Python reads the table: '

    return render_template('index.html', embed=example_embed, result = example_result) 


if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0") # , host="0.0.0.0"

    print('END')


