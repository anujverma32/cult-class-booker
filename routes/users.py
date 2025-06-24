from flask import Blueprint, render_template, redirect, url_for, flash, request
from models import db, Users
from forms import UserForm

users_bp = Blueprint("users", __name__)


@users_bp.route("/create", methods=["GET", "POST"])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = Users(
            name=form.name.data,
            cult_token=form.cult_token.data,
            latitude=form.latitude.data,
            longitude=form.longitude.data,
        )
        db.session.add(user)
        db.session.commit()
        flash("User created successfully!", "success")
        return redirect(url_for("main.index"))
    return render_template("create_user.html", form=form)


@users_bp.route("/edit/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = Users.query.get_or_404(user_id)
    form = UserForm(obj=user)

    if form.validate_on_submit():
        user.name = form.name.data
        user.cult_token = form.cult_token.data
        user.latitude = form.latitude.data
        user.longitude = form.longitude.data
        db.session.commit()
        flash("User updated successfully!", "success")
        return redirect(url_for("main.index"))

    return render_template("edit_user.html", form=form, user=user)


@users_bp.route("/delete/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User and associated preferences deleted successfully!", "success")
    return redirect(url_for("main.index"))
