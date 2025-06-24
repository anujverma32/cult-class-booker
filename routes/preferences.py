from flask import Blueprint, render_template, redirect, url_for, flash
from models import db, Preferences, Users
from forms import PreferenceForm
from utils.enums import Class_timing, Class_type

prefs_bp = Blueprint("prefs", __name__)


@prefs_bp.route("/create", methods=["GET", "POST"])
def create_preference():
    form = PreferenceForm()
    form.user_id.choices = [(u.id, u.name) for u in Users.query.all()]

    if form.validate_on_submit():
        pref = Preferences(
            user_id=form.user_id.data,
            center=form.center.data,
            timing=Class_timing[form.timing.data],
            class_type=Class_type[form.class_type.data],
            days_of_week=",".join([d for d in form.days_of_week.data if d]),
        )
        db.session.add(pref)
        db.session.commit()
        flash("Preference created successfully!", "success")
        return redirect(url_for("main.index"))

    return render_template("create_preference.html", form=form)


@prefs_bp.route("/delete/<int:pref_id>", methods=["POST"])
def delete_preference(pref_id):
    pref = Preferences.query.get_or_404(pref_id)
    db.session.delete(pref)
    db.session.commit()
    flash("Preference deleted.", "success")
    return redirect(url_for("main.index"))
