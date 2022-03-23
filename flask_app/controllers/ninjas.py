from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def new_ninja_form():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', dojos=dojos)
    
@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.create(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}/show")