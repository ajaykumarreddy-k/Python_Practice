from flask import Flask, request

app = Flask(__name__)

students = [
    {'id': 1, 'name': 'Alice', 'age': 20},
    {'id': 2, 'name': 'Bob', 'age': 22},
    {'id': 3, 'name': 'Charlie', 'age': 23}
]

@app.route('/')
def home():
    return "Welcome to the Student API", 200

@app.route('/students', methods=['GET'])
def get_students():
    return {"students": students}, 200

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    new_student = {
        "id": data["id"],
        "name": data["name"],
        "age": data["age"]
    }

    students.append(new_student)
    return {
        "message": "Student added successfully",
        "student": new_student
    }, 201
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    for student in students:
        if student['id'] == student_id:
            student['name'] = data.get('name', student['name'])
            student['age'] = data.get('age', student['age'])
            return {
                "message": "Student updated successfully",
                "student": student
            }, 200
    return {"message": "Student not found"}, 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
