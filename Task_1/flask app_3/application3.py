from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('layout.html')

@app.route('/education')
def education():
    return render_template('layout.html')

@app.route('/experience')
def experience():
    return render_template('layout.html')

@app.route('/projects')
def projects():
    return render_template('layout.html')

@app.route('/skills')
def skills():
    return render_template('layout.html')

@app.route('/contact')
def contact():
    return render_template('layout.html')







if(__name__=='__main__'):
   app.run(debug=True)
