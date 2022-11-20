from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

with app.app_context():
    db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):

        # return Task with id, everytime a new element is added
        return '<Task %r>' % self.id



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/old', methods = ['POST', 'GET']) # methods that this route can accept
def home():
    a = 3
    b = 4
    example_embed='This string is from python and the result is: {}'.format(a+b)

    example_result = 'Python reads the table: '

    return render_template('index_old.html', embed=example_embed, result = example_result) 


@app.route('/spreadsheet_1', methods = ['POST', 'GET']) # methods that this route can accept
def spreadsheet_1():
    return render_template('spreadsheet_1.html') 



######## HOME ############
@app.route('/fetch')
def test_page():
    example_embed='Sending data... [this is text from python]'
    # look inside `templates` and serve `fetch.html`
    return render_template('fetch.html', embed=example_embed)


######## Example fetch ############
@app.route('/test', methods=['GET', 'POST'])
def testfn():
    # POST request
    if request.method == 'POST':
        print(request.get_json())  # parse as JSON
        return 'OK', 200
    # GET request
    else:
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers


######## Data fetch ############
@app.route('/getdata/<transaction_id>/<second_arg>', methods=['GET','POST'])
def datafind(transaction_id,second_arg):
    # POST request
    if request.method == 'POST':
        print('Incoming..')
        print(request.get_text())  # parse as text
        return 'OK', 200
    # GET request
    else:
        message = 't_in = %s ; result: %s ; opt_arg: %s'%(transaction_id, data[int(transaction_id)], second_arg)
        return message #jsonify(message)  # serialize and use JSON headers




if __name__ == "__main__":
    data = list(range(1,300,3))
    #print (data)
    app.run(debug=True)


# https://www.jitsejan.com/python-and-javascript-in-flask
# https://www.valentinog.com/blog/html-table/

# Communication
# https://stackoverflow.com/questions/59975596/how-to-connect-javascript-to-python-script-with-flask
# https://towardsdatascience.com/talking-to-python-from-javascript-flask-and-the-fetch-api-e0ef3573c451

# https://www.youtube.com/watch?v=p5eCYKiZN-4