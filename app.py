## Ramim Tarafdar- Digital Factory Tech Assessment ##
## Restaurant Reservations ##


from flask import Flask, redirect, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Reserve(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    time = db.Column(db.String(300), nullable=False)
    date = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return '<Reservation %r' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        res_name = request.form['name']
        res_quantity = request.form['quantity']
        res_time = request.form['time']
        res_date = request.form['date']
        new_res = Reserve(name = res_name, quantity = res_quantity, time = res_time, date = res_date)

        try:
            db.session.add(new_res)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your reservation'

    else:
        reservations = Reserve.query.order_by(Reserve.date).all()
        return render_template('index.html', reservations=reservations)


@app.route('/delete/<int:id>')
def delete(id):
    res_delete = Reserve.query.get_or_404(id)

    try:
        db.session.delete(res_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that reservation'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    res_update = Reserve.query.get_or_404(id)

    if request.method == 'POST':
        res_update.name = request.form['name']
        res_update.quantity = request.form['quantity']
        res_update.time = request.form['time']
        res_update.date = request.form['date']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your reservation'

    else:
        return render_template('update.html', res_update=res_update)

if __name__ == "__main__": 
    app.run(debug=True)