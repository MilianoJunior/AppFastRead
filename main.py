from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\milianooliveira\\test.db'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'  # Use o caminho para o seu banco de dados aqui
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

with app.app_context():  # Cria um contexto de aplicação
    # Cria o banco de dados e a tabela
    db.create_all()

    # Adiciona alguns usuários para teste
    user1 = User(name='Alice')
    user2 = User(name='Bob')

    db.session.add(user1)
    db.session.add(user2)

    db.session.commit()

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'name': u.name} for u in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'user not found'}), 404
    return jsonify({'id': user.id, 'name': user.name})

if __name__ == '__main__':
    app.run(debug=True)
