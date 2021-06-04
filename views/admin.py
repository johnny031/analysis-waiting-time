from flask import Blueprint, render_template
from flask_login import login_required

admin = Blueprint("admin", __name__)

@admin.route("/admin", methods=['GET', 'POST'])
@login_required
def admin_user(): 
    return render_template("admin.html")