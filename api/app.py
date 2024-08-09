from flask import Flask, request, jsonify
from models import db, User, Leaderboard
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@db:5432/tictactoe'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = User(username=data['username'], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Invalid credentials!"}), 401

@app.route('/leaderboard', methods=['GET'])
def leaderboard():
    leaderboard_data = Leaderboard.query.order_by(Leaderboard.wins.desc()).all()
    return jsonify([{"username": entry.user.username, "wins": entry.wins} for entry in leaderboard_data])

@app.route('/update_leaderboard', methods=['POST'])
def update_leaderboard():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user:
        leaderboard_entry = Leaderboard.query.filter_by(user_id=user.id).first()
        if leaderboard_entry:
            leaderboard_entry.wins += 1
        else:
            new_entry = Leaderboard(user_id=user.id, wins=1)
            db.session.add(new_entry)
        db.session.commit()
        return jsonify({"message": "Leaderboard updated successfully!"})
    return jsonify({"message": "User not found!"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
