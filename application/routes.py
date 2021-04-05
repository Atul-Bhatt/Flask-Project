from application import app, db
from flask import render_template, request, Response, json, redirect, flash, url_for, session
from application.models import User, Course, Enrollment
from application.forms import LoginForm, RegisterForm

# courseData = [{"courseID": "1111", "title": "PHP 111", "description": "Intro to PHP", "credits": "3", "term": "Fall, Spring"},
#               {"courseID": "2222", "title": "Java 1",
#                   "description": "Intro to Java Programming", "credits": "4", "term": "Spring"},
#               {"courseID": "3333", "title": "Adv PHP 201",
#                   "description": "Advanced PHP Programming", "credits": "3", "term": "Fall"},
#               {"courseID": "4444", "title": "Angular 1",
#                "description": "Intro to Angular", "credits": "3", "term": "Fall, Spring"},
#               {"courseID": "5555", "title": "Java 2", "description": "Advanced Java Programming", "credits": "4", "term": "Fall"}]

# route for the root directry
# these are called decorators
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", index=True)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash(f"{user.first_name}, You are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.", "danger")
    return render_template("login.html", title='Login', form=form, login=True)


@app.route("/logout")
def logout():
    session['user_id'] = False
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if session.get('username'):
        return redirect(url_for('index'))

    form = RegisterForm()
    if form.validate_on_submit():
        user_id = User.objects.count()
        user_id += 1

        email = form.email.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data

        user = User(user_id=user_id, email=email,
                    first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()
        flash('You are successfully registered!', 'success')
        return redirect(url_for('index'))
    return render_template("register.html", title='Register', form=form, register=True)


@app.route("/courses")
@app.route("/courses/<term>")
def courses(term=None):
    if term == None:
        term = "Spring 2019"
    # courses = Course.objects.all()
    # TODO: Sort courses by CourseID rather than ID
    courses = Course.objects.order_by("-courseID")
    return render_template("courses.html", courseData=courses, courses=True, term=term)


@app.route("/enrollment", methods=["GET", "POST"])
def enrollment():
    if not session.get('username'):
        return redirect(url_for('login'))

    courseID = request.form.get('courseID')
    courseTitle = request.form.get('title')
    user_id = session.get('user_id')

    if courseID:
        if Enrollment.objects(user_id=user_id, courseID=courseID):
            flash(
                f"Oops! You are already registered in this course {courseTitle}!", "danger")
            return redirect(url_for("courses"))
        else:
            Enrollment(user_id=user_id, courseID=courseID).save()
            flash(f"You are enrolled in {courseTitle}!", "success")

    classes = list(User.objects.aggregate(*[
        {
            '$lookup': {
                'from': 'enrollment',
                'localField': 'id',
                'foreignField': 'user_id',
                'as': 'r1'
            }
        }, {
            '$unwind': {
                'path': '$r1',
                'includeArrayIndex': 'r1_id',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$lookup': {
                'from': 'course',
                'localField': 'r1.courseID',
                'foreignField': 'courseID',
                'as': 'r2'
            }
        }, {
            '$unwind': {
                'path': '$r2',
                'preserveNullAndEmptyArrays': False
            }
        }, {
            '$match': {
                'id': user_id
            }
        }, {
            '$sort': {
                'courseID': 1
            }
        }
    ]))

    return render_template("enrollment.html", enrollment=True, title="Enrollment",
                           classes=classes)


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx == None):
        jData = Course.objects.all()
    else:
        # jData = courseData[int(idx)]
        pass
    return Response(json.dumps(jData), mimetype="application/json")


@app.route("/user")
def user():
    # User(user_id=1, first_name="Atul", last_name="Bhatt", email="atul.bhatt@gmail.com",
    #      password="pass@123").save()
    # User(user_id=2, first_name="Jim", last_name="Shrute", email="jim.shrute@gmail.com",
    #      password="pass@345").save()
    users = User.objects.all()
    return render_template("user.html", users=users)
