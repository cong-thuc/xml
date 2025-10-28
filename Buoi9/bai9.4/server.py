from flask import Flask, jsonify, request

app = Flask(__name__)

# -------------------------
# Trang chủ / (mặc định)
# -------------------------
@app.route('/')
def home():
    return (
        "<h2>🚀 Flask Server dang chay!</h2>"
        "<p>Hay thu truy cap cac duong dan sau:</p>"
        "<ul>"
        "<li><a href='/api/book'>/api/book</a> - Lay thong tin quyen sach</li>"
        "<li><a href='/api/user/Thuc123'>/api/user/Thuc123</a> - Lay thong tin nguoi dung Thuc123</li>"
        "<li>POST /api/subtract - Gui JSON {'a': 10, 'b': 5} de nhan ket qua phep tru</li>"
        "</ul>"
    )

# -------------------------
# API 1: /api/book
# -------------------------
@app.route('/api/book', methods=['GET'])
def get_book():
    book = {
        "title": "Hoc Python co ban",
        "author": "Le Cong Thuc",
        "price": 120000,
        "inStock": True,
        "categories": ["Lap trinh", "Python", "Co ban"],
        "rating": 4.5
    }
    return jsonify(book)

# -------------------------
# API 2: /api/user/<username>
# -------------------------
@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    users = {
        "Thuc123": {
            "username": "Thuc123",
            "password": "Abc@1234",
            "emails": ["thuc123@example.com", "backup@gmail.com"],
            "age": 16,
            "address": {"city": "Can Tho", "street": "45 Nguyen Trai"},
            "hobbies": ["doc sach", "choi game"],
            "isVerified": False
        },
        "lan456": {
            "username": "lan456",
            "password": "Xyz@5678",
            "emails": ["lan456@example.com"],
            "age": 18,
            "address": {"city": "Ha Noi"},
            "hobbies": ["ve", "nghe nhac"]
        }
    }

    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "Khong tim thay nguoi dung"}), 404

# -------------------------
# API 3: /api/subtract (POST)
# -------------------------
@app.route('/api/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    a = data.get('a')
    b = data.get('b')

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({"error": "Gia tri a va b phai la so"}), 400

    result = a - b
    return jsonify({"a": a, "b": b, "result": result})

# -------------------------
# Chay server
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
