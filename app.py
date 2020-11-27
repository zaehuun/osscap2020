from flask import Flask, render_template, redirect, url_for
import posetet as PT
import threading as TH
app = Flask(__name__, static_url_path='/static') 

direct = None
@app.route("/") 
@app.route('/index')
def home():
    return render_template('tm.html')

@app.route("/center") 
def center():
    global direct
    direct = "right"
    return render_template('tm.html')

@app.route("/right") 
def right():
    global direct
    direct = "right"
    return render_template('tm.html')

@app.route("/left") 
def left():
    global direct
    direct = "left"
    return render_template('tm.html')

def LED_init():
    global direct
    thread1=TH.Thread(target=PT.main1, args=(direct,))
    thread1.setDaemon(True)
    thread1.start()
    return
if __name__ == "__main__":
    LED_init()
    app.run()
