# Flask Project

- Create a .flaskenv file and put value of FLASK_APP and FLASK_ENV

- Create a virtual environment:

```console
python -m venv \<name-of-virtual-environment>
```

- Create requirements.txt file:

```console
pip freeze > requirements.txt
```

- Install all the dependencies in requirements.txt

```console
pip install -r requirements.txt
```

- Every ".py" file is called a module.

- To use the .flaskenv file install python-dotenv

```console
pip install python-dotenv
```

- Setting FLASK_APP in powershell

```console
$env:FLASK_APP = "main"
```

## Folder Structure

- Create application folder
- Create init.py file
- Create templates folder for html templates
- Create static folder for static content like css, js, audio, video (anything that is not generated dynamically.)
- move main file's content into init.py and import it into main.py

---

### Running and Configuring the Development server

- Create a config.py file in main folder
- Create a routes.py file in application folder

---

### Creating the Homepage

- put the html files in the templates folder
- import the render_template module from flask

```jinja
{% Jinja code block %}
Example
{% include "include/footer.html" %}
```

---

### Creating navigation links and route patterns

- using the url_for function to resolve links
- using the route decorator to bind functions to one or more url patterns
- Jinja delimeters

```jinja
{% ... %} Statements
{{ ... }} Expressions
{# ... #} Comments
```

---

### Working with templates

- The Jinja template inheritance logic
- Creating the base template
- Using template inheritance to create child templates
- Passing data to the view using props
- Accessing data via the request and response object

if you want to render a template twice you can use this expression:

```jinja
{{ self.content() }}
```

---

### Passing data to the view

- Passing data from the source to the view
- Highlighting the active menu item
- Using the for directive
- Building the course table with JSON data

---

### Request and Response objects

- URL variables
- HTTP methods (GET, POST)
- The global objects: Request and Response
- Requests and Responses are all JSON API format

Accessing Query String (GET)

```python
request.args.get(<field_name>)
```

or

```python
request.args[<field_name>]
```

Accessing Form Data (POST)

```python
request.form.get(<field_name>)
```

or

```python
request.form[<field_name>]
```

---

### URL variables

- Routing Patterns
- Creating a URL variable
- Setting default data to a URL variable
- Passing a URL variable to a template

```python
@app.route("/courses/<term>")
```

---

### Working with the get method

- Creating the enrollment form using the GET method
- Creating the enrollment template
- Creating the enrollment route (URL pattern)
- Accessing form data via the GET method

---

### Working with the post method

You have to explicitly include the post method to the list in decorator

```python
@app.route("/<path>", method=["GET", "POST"])
```

We didn't have to mention this for GET but since we have provided a list, we need to include GET too.

---

### Sending a JSON Response

- The Response Object
- Creating two APIs to send JSON response

```python
Response Object
Class flask.Response(
response=None, # most commonly used
status=None,
headers=None,
mimetype=None, # most commonly used
content_type=None, # most commonly used
direct_passthrough=False
)
```

---

### Working with databases

- Installing the MongoDB database system
- Installing the MongoEngine extension for Flask
- Setting up the database
- Connecting to the database
- Creating documents and data
- Creating the data model

In config file:

```python
MONGODB_SETTINGS = {'db' : '<database_name>'}
```

Install mongoengine:

```console
pip install flask-mongoengine
```

---

Connecting to the database

- Connecting to the MongoDB via the MongoDB object
- Hooking up a use collection using a simple user model Class
- Inserting sample user document(data) to the collection
- Displaying the collection to the view

A collection name is a table.

---

Set path of mongoDB to use shell
In CMD:

```console
set path=C:\Program Files\MongoDB\Server\4.4\bin
mongo --version
```

import json data into a collection:

```console
mongoimport --db UTA_Enrollment --collection user --file users.json
```

If the file has json array then use --jsonArray flag:

```console
mongoimport --jsonArray --db UTA_Enrollment --collection user --file users.json
```

---

### Creating the Data Models

- Creating the models module
- Creating the User model
- Creating the Course model
- Creating the Enrollment model

```python
class ModelName(db.Document):
    field1 = db.IntField()
    field2 = db.StringField()
```

---

### Working with Web Forms and Flask-Security

- Installing and configuring Flask-WTF and Flask-Security extensions
- Creating the login and registration pages
- Processing form data and updating the database
- Creating Courses and Enrollment pages
- Creating sessions and authentication

### Flask WTF extension

- Flask-WTF is an extension for WTForms library
- WTForms is a clean way to generate HTML form fields
- Maintain a seperation of code and presentation

```html
<form>
  {{ form.hidden_tag() }} {{ form.username }} {{ form.email }} {{ form.password
  }}
</form>
```

### Flask-Security Extension

- Provides common security and authentication features:
  - Session based authentication
  - Password hashing
  - Basic HTTP and token based authentication
  - User registration
  - Login tracking (Flask-Login)
- Supports data persistency for Flask-SQLAlchemy, Flask-MongoEngine, flask-peewee, and PonyORM

```console
pip install flask-wtf flask-security
```

Validate Form:

```python
form = LoginForm() # class that inherits from FlaskForm
if form.validate_on_submit():
  flash("You are successfully loged in!")
  return redirect("/index")
```

---

### Flashing Messages

- Flash messages from the source to the view

---

# Database

## Sort data in mongo

```python
courses = Course.objects.order_by("courseID")
# In ascending order
courses = Course.objects.order_by("+courseID")
# In descending order
courses = Course.objects.order_by("-courseID")
```

---

## MongoDB Aggregation Pipeline

- Exploring the MongoDB Aggregation framework using Compass interface
- Creating the aggregation pipeline to process data in three stages:
  - $lookup: Performs a left outer join
  - $match: Filters documents
  - $unwind: Deconstructs an array field

--

## Create sessions and authentication

- State management and user authentication using Flask-Session
- The session object stores information specific to a user
- Implementation on top of cookies and signs cookies cryptographically

## Flask-Login Extension (Not implemented here)

- Sessions and State management using Flask-Login extension
- Managing user logged in state using a user_loader() function
- Using a LoginManager class to manage login state
- Implementing the remember me feature
- Restricting access to protected pages using @login_required
- Logging out user using the logout_user() function

for more information go to this [link](https:flask-login.readthedocs.io/en/latest/)
