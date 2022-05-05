from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def receive_data():
    name = request.form['nameinp']
    password = request.form['password']
    return f"<h1>Name: {name}, password: {password}</h1>"
    # return render_template("login.html", name=name, password=password)
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    #     # the code below is executed if the request method
    #     # was GET or the credentials were invalid
    # return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)