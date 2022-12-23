# A Python To Do List that writes to a text file

def main():
   print("Welcome to your To Do List!\n")
   user = input("What is your name?: ")
   fname = input("What would you like your output file to be called?: ")
   fname = fname + ".txt"
   f = open(fname,"a")
   f.write("To-Do-List for " + user +":\n")
   f.close()
   while True:
        print(fname)
        menu = input("What would you like to do? (Add, View, or Quit): ")
        if menu == "Add":
            f = open(fname,"a")
            add = input("What would you like to add?: ")
            f.write(add + "\n")
        elif menu == "View":
            f = open(fname,"r")
            print(f.read())
        elif menu == "Quit":
            f.close()
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please try again.")
main()