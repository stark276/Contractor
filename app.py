from bson.objectid import ObjectId
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

client = MongoClient()
db = client.Teas_tore
teas = db.teas




app = Flask(__name__)

# teas = [
#     { 'title': 'mango', 'description': 'bellisimo' },
#     { 'title': '80\'s Music', 'description': 'Don\'t stop believing!' }
# ]

@app.route('/')
def teas_index():
    """Show all lists."""
    return render_template('tea_index.html', teas=teas.find())


@app.route('/teas/new')
def teas_new():
    """Create a new tea list."""
    return render_template('tea_new.html',  tea ={}, title ="create new")


@app.route('/teas/<tea_id>')
def teas_show(tea_id):
    ''' shows the info for one individual plant '''
    tea = teas.find_one({'_id': ObjectId(tea_id)})
    return render_template('teas_show.html', tea=tea)



@app.route('/teas', methods=['POST'])
def teas_submit():

    tea = {
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        "price": request.form.get("price"),
        "domain": request.form.get("domain")
    }

    teas.insert_one(tea).inserted_id
    return redirect(url_for('teas_index'))

@app.route("/teas/<tea_id>/edit")
def teas_edit(tea_id):
	tea = teas.find_one({"_id" : ObjectId(tea_id)})
	return render_template("teas_edit.html", tea = tea, title = "Edit Your Product")


@app.route("/teas/<tea_id>", methods = ['POST'])
def teas_update(tea_id):
	updated_tea = {
		"tea_name": request.form.get("tea_name"),
		"description": request.form.get("description"),
		"price": request.form.get("price"),
        "domain": request.form.get("domain")

	}

	teas.update_one( {"_id" : ObjectId(tea_id)}, {"$set" : updated_tea})
	return redirect(url_for("teas_show", tea_id = tea_id))



















if __name__ == '__main__':
    app.run(debug=True)
