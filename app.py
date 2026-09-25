from flask import Flask, jsonify, request

app = Flask(__name__)


# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}


# In-memory "database"
events = [Event(1, "Tech Meetup"), Event(2, "Python Workshop")]
next_id = 3


def find_event(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None


# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    global next_id
    # TODO: Task 2 - Design and Develop the Code
    data = request.get_json()

    if "title" not in data or not data["title"]:
        return jsonify({"error": "Title is required"}), 400

    new_event = Event(next_id, data["title"])
    events.append(new_event)
    # TODO: Task 3 - Implement the Loop and Process Each Element

    result = [event.to_dict() for event in events]

    # TODO: Task 4 - Return and Handle Results

    next_id += 1
    return jsonify(result), 201


# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    event = find_event(event_id)

    # TODO: Task 3 - Implement the Loop and Process Each Element
    if event is None:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json()

    if "title" in data:
        if not data["title"]:
            return jsonify({"error": "Title not found"}), 400
        event.title = data["title"]

    # TODO: Task 4 - Return and Handle Results
    return jsonify(event.to_dict()), 200


# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    global events
    # TODO: Task 2 - Design and Develop the Code
    event = find_event(event_id)

    if event is None:
        return jsonify({"error": "Event not Found"}), 404

    events = [event for event in events if event.id != event_id]

    # TODO: Task 3 - Implement the Loop and Process Each Element

    # TODO: Task 4 - Return and Handle Results
    result_events = [event.to_dict() for event in events]
    return jsonify(result_events), 200


if __name__ == "__main__":
    app.run(debug=True)
