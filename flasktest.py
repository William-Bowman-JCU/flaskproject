from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=''):
    return f'Hello {name}'


@app.route('/f/<temp>')
def f_to_c(temp=''):
    return f'{convert_celsius_to_fahrenheit(float(temp))}'

@app.route('/c/<temp>')
def c_to_f(temp=''):
    return f'{convert_fahrenheit_to_celsius(float(temp))}'


def convert_celsius_to_fahrenheit(celsius):
    """Convert users chosen temperature from celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert users chosen temperature from fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)


if __name__ == '__main__':
    app.run()