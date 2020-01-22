from flask import Flask, render_template, request
from birthday_range_coincidence import funct_birthday

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def birthday_calculate():
    if request.method == 'POST':
        form_data = request.form
        drange = int(form_data['drange']) if form_data['drange'] else 7
        pcnt = int(form_data['pcnt']) if form_data['pcnt'] else 8
        ydays = int(form_data['ydays']) if form_data['ydays'] else 365
        answer = funct_birthday(drange, pcnt, ydays)
        result = {
            'drange': drange,
            'pcnt': pcnt,
            'ydays': ydays,
            'answer': answer
        }
        return render_template("result.html", result=result)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
