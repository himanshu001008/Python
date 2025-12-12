rooms = {
    101: {"type": "Single", "booked": False},
    102: {"type": "Single", "booked": False},
    201: {"type": "Double", "booked": False},
    202: {"type": "Double", "booked": False},
    301: {"type": "Suite", "booked": False}
}
def show_rooms():
    print("\nRoom No | Type   | Status")
    for room_no, info in rooms.items():
        status = "Booked" if info["booked"] else "Available"
        print(f"{room_no}     | {info['type']} | {status}")
def book_room():
    room_no = int(input("Enter room number to book: "))
    if room_no in rooms:
        if not rooms[room_no]["booked"]:
            rooms[room_no]["booked"] = True
            print(f"Room {room_no} has been booked successfully!")
        else:
            print("Sorry, this room is already booked.")
    else:
        print("Invalid room number.")
def cancel_booking():
    room_no = int(input("Enter room number to cancel booking: "))
    if room_no in rooms:
        if rooms[room_no]["booked"]:
            rooms[room_no]["booked"] = False
            print(f"Booking for room {room_no} has been canceled.")
        else:
            print("This room is not booked.")
    else:
        print("Invalid room number.")
while True:
    print("\n Hotel Reservation System ")
    print("1. Show Rooms")
    print("2. Book a Room")
    print("3. Cancel Booking")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        show_rooms()
    elif choice == 2:
        book_room()
    elif choice == 3:
        cancel_booking()
    elif choice == 4:
        print("Thank you for using our system. Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
