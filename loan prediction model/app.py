
from logging import debug
from flask import Flask, render_template, request
import utils
from utils import preprocessdata

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict/', methods=['GET', 'POST'])

def predict():
    if request.method == 'POST':
        income = request.form.get('income')
        age = request.form.get('age')
        experience = request.form.get('experience')
        married_single = request.form.get('married_single')
        house_ownership = request.form.get('house_ownership')
        car_ownership = request.form.get('car_ownership')
        profession = request.form.get('profession')
        city = request.form.get('city')
        state = request.form.get('state')
        current_job_yrs = request.form.get('current_job_yrs')
        current_house_yrs = request.form.get('current_house_yrs')

    prediction = utils.preprocessdata(income, age, experience, married_single, house_ownership, car_ownership, profession, city, state, current_job_yrs, current_house_yrs)

    return render_template('predict.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)