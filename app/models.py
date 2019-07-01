from app import db, ma

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, username):
        self.username = username

    def __repr(self):
        return f"<% Username: {self.username} %>"

class UserSchema(ma.Schema):
    class Meta:
        fields = ['id', 'username']

user_one_schema = UserSchema()
user_many_shema = UserSchema(many=True)