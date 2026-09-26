"""
Midterm Practical Exam — Pet Adoption Records Manager
Student: Sapnu, Charlotte G.
"""

pets_list = []

def add_pet(name, type, status):
    while True:
        name = input("Name of the Pet:")
        type = input("Type of the Pe:")
        status = input("Type the Status of the Pet:")
        if name and type and status != "":
            pets_list.append({"name": name, "type": type, "status" : status})
            print("Added to the lists!")
        elif name or type or status == "":
            pets_list.append({"name": name, "type": type, "status" : status})
            print("There's missing to fill in.")
        elif name or type or status == 0:
                    pets_list.append({"name": name, "type": type, "status" : status})
                    print("No numbers.")

def view_pets(pets_list):
    for item in pets_list:
        print(item)

def count_available_avail():
     while True:
          choice = input("Available or Adopted? : ")
          if choice == "Available":
               print()
          elif choice == "Adopted":
               print()

def count_available_adopted(status):
    for item in pets_list:
        if status == "Available":
            print(item)
        elif status == "Adopted":
            print(item)
        
def find_pet(name):
    for item in pets_list:
         if name == name:
              print(pets_list)
         else:
              print("Not Found")
        
def display_menu():
  while True:
        print(f" Pet Adoption ")
        print("1. Add a pet\n2. View all pets\n3. Count available vs adopted\n4. Find a pet by name\n5. Exit")
        choice = input("Choose an option [1-5]:")

        if choice == 1:
            add_pet()
        elif choice == 2:
            view_pets()
        elif choice == 3:
            count_available_adopted
        elif choice == 4:
            find_pet()
        elif choice == 5:
            return
        
display_menu()
