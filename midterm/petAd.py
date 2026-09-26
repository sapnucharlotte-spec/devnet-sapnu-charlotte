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
    for item in pets_list:
        print(item)

def main ():
     print("Success")

if __name__ == "__main__":
    main()

    