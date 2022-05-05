from flask import Flask
import random
app = Flask(__name__)

def bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"

    return wrapper
@app.route('/')
@bold
def hello_world():
    return 'Hi world'

@app.route('/user/<name>')
def greet(name):
    number = random.randint(0, 2)
    if number == 0:
        src = 'https://i.pinimg.com/736x/04/7a/b5/047ab539ec61c81dcf943451c08faa0e.jpg'
    elif number == 1:
        src = 'https://6.viki.io/image/a651013f56a44218a80883a9799c3f93.jpeg?s=900x600&e=t'
    else:
        src = 'https://i.pinimg.com/originals/f4/d3/b1/f4d3b12c3deca394e7d9b947272a1c51.jpg'
    return f'<h1 style="text-align: center">hi {name}!!</h1>' \
           f'<p>WELCOME</p>' \
           f'<img src={src} width=300px>'

if __name__ == "__main__":
    app.run()#debug=True