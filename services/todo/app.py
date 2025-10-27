from flask import Flask, request, jsonify
import os
import uuid

app = Flask(__name__)

# simple in-memory store (later replace with a DB)
TODOS = {}

@app.route("/todos", methods=["GET"])
def list_todos():
    return jsonify(list(TODOS.values()))

@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.json or {}
    todo_id = str(uuid.uuid4())
    todo = {"id": todo_id, "title": data.get("title", ""), "done": False}
    TODOS[todo_id] = todo
    return jsonify(todo), 201

@app.route("/todos/<tid>", methods=["DELETE"])
def delete_todo(tid):
    if tid in TODOS:
        del TODOS[tid]
        return "", 204
    return jsonify({"error": "not found"}), 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
