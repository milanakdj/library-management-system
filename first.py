
import sys


class Library:
    def __init__(self, listofbooks):
        self.availablebook = listofbooks

    def displayavailablebooks(self):
        print("===================")
        print("the avialable books are ")
        for book in self.availablebook:
            print(book)

    def lendbook(self, requestedbook):
        # for book in self.availablebook:
        # 	if(book==book_name):
        # 		return 1;
        # 		self.availablebook.
        # 	else
        # 		return 0;
        if requestedbook in self.availablebook:
            print("the book you asked for has now been borrowed")
            self.availablebook.remove(requestedbook)
        else:
            print("the book is not avialable in the library")

    def addbook(self, book_name):
        if book_name not in self.availablebook:
            self.availablebook.append(book_name)
        print("thank you for returning the book")


class Student:
    def requestbook(self):
        # book_name=input("what book do you want ")
        print("what book do you want to lend")
        self.book = input()
        return self.book

    def returnbook(self):
        # book_name=input("what book do you want to return")
        print("what book do you want to return")
        self.book = input()
        return self.book


def main():
    student = Student()
    library = Library(["the book 1", "the book 2", "the book 3"])
    while 1 == 1:
        print(""" 
		======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
         """)
        choice = int(input("Enter Choice:"))

        if choice == 1:
            library.displayavailablebooks()
        elif choice == 2:
            library.lendbook(student.requestbook())

        # book_name=input("enter the book that you want")
        # haveorno=library.lendbook(book_name)
        # if(haveorno==1)
        # 	print("you can have the book ")
        # elif
        # 	print("the book is not available")

        elif choice == 3:
            library.addbook(student.returnbook())
        # elif choice==3
        # 	book_name=input("enter the book that you want to return")
        # 	haveorno=library.returnbook(book_name)

        elif choice == 4:
            sys.exit()


main()
