from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def ninjas():
    return render_template("ninjas.html")

@app.route('/Dojo/new')
def new():
    return render_template("new.html")

#@app.route('/users', methods=['POST'])
#def create_user():
#    print "Got Post Info"
#    return redirect('/ninja')
#def button1():
#    if request.method == 'POST':
##        return render_template('ninjas.html')

app.run(debug=True)