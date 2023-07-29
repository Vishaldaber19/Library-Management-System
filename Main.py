# dependencies of project
import os
import datetime as time

# Class Of Library Management System


class LibSys:

    # Constructor
    def __init__(self, booklist, library_name):
        self.booklist = booklist
        self.library_name = library_name
        self.books_dict = {}
        Id = 1001
        Misserror = str("<__main__.LibSys object at 0x7fb38fc99040>")
        with open(self.booklist) as book:
            book_name = book.readlines()
        for line in book_name:
            if (line == Misserror):
                continue
            self.books_dict.update({str(Id): {"Book_Title": line.replace(
                "\n", ""), "Borrower_Name": "", "Issue_Date": "", "Status": "Available"}})
            Id += 1

    # Displaying Books

    def Display_books(self):
        print("\n-------------List of Books--------------\n")
        print("Books ID", "\t", "Title")
        print("-------------------------------")
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("Book_Title"),
                  "-[", value.get("Status"), "]")

    # Issuing Book
    def Issue_book(self):
        books_id = input("Enter Books ID: ")
        current_date = time.datetime.now().strftime("%D %H:%M:%S")
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]["Status"] == "Available":
                print(
                    f"This books is already issued to {self.books_dict[books_id]['Borrower_Name']} \t on {self.books_dict[books_id]['Issue_Date']}")
                return self.Issue_book()
            elif self.books_dict[books_id]["Status"] == "Available":
                your_name = input("Enter your name: ")
                self.books_dict[books_id]["Borrower_Name"] = your_name
                self.books_dict[books_id]["Issue_Date"] = current_date
                self.books_dict[books_id]["Status"] = "Already Issued"
                print("Book Issued Successfully !!! \n")
        else:
            print("Book ID not found!!!")

    # Adding New Book
    def Add_book(self):
        new_book_title = input("Enter books title: ")
        if new_book_title == "":
            return self.Add_book()
        elif len(new_book_title) > 20:
            print("Book Title is too long!! Title length should be 20 characters")
            return self.Add_book()
        else:
            with open(self.booklist, "a") as book:
                book.writelines(f"{new_book_title}\n")
                new_book_id = str(1000+int(len(self.books_dict)+1))
                self.books_dict.update({new_book_id: {
                                       "Book_Title": new_book_title, "Borrower_Name": "", "Issue_Date": "", "Status": "Available"}})
                print(
                    f"This book '{new_book_title}' has been added successfully!! ")

    # Return Book
    def return_book(self):
        book_id = input("Enter Book ID you want to return: ")
        if book_id in self.books_dict.keys():
            if self.books_dict[book_id]["Status"] == "Available":
                print(
                    "This book is already available in library. Please check your book ID")
                return self.return_book()
            else:
                self.books_dict[book_id]["Borrower_Name"] = ""
                self.books_dict[book_id]["Issue_Date"] = ""
                self.books_dict[book_id]["Status"] = "Available"
                print("Successfully Updated!!")
        else:
            print("Book ID not found")


# Execption Handling
try:
    Myobject = LibSys("BookList.txt", "Python")
    key_press_list = {"D": "Display Books", "I": "Issue Books",
                      "A": "Add Books", "R": "Return Books", "Q": "Quit"}
    while True:
        print(
            f"\n--------------Welcome to {Myobject.library_name} Library Management System----------------- \n")
        for key, value in key_press_list.items():
            print(f"Press {key} To {value}")
        try:
            pressed_key = input("Press key: ").lower()
        except: 
            print("\nThank You for Using the App")
            break
        if pressed_key == "i":
            os.system('clear')
            print("\nCurrent Selection : Issue Books\n")
            Myobject.Issue_book()
        elif pressed_key == "r":
            os.system('clear')
            print("\nCurrent Selection : Return Books\n")
            Myobject.return_book()
        elif pressed_key == "d":
            os.system('clear')
            print("\nCurrent Selection : Display Books\n")
            Myobject.Display_books()
        elif pressed_key == "a":
            os.system('clear')
            print("\nCurrent Selection : Add Books\n")
            Myobject.Add_book()
        elif pressed_key == "q":
            print("Thank You for Using the App")
            break
        else:
            print("Please press a valid key")
            continue
except Exception as error:
    print("Something went wrong. Please check your input!!"+error)
