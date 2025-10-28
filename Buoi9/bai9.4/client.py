import requests
from jsonschema import validate, ValidationError

# =======================
# Schema kiểm tra book (bài 9.1)
# =======================
book_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "minLength": 3, "maxLength": 100},
        "author": {"type": "string", "minLength": 1},
        "price": {"type": "number", "exclusiveMinimum": 0},
        "inStock": {"type": "boolean"},
        "categories": {
            "type": "array",
            "items": {"type": "string", "minLength": 2}
        },
        "rating": {"type": "number", "minimum": 0, "maximum": 5}
    },
    "required": ["title", "author", "price", "inStock"]
}

# =======================
# Schema kiểm tra subtract (tự xây dựng)
# =======================
subtract_schema = {
    "type": "object",
    "properties": {
        "a": {"type": "number"},
        "b": {"type": "number"},
        "result": {"type": "number"}
    },
    "required": ["a", "b", "result"]
}


# =======================
# Gọi API /api/book
# =======================
print("🔹 Kiểm tra dữ liệu sách:")
book_response = requests.get("http://127.0.0.1:5000/api/book")
book_data = book_response.json()
print("Dữ liệu:", book_data)

try:
    validate(instance=book_data, schema=book_schema)
    print("✅ Dữ liệu sách hợp lệ!\n")
except ValidationError as e:
    print("Lỗi dữ liệu sách:", e.message, "\n")


# =======================
# Gọi API /api/user/Thuc123
# =======================
print("🔹 Lấy dữ liệu người dùng:")
user_response = requests.get("http://127.0.0.1:5000/api/user/Thuc123")
print("Dữ liệu:", user_response.json(), "\n")


# =======================
# Gọi API /api/subtract (POST)
# =======================
print("🔹 Gửi phép trừ a - b:")
data = {"a": 10, "b": 4}
subtract_response = requests.post("http://127.0.0.1:5000/api/subtract", json=data)
subtract_data = subtract_response.json()
print("Kết quả:", subtract_data)

try:
    validate(instance=subtract_data, schema=subtract_schema)
    print("✅ Kết quả hợp lệ!")
except ValidationError as e:
    print("Lỗi:", e.message)
