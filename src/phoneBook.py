class Person:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def print(self):
        print(f"{self.name} is {self.age} years old with phone number: {self.phone}")

def main():
    phoneBook = {}
    print("Welcome to your phone book!")
    while True:
        print("1. Add a person")
        print("2. Remove a person")
        print("3. Print all people")
        print("4. Exit")
        choice = input("Please enter your choice: ")
        if choice == "1":
            name = input("Enter the name of the person: ")
            age = input("Enter the age of the person: ")
            phone = input("Enter the phone number of the person: ")
            person = Person(name, age, phone)
            phoneBook[name] = person
        elif choice == "2":
            flag = 0
            inp = input("Enter the name of the person you wish to remove: ")
            for k in phoneBook.keys():
                if(inp == k):
                    phoneBook.pop(k)
                    print("Person removed!")
                    flag = 1
                    break
            if flag == 0:
                print("Person not found!")
        elif choice == "3":
            print()
            for person in phoneBook.values():
                person.print()
            print()
        elif choice == "4":
            print("Thank you for using our phone book system!")
            break
        else:
            print("Invalid choice, please try again!")

main()