book={}
while True:
    print("1.inset books")
    print("2.delete books")
    print("3.search books")
    print("4.update books")
    print("5.dispaly books")
    print("6.exit")
    choice=int(input("enter the choice"))
    if choice==1:
        book_id=input("enter book id")
        author=input("enter the author name")
        title=input("enter the title of book")
        book[book_id]={"title":title,"author":author}
        print("book inserted successfully")
    elif choice==2:
        book_id=input("enter the book id to delete")
        if book_id in book:
            del book[book_id]
            print("book deleted successfully")
        else:
            print("book is not found")

    elif choice==3:
        book_id=input("enter the book id to search")
        if book_id in book:
            print("book details")
            print("title",book[book_id]["title"])
            print("author",book[book_id]["author"])
        else:
            print("book is not found")
    elif choice==4:
        book_id=input("enter the book id to update")
        if book_id in book:
            book[book_id]["title"]=input("enter new title")
            book[book_id]["author"]=input("enter new author")
            print("book updated successfully")
        else:
            print("book is not found")
    elif choice==5:
        if book:
            print("book details are")
            for book_id,details in book.items():
                print("book id ",book_id)
                print("title",details["title"])
                print("author",details["author"])
                print("-----------------------------")
        else:
            print("book is not avaible")
    elif choice==6:
        print("exiting in this program....")
        break
    else:
        print("invalid choice")
            

            
