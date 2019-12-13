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
    return render_template('tea_new.html', tea = {})


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
        'image':request.form.get('image')
    }

    teas.insert_one(tea).inserted_id
    return redirect(url_for('teas_index'))
















if __name__ == '__main__':
    app.run(debug=True)
