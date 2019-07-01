from flask import render_template, jsonify, request
from flask_migrate import Migrate

from app import create_app, db
from app.models import User, user_many_shema, user_one_schema

app = create_app()

Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User
    )

@app.route('/')
def home():
    all_users = User.query.all()

    return render_template('index.html', users=all_users)

@app.route('/user/add', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.json['name']

        user = User(username=name)
        db.session.add(user)
        db.session.commit()

        result = user_one_schema.dump(user)

        return jsonify(result)


    return render_template('user/add.html')
