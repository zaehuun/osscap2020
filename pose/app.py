from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, static_url_path='/static') 

@app.route("/") 
@app.route('/index')
def home(): 
    return render_template('tm.html')

if __name__ == "__main__":
    app.run()