from flask import request
from flask import Flask 
from flask import render_template
from weather import main as get_weather

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    data = None
    if request.method == 'POST':
        city = request.form['city']
        data = get_weather(city)
        print(data)
    return render_template('w3t1.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)