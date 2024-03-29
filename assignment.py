# 1. Real-World Python Dictionary Applications

# Objective:
# The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, and dictionary methods in real-world scenarios. You will apply these concepts to solve practical problems, demonstrating your ability to manipulate and manage complex data structures.

# Task 1: Restaurant Menu Update
# You are given an initial structure of a restaurant menu stored in a nested dictionary. Your task is to update this menu based on given instructions. This exercise tests your ability to manipulate nested dictionaries and manage data effectively.

# Problem Statement:
# Given the initial menu:

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

#     Add a new category called "Beverages" with at least two items.
#     Update the price of "Steak" to 17.99.
#     Remove "Bruschetta" from "Starters".

restaurant_menu["Beverages"] = {"Soda" : 1.99, "Tea" : 1.50}

restaurant_menu["Main Course"]["Steak"] = 17.99

del restaurant_menu["Starters"]["Bruschetta"]

print(restaurant_menu)

# 2. Advanced Data Handling with Python

# Objective:
# The aim of this assignment is to deepen your knowledge and practical skills in handling complex data structures using Python. You will work on real-world inspired tasks that require advanced manipulation of dictionaries, nested collections, and implementing custom functions for specific data processing needs.

# Task 1: Hotel Room Booking Tracker
# Enhance your ability to work with nested collections by developing a system to track room bookings for a hotel.

# Problem Statement:
# Develop a program that:

#     Manages room bookings, where each room has details such as booking status (booked/available) and customer name.
#     Implement functions to:
#         Book a room (mark as booked and assign to a customer).
#         Check-out a customer (mark room as available and remove customer name).
#         Display the status of all rooms.

# Start with this initial hotel room structure:

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_a_room(hotel_rooms, room_number, customer_name):
    if room_number in hotel_rooms:
        hotel_rooms[room_number]["status"] = "booked"
        hotel_rooms[room_number]["customer"] = customer_name
    else:
        print("The room number was not found in hotel_rooms")

def check_out_customer(hotel_rooms, room_number):
    if room_number in hotel_rooms:
        hotel_rooms[room_number]["customer"] = ""
        hotel_rooms[room_number]["status"] = "available"
    else:
        print("The room number was not found in hotel_rooms")

def display_all_rooms():
    print(hotel_rooms)

display_all_rooms()
book_a_room(hotel_rooms, "101", "John Doe")
check_out_customer(hotel_rooms, "102")
display_all_rooms()




# Task 2: E-commerce Product Search Feature
# Put your data handling and string manipulation skills to the test by creating a product search feature for an e-commerce platform.

# Problem Statement:
# Create a system that:

#     Holds a dictionary of products where each product has attributes like name, category, and price.
#     Implement a search function that allows searching for products by name, returning a list of matching products (case-insensitive search).
#     Handle cases where no matches are found.

# Example product dictionary:

products = {
    "1": {"name": "Laptop", "category": "Electronics", "price": 800},
    "2": {"name": "Shirt", "category": "Clothing", "price": 20}
}

def search_products(products, name):
    for id, description in products.items():
        if name in description["name"]:
            print(f"{name} found in products with id {id}")
        else:
            print(f"{name} was not found in product # {id}")

search_products(products, "Laptop")
search_products(products, "Pants")

# 3. Python Programming Challenges for Customer Service Data Handling

# Objective:
# This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker
# Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement:
# Develop a program that:

#     Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
#     Implement functions to:
#         Open a new service ticket.
#         Update the status of an existing ticket.
#         Display all tickets or filter by status.
#     Initialize with some sample tickets and include functionality for additional ticket entry.

# Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_new_service_ticket(ticket_number, customer_name, issue):
    if ticket_number not in service_tickets:
        service_tickets[ticket_number] = {"Customer" : customer_name, "Issue" : issue, "Status" : "open"}
    else:
        print(f"Ticket number {ticket_number} already exists in service_tickets")

def update_service_ticket_status(ticket_number):
    if ticket_number in service_tickets:
        service_tickets[ticket_number]["Status"] = "closed" if service_tickets[ticket_number]["Status"] == "open" else "open"
    else:
        print(f"Ticket number {ticket_number} does not exist in service_tickets")

def display_all_service_tickets():
    print(service_tickets)

open_new_service_ticket("Ticket003", "Chandler", "Forgot password")
update_service_ticket_status("Ticket001")
update_service_ticket_status("Ticket002")
update_service_ticket_status("Ticket003")
display_all_service_tickets()


# 4. Python Essentials for Business Analytics

# Objective:
# This assignment aims to strengthen your proficiency in Python by tackling challenges that simulate real-world business analytics scenarios. You'll practice copying dictionaries, utilizing built-in methods, managing nested collections, and implementing try-except blocks for error handling.

# Task 1: Sales Data Cloning and Modification
# Gain practical experience in copying dictionaries and modifying data, crucial skills in data analysis.

# Problem Statement:
# You have a dictionary representing weekly sales data for a store. Your task is to create a deep copy of this data and update the sales figures for a specific week.

# Given Sales Data:

import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

#     Create a deep copy of weekly_sales.
#     Update the sales figure for "Electronics" in "Week 2" to 18000 in the copied data.

weekly_sales_deep_copy = copy.deepcopy(weekly_sales)

print(weekly_sales_deep_copy)
weekly_sales_deep_copy["Week 2"]["Electronics"] = 18000
print(weekly_sales_deep_copy)