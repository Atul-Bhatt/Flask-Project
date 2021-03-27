# Flask Project

Create a .flaskenv file and put value of FLASK_APP and FLASK_ENV

Create a virtual environment:
python -m venv <name-of-virtual-environment>

Create requirements.txt file:
pip freeze > requirements.txt

Install all the dependencies in requirements.txt
pip install -r requirements.txt

Every ".py" file is called a module.

To use the .flaskenv file install python-dotenv
pip install python-dotenv

setting FLASK_APP in powershell
$env:FLASK_APP = "main"

Create application forlder
create **init**.py file
create templates folder for html templates
create static folder for static content like css, js, audio, video (anything that is not generated dynamically.)

move main file's content into **init**.py and import it into main.py

---

Running and Configuring the Development server

Create a config.py file in main folder
Create a routes.py file in application folder

---

Creating the Homepage

put the html files in the templates folder
import the render_template module from flask

{% Jinja code block %}
Example
{% include "include/footer.html" %}

---

Creating navigation links and route patterns

-> using the url_for function to resolve links
-> using the route decorator to bind functions to one or more url patterns
-> Jinja delimeters

Jinja:
{% ... %} Statements
{{ ... }} Expressions
{# ... #} Comments

---

Working with templates

-> The Jinja template inheritance logic
-> Creating the base template
-> Using template inheritance to create child templates
-> Passing data to the view using props
-> Accessing data via the request and response object

if you want to render a template twice you can use this expression:
{{ self.content() }}

---

Passing data to the view

Passing data from the source to the view
Highlighting the active menu item
Using the for directive
Building the course table with JSON data

---

Request and Response objects

URL variables
HTTP methods (GET, POST)
The global objects: Request and Response
Requests and Responses are all JSON API format

Accessing Query String (GET)
request.args.get(<field_name>)
or
request.args[<field_name>]

Accessing Form Data (POST)
request.form.get(<field_name>)
or
request.form[<field_name>]

---

URL variables

Routing Patterns
Creating a URL variable
Setting default data to a URL variable
Passing a URL variable to a template

@app.route("/courses/<term>")

---

Working with the get method

Creating the enrollment form using the GET method
Creating the enrollment template
Creating the enrollment route (URL pattern)
Accessing form data via the GET method

---

Working with the post method

You have to explicitly include the post method to the list in decorator
@app.route("/<path>", method=["GET", "POST"])

We didn't have to mention this for GET but since we have provided a list, we need to include GET too.

---

Sending a JSON Response

The Response Object
Creating two APIs to send JSON response

Response Object
Class flask.Response(
response=None, # most commonly used
status=None,
headers=None,
mimetype=None, # most commonly used
content_type=None, # most commonly used
direct_passthrough=False
)

---

Working with databases

Installing the MongoDB database system
Installing the MongoEngine extension for Flask
Setting up the database
Connecting to the database
Creating documents and data
Creating the data model

In config file:
MONGODB_SETTINGS = {'db' : '<database_name>'}

pip install flask-mongoengine

---

Connecting to the database

Connecting to the MongoDB via the MongoDB object
Hooking up a use collection using a simple user model Class
Inserting sample user document(data) to the collection
Displaying the collection to the view

A collection name is a table.

---

Set path of mongoDB to use shell
In CMD:
set path=C:\Program Files\MongoDB\Server\4.4\bin
mongo --version

import json data into a collection:
mongoimport --db UTA_Enrollment --collection user --file users.json
If the file has json array then use --jsonArray flag:
mongoimport --jsonArray --db UTA_Enrollment --collection user --file users.json

---