# A Python To Do List that writes to a text file

def main():
   print("Welcome to your To Do List!")
   user = input("What is your name?: ")
   fname = input("What would you like your output file to be called?: ")
   fname = fname + ".txt"
   f = open(fname,"a")
   f.write("A To-Do-List for " + user +"!")
   f.write("\n hello world")
#    while True:
#         menu = input("What would you like to do? (Add, View, or Quit): ")
#         if menu == "Add":
#             add = input("What would you like to add?: ")
#             file.write(add + "\n")
#         elif menu == "View":
#             file = open(fname,"r")
#             print(file.read())
#         elif menu == "Quit":
#             file.close()
#             print("Goodbye!")
#             break
    
main()