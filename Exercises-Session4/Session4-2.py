products = []
def read_file():
    r = open("V:\EDUCATION\PYTHON\Session-IV\Database", "r")
    for line in r:
        result = line.split(",")
        my_dic = {"id":result[0],"name":result[1],"price":result[2],"count":result[3]}
        products.append(my_dic)
        print(result)
       


def show_menu():
    print("1- add")
    print("2- remove")    
    print("3- search")
    print("4- edit")
    print("5- show_list")
    print("6- buy")
    print("7- exit")


def add():
    id = input("id: ")
    name = input("name: ")
    price = input("price: ")
    count = input("count: ")  

    new_dic = {"id":id,"name":name,"price":price,"count":count}
    products.append(new_dic)
    print(products)

def remove():
    num = input("Enter your operation: ")
    for product in products:
        if product["id"] == num or product["name"] == num:
            products.remove(product)
            print(products)
            show_list()
            break

def search():
    num = input("Enter your operation: ")
    for product in products:
        if product["id"] == num or product["name"] == num:
            print(product)
            break
    else:
        print("not found")    


def show_list():
    print("id\tname\tprice\tcount")
    for product in products:
        print(product["id"],product["name"],product["price"],product["count"] )


def buy():
    read_file()
    buy_list = []
    num = input("Enter name/id : ")
    for product in products:
        if product["id"] == num or product["name"] == num:
            print(product)
            number = int(input("number of product:  "))
            count = int(product["count"])
            price = int(product["price"])
            print(price)
            print(count)

            if number > count:
                print("Product shortage")
                break
            if count == 0:
                price("ERROR")
                break
            else:
                print("Correct")
                

                price = number * price
                print("Total price is: ", price)
                buy_list.append(product["name"])
                buy_list.append(count)
                buy_list.append(price)
                print(buy_list)
                show_list()
              
            

def store():
    st = input("Do you want to save? (Y/N)")
    if st == "Y":
        st = open("Database.txt", "a")
        for product in products:
            st.write(str(product))
            st.write("")
        print(product)
    else:
        print("Not store")


read_file()

while True:
    show_menu()

    user= int(input("Enter your number: "))

    if user == 1:
        add()
    elif  user == 2: 
        remove()
    elif  user == 3:
        search()
  
    elif  user == 5: 
        show_list() 
    elif  user == 6:
        buy()
    elif  user == 7:
        store()
        exit(0)  

    else:
        print("select another number")   