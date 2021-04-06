
from flask import Flask,render_template, redirect, url_for,request, flash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ANKILOVESCHOCOLATE07'

formpref=''


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/visualization')
def visualization():
    return render_template('visualize.html')
if __name__ == "__main__":
    app.run(debug=True)

