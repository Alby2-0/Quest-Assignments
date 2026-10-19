import csv


def read_attendance():
    records = []

    with open("attendance.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if len(row) != 3:
                continue

            name = row[0]
            date = row[1]
            status = row[2].capitalize()

            if status == "Present" or status == "Absent":
                records.append([name, date, status])

    return records

def calculate_attendance(records):
    employees = {}

    for record in records:
        name = record[0]
        status = record[2]

        if name not in employees:
            employees[name] = {
                "Present": 0,
                "Absent": 0
            }

        if status == "Present":
            employees[name]["Present"] += 1
        else:
            employees[name]["Absent"] += 1

    return employees


def calculate_percentage(present, absent):
    total = present + absent

    if total == 0:
        return 0

    return (present/total)*100


def display_report(employees):
    print("\nEMPLOYEE ATTENDANCE REPORT")
    print("--------------------------")

    for name in employees:
        present = employees[name]["Present"]
        absent = employees[name]["Absent"]

        percentage = calculate_percentage(present, absent)

        print("\nEmployee:", name)
        print("Present Days:", present)
        print("Absent Days:", absent)
        print("Attendance:", round(percentage, 2), "%")

        if percentage < 75:
            print("WARNING: Attendance below 75%")


def write_report(employees):
    with open("attendance_report.txt", "a") as file:

        file.write("EMPLOYEE ATTENDANCE REPORT\n")
        file.write("=====================================\n\n")

        for name in employees:
            present = employees[name]["Present"]
            absent = employees[name]["Absent"]

            percentage = calculate_percentage(present, absent)

            file.write("Employee: " + name + "\n")
            file.write("Present Days: " + str(present) + "\n")
            file.write("Absent Days: " + str(absent) + "\n")
            file.write("Attendance: " + str(round(percentage, 2)) + "%\n")

            if percentage < 75:
                file.write("WARNING: Attendance below 75%\n")

            file.write("\n")


def add_attendance():
    name = input("Enter employee name: ")
    date = input("Enter date: ")
    status = input("Enter status (Present/Absent): ").capitalize()

    if status == "Present" or status == "Absent":
        with open("attendance.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, date, status])

        print("Attendance added successfully.")
    else:
        print("Invalid status.")


def main():

    while True:

        print("\nEmployee Attendance Management System")
        print("1. View Report")
        print("2. Add Attendance")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            records = read_attendance()

            if len(records) == 0:
                print("No attendance records found.")
            else:
                employees = calculate_attendance(records)
                display_report(employees)
                write_report(employees)

        elif choice == "2":
            add_attendance()

        elif choice == "3":
            print("Program ended.")
            break

        else:
            print("Invalid choice.")


main()