from application import app, db
from flask import render_template, request, Response, json, redirect, flash
from application.models import User, Course, Enrollment
from application.forms import LoginForm, RegisterForm

courseData = [{"courseID": "1111", "title": "PHP 111", "description": "Intro to PHP", "credits": "3", "term": "Fall, Spring"},
              {"courseID": "2222", "title": "Java 1",
                  "description": "Intro to Java Programming", "credits": "4", "term": "Spring"},
              {"courseID": "3333", "title": "Adv PHP 201",
                  "description": "Advanced PHP Programming", "credits": "3", "term": "Fall"},
              {"courseID": "4444", "title": "Angular 1",
               "description": "Intro to Angular", "credits": "3", "term": "Fall, Spring"},
              {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": "4", "term": "Fall"}]

# route for the root directry
# these are called decorators
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.form.get("email") == "test@uta.com":
            flash("You are successfully logged in!", "success")
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("login.html", title='Login', form=form, login=True)


@app.route("/register")
def register():
    form = RegisterForm()
    return render_template("register.html", title='Register', form=form, register=True)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term="Spring 2019"):
    return render_template("courses.html", courseData=courseData, courses=True, term=term)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    return render_template("enrollment.html",
                           data={"courseId": request.form.get("courseID"),
                                 "title": request.form.get("title"), "term": request.form.get("term")})


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jData = courseData
    else:
        jData = courseData[int(idx)]
    return Response(json.dumps(jData), mimetype="application/json")


@app.route("/user")
def user():
    # User(user_id=1, first_name="Atul", last_name="Bhatt", email="atul.bhatt@gmail.com",
    #      password="pass@123").save()
    # User(user_id=2, first_name="Jim", last_name="Shrute", email="jim.shrute@gmail.com",
    #      password="pass@345").save()
    users = User.objects.all()
    return render_template("user.html", users=users)
