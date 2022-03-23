from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.dojo import Dojo

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('all_dojos.html', dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def dojos_create():
    print(request.form)
    Dojo.create(request.form)
    return redirect ('/dojos')

@app.route('/dojos/<int:id>/show')
def show_ninjas_in_dojo(id):
    data = {
        'id' : id
    }
    dojo = Dojo.dojo_with_ninjas(data)
    return render_template('select_dojo.html', dojo=dojo)

