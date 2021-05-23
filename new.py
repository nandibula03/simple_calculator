from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def cal():
    return render_template('form.html')


@app.route('/result', methods=['POST'])
def result():
    number1 = request.form.get("number1", type=int)
    number2 = request.form.get("number2", type=int)
    operation = request.form.get("operation")
    if(operation == 'Addition'):
        result = number1 + number2
    elif(operation == 'Subtraction'):
        result = number1 - number2
    elif(operation == 'Multiplication'):
        result = number1 * number2
    elif(operation == 'Division'):
        result = number1 / number2
    else:
        result = 'INVALID CHOICE'
    entry = result
    return render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
