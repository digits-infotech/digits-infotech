import json
from flask import Flask, request, render_template, url_for, jsonify, flash, redirect

app = Flask(__name__, template_folder='templates', static_folder='static')

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        msg = f'{name}, your message has been received.'
        msg1 = 'Thank you for contacting us'
        resp = {'name': name, 'email': email, 'subject': subject, 'message': message, 'msg': msg, 'msg1': msg1}
        return render_template('result.html', resp=resp)
    return render_template('index.html', title="DigitsInfotech")


@app.route('/news', methods=['GET', 'POST'])
def news_letter():
    if request.method == 'POST':
        email = request.form['email']
        msg = 'You have successfully registered for our weekly newsletter'
        display = {'email': email, 'msg': msg}
        return render_template('newsletter.html', display=display)
    return render_template('index.html', title='DigitsInfotech')


@app.route('/form', methods=['GET', 'POST'])
def form_page():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        # age = int(request.form['age'])
        subject = request.form['subject']
        message = request.form['message']
        msg = f'{name}, your message has been received. '
        msg1 = 'Thank you for contacting us'
        # if age <= 20:
        #     name = request.form['name']
        #     msg = f'{name} you are not qualified'
        #     alert = {'name': name, 'msg': msg}
        #     return render_template("result.html", alert=alert)

        resp = {'name': name, 'email': email, 'subject': subject, 'message': message, 'msg': msg, 'msg1': msg1}
        return render_template('result.html', resp=resp)
    return render_template('forms.html', title="Form Page")

@app.route('/flash', methods=['GET', 'POST'])
def flash_func():
    if request.method == 'POST':
        name = request.form['name']
        if name == 'Felix':
            flash('Login Successful')
            return render_template('success.html')
        else:
            msg = 'Login Not Successful'
            return render_template('flash.html', msg=msg)
    return render_template('flash.html', title='Flash Message')


@app.route('/calculate', methods=['GET', 'POST'])
def calc_func():
    if request.method == 'POST':
        name = request.form['name']
        regular_hours = int(request.form['regular_hours'])
        over_time = int(request.form['over_time'])
        hourly_pay = 100.0
        over_hourly_pay = 50.0
        regular_pay = hourly_pay * regular_hours
        overtime_pay = over_time * over_hourly_pay
        initial = float(regular_pay * overtime_pay)
        gross_pay = f'{name} Gross Pay: {initial}'
        return render_template('cal.html', gross_pay=gross_pay)
    return render_template('cal.html', title='Calculation')

@app.route('/food', methods=['GET', 'POST'])
def food_func():
    items = {'Yam': {'qty': 20, 'price': 1200},
             'Beans': {'qty': 30, 'price': 1500},
             'Rice': {'qty': 40, 'price': 1800},
             'Semo': {'qty': 35, 'price': 1100},
             'Gari': {'qty': 45, 'price': 1000},
             'Yam Flour': {'qty': 30, 'price': 2000},
             'Millet': {'qty': 50, 'price': 1400},
             'Sesame': {'qty': 10, 'price': 1700},
             'Wheat': {'qty': 15, 'price': 1300},
             }
    if request.method == 'POST':
        food = request.form['food']
        qty = int(request.form['qty'])
        if qty <= items[food]['qty']:
            cost = float(qty * items[food]['price'])
            per_bag = items[food]['price']
            # message = f'The price of {qty} bags of {food} is: {cost}'
            return render_template('table.html', food=food, qty=qty, per_bag=per_bag, cost=cost)
        else:
            msg = f'Insufficient quantity! We do not have as much as {qty} bags of {food} in stock.'
            echo = f"We only have {items[food]['qty']} left"
            return render_template('food.html', msg=msg, echo=echo)
    return render_template('food.html', title='Market')









if __name__ == '__main__':
    app.run(debug=True)

