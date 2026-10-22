class HostelManagementSystem:
    def __init__(self, total_rooms):
        # Dictionary for Room Allocation: Room Number -> Student ID (None if vacant)
        self.rooms = {room: None for room in range(101, 101 + total_rooms)}
        # Dictionary for Student Records: Student ID -> Details
        self.students = {}
        # List to maintain history logs
        self.logs = []

    def check_in(self, student_id, name, room_number):
        if room_number not in self.rooms:
            print(f"❌ Error: Room {room_number} does not exist.")
            return
        if self.rooms[room_number] is not None:
            print(f"❌ Error: Room {room_number} is already occupied.")
            return
        if student_id in self.students:
            print(f"❌ Error: Student ID {student_id} is already checked in.")
            return

        # Allocate room and store details
        self.rooms[room_number] = student_id
        self.students[student_id] = {
            "name": name,
            "room": room_number,
            "mess_fee": 0.0
        }
        self.logs.append(f"CHECK-IN: {name} (ID: {student_id}) allocated Room {room_number}")
        print(f"✅ Success: {name} checked into Room {room_number}.")

    def update_mess_fee(self, student_id, amount):
        if student_id not in self.students:
            print("❌ Error: Student record not found.")
            return
        self.students[student_id]["mess_fee"] += amount
        print(f"✅ Success: Updated mess fee for {self.students[student_id]['name']}. Balance: ₹{self.students[student_id]['mess_fee']}")

    def check_out(self, student_id):
        if student_id not in self.students:
            print("❌ Error: Student record not found.")
            return
        
        student = self.students[student_id]
        if student["mess_fee"] > 0:
            print(f"⚠️ Dues Pending: Cannot check out. Outstanding mess fee: ₹{student['mess_fee']}")
            return

        # Clear room and remove student record
        room_number = student["room"]
        self.rooms[room_number] = None
        self.logs.append(f"CHECK-OUT: {student['name']} (ID: {student_id}) vacated Room {room_number}")
        del self.students[student_id]
        print(f"✅ Success: Student ID {student_id} successfully checked out.")

    def display_hostel_status(self):
        print("\n--- Current Hostel Status ---")
        for room, student_id in self.rooms.items():
            if student_id:
                print(f"Room {room}: Occupied by {self.students[student_id]['name']} (ID: {student_id})")
            else:
                print(f"Room {room}: Vacant")

    def view_logs(self):
        print("\n--- System Activity Logs ---")
        for log in self.logs:
            print(log)

# --- Demonstration of the System ---
if __name__ == "__main__":
    # Initialize hostel with 5 rooms (Rooms 101 to 105)
    hostel = HostelManagementSystem(total_rooms=5)

    print("--- 1. Checking In Students ---")
    hostel.check_in("S101", "Rahul Sharma", 101)
    hostel.check_in("S102", "Amit Verma", 102)

    print("\n--- 2. Managing Mess Fees ---")
    hostel.update_mess_fee("S101", 2500.0)

    print("\n--- 3. Attempting Check-out with Dues ---")
    hostel.check_out("S101")  # Will fail due to outstanding balance

    print("\n--- 4. Clearing Dues and Checking Out ---")
    hostel.update_mess_fee("S101", -2500.0)  # Simulating fee payment
    hostel.check_out("S101")  # Will succeed now

    print("\n--- 5. Viewing Final Status & Logs ---")
    hostel.display_hostel_status()
    hostel.view_logs()
