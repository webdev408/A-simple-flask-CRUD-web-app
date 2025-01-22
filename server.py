from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.app_context().push()
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image = db.Column(db.String(120), unique=True, nullable=False)

  def __repr__(self):
    return '<User %r>' % self.username
  
@app.route('/')
def index():
  users = User.query.all()
  return render_template('index.html', users=users)

@app.route('/add', methods=['Get', 'POST'])
def add():
  if request.method == 'GET':
    return render_template('form.html')
  name = request.form['name']
  email = request.form['email']
  image = request.form['image']
  user = User(name=name, email=email, image=image)
  db.session.add(user)
  db.session.commit()
  return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['Get', 'POST'])
def edit(id):
  user = User.query.get(id)
  if request.method == 'GET':
    return render_template('edit.html', user=user)
  user.name = request.form['name']
  user.email = request.form['email']
  user.image = request.form['image']
  db.session.commit()
  return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
  user = User.query.get(id)
  db.session.delete(user)
  db.session.commit()
  return redirect(url_for('index'))


if __name__ == '__main__':
  db.create_all()
  app.run(debug=True)
