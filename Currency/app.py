from flask import Flask, render_template, request, redirect, session, url_for
from forex_python.converter import CurrencyCodes, CurrencyRates

app = Flask(__name__)
app.config["secret key"] = "yeah"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

responses_key = "responses"

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('Index.html')

C = CurrencyRates()

@app.route("/conversion", methods = ['GET', 'POST'])
def conversion():
    if request.method == 'POST':
        C1 = request.form.get('C1', None)
        C2_to = request.form.get('C2_to', None)
        amt = request.form.get('amt', None)
        rate = C.convert(C1, C2_to, int(amt))
        print(C1, C2_to, amt, rate)
        details = {'C1': C1, 'C2_to': C2_to, 'amt': amt, 'rate': rate}
    return render_template("Index2.html", details=details)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(debug=True)
