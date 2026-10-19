shows = {
    "THE ODYSSEY": {
        "time": "10:00 AM",
        "price": 230
    },
    "SPIDER-MAN : BRAND NEW DAY": {
        "time": "1:30 PM",
        "price": 230
    },
    "THE AVERGERS: ENDGAME": {
        "time": "6:00 PM",
        "price": 230
    },
    "i=I AM GAME": {
        "time": "9:00 PM",
        "price": 230
    }
}

bookings=[]
booking_id =1

def list_shows():
    print("\n----- AVAILABLE MOVIES -----")

    for movie, details in shows.items():
        print("Movie:", movie)
        print("Show Time:", details["time"])
        print("Ticket Price: Rs.", details["price"])
        print("----------------------------")

def calculate_total(price, quantity, discount=0):
    total = price * quantity
    total = total - (total * discount / 100)
    return total


def loyalty_discount(total, quantity):
    if quantity < 2:
        return total

    total = total * 0.90
    return loyalty_discount(total, quantity - 2)


def book_tickets(show_name, number_of_tickets, *seat_numbers):
    global booking_id

    if show_name not in shows:
        print("Movie not found!")
        return

    if number_of_tickets <= 0:
        print("Number of tickets must be greater than zero.")
        return

    if len(seat_numbers) != number_of_tickets:
        print("Please enter exactly", number_of_tickets, "seat numbers.")
        return
    

    booked_seats = []

    for booking in bookings:
        if booking["movie"].lower() == show_name.lower():
            booked_seats.extend(booking["seats"])

    if len(set(seat_numbers)) != len(seat_numbers):
        print("Duplicate seat numbers are not allowed.")
        return

    for seat in seat_numbers:
        if seat in booked_seats:
            print("Seat", seat, "is already booked!")
            return

    price = shows[show_name]["price"]
    quantity = number_of_tickets

    print("\nPayment Methods:")
    print("1. Cash")
    print("2. GPay")
    print("3. Credit Card")

    payment_choice = input("Choose payment method: ")

    if payment_choice == "1":
        payment_method = "Cash"
        discount = 0
        convenience_fee = 0

    elif payment_choice == "2":
        payment_method = "GPay"
        discount = 0
        convenience_fee = 30

    elif payment_choice == "3":
        payment_method = "Credit Card"
        discount = 30
        convenience_fee = 0

    else:
        print("Invalid payment method!")
        return

    total = calculate_total(price, quantity, discount)

    total = loyalty_discount(total, quantity)

    total = total + convenience_fee

    booking = {
        "id": booking_id,
        "movie": show_name,
        "time": shows[show_name]["time"],
        "quantity": quantity,
        "seats": list(seat_numbers),
        "payment": payment_method,
        "total": round(total, 2),
        "cancelled": False
    }

    bookings.append(booking)

    print("\nBooking successful!")
    print("Booking ID:", booking_id)
    print("Movie:", show_name)
    print("Seats:", seat_numbers)
    print("Payment Method:", payment_method)
    print("Total Amount: Rs.", round(total, 2))

    booking_id += 1

def view_bookings():
    print("\n----- BOOKING DETAILS -----")

    if not bookings:
        print("No bookings available.")
        return

    for booking in bookings:
        if not booking["cancelled"]:
            print("\nBooking ID:", booking["id"])
            print("Movie:", booking["movie"])
            print("Show Time:", booking["time"])
            print("Number of Tickets:", booking["quantity"])
            print("Seats:", booking["seats"])
            print("Payment:", booking["payment"])
            print("Total: Rs.", booking["total"])


def cancel_booking():
    try:
        cancel_id = int(input("Enter booking ID to cancel: "))
    except ValueError:
        print("Please enter a valid booking ID.")
        return

    for booking in bookings:
        if booking["id"] == cancel_id and not booking["cancelled"]:

            price = shows[booking["movie"]]["price"]
            quantity = booking["quantity"]
            payment = booking["payment"]

            # Recalculate the amount using the same pricing rules
            if payment == "Credit Card":
                refund = calculate_total(price, quantity, 30)
            else:
                refund = calculate_total(price, quantity)

            refund = loyalty_discount(refund, quantity)

            if payment == "GPay":
                refund += 30

            refund = min(round(refund, 2), booking["total"])

            booking["cancelled"] = True

            print("\nBooking cancelled successfully!")
            print("Booking ID:", cancel_id)
            print("Refund Amount: Rs.", refund)
            return

    print("Active booking not found!")


def main():
    while True:
        print("\n===== MOVIE TICKET BOOKING =====")
        print("1. List Available Shows")
        print("2. Book Tickets")
        print("3. View Bookings")
        print("4. Cancel Booking")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_shows()

        elif choice == "2":
            list_shows()

            movie = input("Enter movie name: ")

            try:
                quantity = int(input("Enter number of tickets: "))

                if quantity <= 0:
                    print("Number of tickets must be positive.")
                    continue

                seats = []

                for i in range(quantity):
                    seat = input("Enter seat number " + str(i + 1) + ": ")
                    seats.append(seat)

                book_tickets(movie, quantity, *seats)

            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            view_bookings()

        elif choice == "4":
            cancel_booking()

        elif choice == "5":
            print("Thank you for using the booking system!")
            break

        else:
            print("Invalid choice! Please try again.")


main()