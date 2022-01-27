from flask_app import app
from flask import render_template,request,redirect,flash, session
from flask_app.models.usersmodel import User


@app.route("/")
def home():
    return redirect("/users")


@app.route("/users")
def index():
    all_users = User.get_all()
    return render_template("users.html",all_users=all_users)



@app.route("/users/new")
def new_form():
    return render_template("new_user.html")

@app.route("/adduser", methods=["POST"])
def add_user():
    User.add_user(request.form)
    return redirect("/users")



@app.route("/users/<int:id>")
def show_user(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    return render_template("show_one.html", user=user)



@app.route("/edit/<int:id>")
def edit_page(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    return render_template("edit.html", user=user)

@app.route("/edituser/<int:id>", methods=["POST"])
def edit_user(id):
    data = {
        "id":id,
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    User.update(data)
    return redirect("/users")



@app.route("/deleteuser/<int:id>")
def del_user(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect("/users")