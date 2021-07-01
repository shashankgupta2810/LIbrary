class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks
    
    def displayAvailableBooks(self):
        print("Books present in this library are : ")
        for index,book in enumerate(self.books):
            print(index+1,book)
    
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have issued {bookName} book.")
            self.books.remove(bookName)
        else:
            print("This book is not available")
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for return")

class Student:
    def requestBook(self):
        self.book = input("Enter the book name which you want borrow ")
        return self.book 
    def returnBook(self):
        self.book = input("Enter the book which you want return ")
        return self.book
     
if __name__=="__main__":
    student = Student()
    grandLibrary = Library(["python","data Science","software developer","django","flask","C","C++","java"])
    while(True):
        welcomeMsg =''' =======Welcome to Grand Library======
        Please choose an option:
        1.Listing all the books
        2.Request a book
        3.Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a= input("Enter a Choice:")
        try:
            a= int(a)
            if a==1:
                grandLibrary.displayAvailableBooks()
            elif a==2:
                grandLibrary.borrowBook(student.requestBook())
            elif a==3:
                grandLibrary.returnBook(student.returnBook())
            elif a==4:
                print("Thank for using")
                exit()   
            else:
                print("You choose wrong number")
        except:
            print(f"Your are enter '{a}' please enter valid number between 1 to 4")