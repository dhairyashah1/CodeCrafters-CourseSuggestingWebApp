from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/index.html")
@app.route("/")
def home():
    return render_template('index1.html')


@app.route("/about.html")
def about():
    return render_template('about1.html')

@app.route("/contact",methods=['GET','POST'])
@app.route("/contact.html", methods = ['GET', 'POST'])
def contact():
    return render_template('contact1.html')



@app.route("/courses.html")
def courses():
    return render_template('courses.html')


@app.route("/course-details.html")
def details():
    return render_template('course-details.html')


@app.route("/events.html")
def events():
    return render_template('events.html')

@app.route("/pricing.html")
def pricing():
    return render_template('pricing.html')


@app.route("/trainers.html")
def trainers():
    return render_template('trainers.html')

app.run(debug=True)


