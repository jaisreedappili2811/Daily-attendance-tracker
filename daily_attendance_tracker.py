people = {}
attendance = []


def register_person():
    print("\n--- Registration ---")

    person_id = input("Enter numeric ID: ").strip()

    if not person_id.isdigit():
        print("Invalid ID. Numbers only.")
        return

    if person_id in people:
        print("ID already registered.")
        return

    name = input("Enter name: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    for ch in name:
        if not (ch.isalpha() or ch == " "):
            print("Invalid name. Alphabets only.")
            return

    print("1. Student")
    print("2. Employee")

    category = input("Choose category: ").strip()

    if category == "1":
        category = "Student"
    elif category == "2":
        category = "Employee"
    else:
        print("Invalid category.")
        return

    people[person_id] = {
        "name": name,
        "category": category
    }

    print("Registration successful!")


def display_people():
    print("\n--- Registered People ---")

    if not people:
        print("No people registered.")
        return

    for person_id in people:
        print(person_id, "-", people[person_id]["name"],
              "-", people[person_id]["category"])


def mark_attendance():
    person_id = input("Enter numeric ID: ").strip()

    if not person_id.isdigit():
        print("Invalid ID. Numbers only.")
        return

    if person_id not in people:
        print("Person ID not found.")
        return

    date = input("Enter date (YYYY-MM-DD): ").strip()

    if len(date) != 10 or date[4] != "-" or date[7] != "-":
        print("Invalid date format.")
        return

    date_parts = date.split("-")

    if not (date_parts[0].isdigit() and
            date_parts[1].isdigit() and
            date_parts[2].isdigit()):
        print("Invalid date.")
        return

    year = int(date_parts[0])
    month = int(date_parts[1])
    day = int(date_parts[2])

    if month < 1 or month > 12:
        print("Invalid month.")
        return

    if day < 1 or day > 31:
        print("Invalid day.")
        return

    if month in [4, 6, 9, 11] and day > 30:
        print("Invalid day for this month.")
        return

    if month == 2:
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            if day > 29:
                print("Invalid day for February.")
                return
        elif day > 28:
            print("Invalid day for February.")
            return

    print("1. Present")
    print("2. Absent")

    choice = input("Enter attendance status: ").strip()

    if choice == "1":
        status = "Present"
    elif choice == "2":
        status = "Absent"
    else:
        print("Invalid choice.")
        return

    for record in attendance:
        if record["id"] == person_id and record["date"] == date:
            record["status"] = status
            print("Attendance updated successfully.")
            return

    attendance.append({
        "id": person_id,
        "date": date,
        "status": status
    })

    print("Attendance recorded successfully.")


def show_attendance_lists():
    date = input("Enter date (YYYY-MM-DD): ").strip()

    print("\n--- Present List ---")
    present_found = False

    for record in attendance:
        if record["date"] == date and record["status"] == "Present":
            print(record["id"], "-", people[record["id"]]["name"])
            present_found = True

    if not present_found:
        print("No present records.")

    print("\n--- Absent List ---")
    absent_found = False

    for record in attendance:
        if record["date"] == date and record["status"] == "Absent":
            print(record["id"], "-", people[record["id"]]["name"])
            absent_found = True

    if not absent_found:
        print("No absent records.")


def attendance_percentage():
    person_id = input("Enter numeric ID: ").strip()

    if not person_id.isdigit():
        print("Invalid ID. Numbers only.")
        return

    if person_id not in people:
        print("Person ID not found.")
        return

    total = 0
    present = 0

    for record in attendance:
        if record["id"] == person_id:
            total += 1

            if record["status"] == "Present":
                present += 1

    if total == 0:
        print("No attendance records found.")
        return

    percentage = (present / total) * 100

    print("\n--- Attendance Percentage ---")
    print("Name:", people[person_id]["name"])
    print("Present days:", present)
    print("Recorded days:", total)
    print("Attendance percentage:", round(percentage, 2), "%")


def date_wise_report():
    date = input("Enter date (YYYY-MM-DD): ").strip()

    print("\n--- Date-wise Report ---")
    found = False

    for record in attendance:
        if record["date"] == date:
            print(record["id"], "-",
                  people[record["id"]]["name"],
                  "-", record["status"])
            found = True

    if not found:
        print("No attendance records found.")


def person_wise_report():
    person_id = input("Enter numeric ID: ").strip()

    if not person_id.isdigit():
        print("Invalid ID. Numbers only.")
        return

    if person_id not in people:
        print("Person ID not found.")
        return

    print("\n--- Person-wise Report ---")
    print("ID:", person_id)
    print("Name:", people[person_id]["name"])

    found = False

    for record in attendance:
        if record["id"] == person_id:
            print(record["date"], "-", record["status"])
            found = True

    if not found:
        print("No attendance records found.")


def main():
    while True:
        print("\n===== DAILY ATTENDANCE TRACKER =====")
        print("1. Register student or employee")
        print("2. Display registered people")
        print("3. Mark daily attendance")
        print("4. Show present and absent lists")
        print("5. Calculate attendance percentage")
        print("6. Date-wise report")
        print("7. Person-wise report")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            register_person()
        elif choice == "2":
            display_people()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            show_attendance_lists()
        elif choice == "5":
            attendance_percentage()
        elif choice == "6":
            date_wise_report()
        elif choice == "7":
            person_wise_report()
        elif choice == "0":
            print("Thank you for using Daily Attendance Tracker!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()