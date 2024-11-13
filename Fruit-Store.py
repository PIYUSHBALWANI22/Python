menu="""
                            WELCOME TO FRUIT MARKET

                                1) Manager
                                2) customer
"""
print(menu)
fruitStock=[

     {"product":"Apple","Qty": 5, "price": 120},
     {"product":"Banana","Qty": 8, "price": 80},
     {"product":"Strawberry","Qty": 6, "price": 140},
     {"product":"Mango","Qty": 12, "price": 200}
]
role=(input("select your role : ")).lower()
if role=="1" or role=="manager":
    print("""
                        Fruit Market Manager

                            1) Add fruit stock
                            2) View fruit stock
                            3) Update fruit stock
""")

    choice=(input("Enter your choice :  ")).lower()
    if choice=="1" or choice=="add fruit stock":
        print("ADD FRUIT STOCK")
        efName=input("Enter fruit name : ").capitalize()
        eQty=int(input("Enter quantity (in kg): "))
        ePrice=int(input("Enter price : "))
        fruitStock.append({"product":{efName},"Qty":{eQty},"price":{ePrice}})
        choice1=input("Do you want to add more fruit stock press y for yes and n for no :").lower()
        
        status=True
        while status :
            if choice1=="y" or choice1=="yes":
                efName=input("Enter fruit name : ").capitalize()
                eQty=int(input("Enter quantity (in kg): "))
                ePrice=int(input("Enter price : "))
                fruitStock.append({"product":efName,"Qty":eQty,"price":ePrice})
                choice1=input("Do you want to add more fruit stock press y for yes and n for no : ").lower()

            elif choice1=="n" or choice1=="no":
                for fruit in fruitStock:
                    print(fruit)
                status=False
            else: 
                status=False 
    elif choice=="2" or choice=="view fruit stock":
        print("VIEW FRUIT STOCK")
        for fruit in fruitStock:
            print(fruit)
    elif choice=="3" or choice=="update fruit stock":
        print("UPDATE FRUIT STOCK")
        print("Availabe stock to update : ")
        for fruit in fruitStock:
            print(fruit)
        fruitName=input("Enter the fruit name you want to update in stock : ").capitalize()

        fFind=False
        for fruit in fruitStock:
            if fruit["product"]==fruitName:
                fFind=True
                uQty=int(input("Enter new quantity in kgs : "))
                uPrice=int(input("Enter new price : "))

                fruit["Qty"]=uQty
                fruit["price"]=uPrice
                print(f"{fruitName} has been updated successfully")
                for fruit in fruitStock:
                    print(fruit)
                break
        if not fFind:
                print("The name you enterd is not in stock.")

    else:
                print("Invalid choice..!")

elif role=="2" or role=="customer":
    print("AVAILABE FRUIT STOCK")
    for fruit in fruitStock:
        print(f"Product : {fruit['product']}, Qty : {fruit['Qty']}, Price : {fruit['price']}")

else:
    print("Invalid input 🤡")