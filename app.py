from flask import Flask, render_template, request

app = Flask(__name__)

# Temporary storage
rooms = []
bookings = []

# Home route (optional)
@app.route("/")
def home():
    return "Hotel Booking App Home"

# Add Room
@app.route("/add_room", methods=["GET", "POST"])
def add_room():
    if request.method == "POST":
        room_name = request.form["room_name"]
        price = request.form["price"]
        rooms.append({"name": room_name, "price": price})
        return f"Room '{room_name}' added successfully at price {price}"
    return render_template("add_room.html")

# Add Booking (updated for Day 10)
@app.route("/add_booking", methods=["GET", "POST"])
def add_booking():
    if request.method == "POST":
        room_name = request.form["room_name"]
        price = request.form["price"]
        # Save booking in bookings list
        bookings.append({"name": room_name, "price": price})
        return f"Booking for '{room_name}' at ₹{price} confirmed!"
    return render_template("add_booking.html")

# View Rooms
@app.route("/view_rooms")
def view_rooms():
    return render_template("view_rooms.html", rooms=rooms)

# View Bookings (new Day 10 route)
@app.route("/view_bookings")
def view_bookings():
    return render_template("view_bookings.html", bookings=bookings)

# Run Flask
if __name__ == "__main__":
    app.run(debug=True)
    
    