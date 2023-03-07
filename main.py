from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    gender = None
    preferences = None
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        preferences = request.form.getlist('preferences')
        pref_text = ''
        for preference in preferences:
          pref_text = ' ' + preference
        with open('data.txt', 'a') as file:
          file.write(name + ' ' + gender + ' ' + pref_text + ' \n')
    return render_template('index.html', name=name, gender=gender, preferences=preferences)


app.run(host='0.0.0.0', port=81)
