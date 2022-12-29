# ====== FLASK STANDART LIBRARY =============
from flask import Blueprint, session, render_template, make_response, redirect, url_for, request
from flask_login import login_required, current_user
# =============== MODEL DATABASE ===============
from .models import Users
from . import db
# ============= MONGO ACCESS =========
from .mongo_meths import *

main = Blueprint('main', __name__)


# ======= GENERIC VIEW ==============
@main.route('/')
def home_page():
    return render_template("homepage.html")


# ======== VIEW FOR LOGGED USERS ===========
@main.route('/profile')
@login_required
def profile():
    return render_template("profile.html", name=current_user.name)


@main.route('/dashboard', methods=["POST", "GET"])
@login_required
def dashboard():
    # == GATHER THE INFO OF THE CURRENT USER ==
    email = current_user.email
    user = Users.query.filter_by(email=email).first()
    
    # == POST VIEW FROM THE DASHBOARD ==
    if request.method == "POST":
        title = request.form.get('title')
        description = request.form.get('description')
        _id = session.get(f"{email}_doc")["_id"]

        insert_new_note(_id, kwargs={"title": title, "description": description})

        return redirect(url_for('main.dashboard'))

    try:
        # == CHECK IF THE USER HAS A "DOC" IN MONGO ==
        if user.id_doc:

            # == ADD THE ID REFERENCE AND THE MAIL OF THE ==
            # == USER IN SESSION COCKIE FOR RETRIEVING AND MODIFYING ==

            notes = retrieve_notes(user.id_doc)
            notes['_id'] = user.id_doc

            session[f"{email}_doc"] = notes            

            return render_template("dashboard.html", notes= notes["notes"])

        # == CREATE A NEW DOC FOR THE CURRENT USER ==
        # == ADD THE RESPECTIVES KEY (DOC) TO THE COCKIE ==

        _id = insert_new_doc(email=email)
        user.id_doc = str(_id)

        notes = retrieve_notes(user.id_doc)
        notes['_id'] = user.id_doc

        session[f"{email}_doc"] = notes

        db.session.commit()
    
        return render_template("dashboard.html", notes= notes["notes"])

    except Exception as e:
        print(f"===== error in {__file__} - {e} ======")
    # == GENERIC VIEW FOR DASHBOARD ==
    return render_template("dashboard.html")


@main.route("/modify_note/<string:id_note>", methods=["GET", "POST"])
@login_required
def modify_note(id_note):

    # == RETRIVE THE CURRENT NOTE ON MODIFICATION ==
    email = current_user.email
    notes = session.get(f"{email}_doc")
    _id = notes.pop("_id")
    current_note = [note for note in notes["notes"] if note["id_note"] == id_note]
    modify = True

    if request.form.get("_method") == "PUT":
        index = next((i for i, d in enumerate(notes["notes"]) if d.get('id_note') == id_note), None)
        title = request.form.get('title')
        description = request.form.get('description')

        current_note[0]["description"] = description
        current_note[0]["title"] = title

        notes["notes"][index]["title"] = title
        notes["notes"][index]["description"] = description

        modify_doc(_id, notes)

        return redirect(url_for("main.dashboard"))

    return render_template("note_form.html", note= (current_note, modify)) 


@main.route("/del/<string:id_note>", methods=["GET", "POST"])
@login_required
def del_note(id_note):

    # == RETRIVE THE CURRENT NOTE ON MODIFICATION ==
    email = current_user.email
    notes = session.get(f"{email}_doc")
    _id = notes.pop("_id")
    current_note = [note for note in notes["notes"] if note["id_note"] == id_note]
    modify = False

    print(_id)

    # == MAKE DE DELETION OF A NOTE ==
    if request.form.get("_method") == "DELETE":

        index = next((i for i, d in enumerate(notes["notes"]) if d.get('id_note') == id_note), None)
        notes["notes"].pop(index)

        modify_doc(_id, notes)
        
        return redirect(url_for("main.dashboard"))

    return render_template("note_form.html", note=(current_note, modify))
