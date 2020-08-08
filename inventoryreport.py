# product lists
product_names = ["soft drink", "onion rings", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_inventory = [10, 5, 20]

while True:
    #list out options
    option = input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit: ")
    #quit the program
    if option == "q":
        break
    #search for product
    elif option == "s":
        name = input("Enter name of product to search for: ").lower()
        #see if we sell this product
        if name in product_names:
          #search the product_costs list for the product price
            position = product_names.index( name )
            print ("We sell", name, "for", product_costs[ position] )
            print ("We have", product_inventory[position], "left")
        else:
            print ("We don't sell", name)
    #list all the products available
    elif option == "l":
        print("Product", format("Price", ">20s"), format("Quantity",">20s"))
        #for loop to list each category
        for i in range(0, len(product_names)):
            print(product_names[i], format(product_costs[i],">16.2f"), format(product_inventory[i],">20"))
    #add another product
    elif option == "a":
        #product name
        while True:
            entry=input("Enter a new product name: ")
            if entry in product_names:
                print("Sorry, we already sell that product. Try again.")
            #add the entry to the list
            else:
                product_names += [entry]
                break
        #product cost
        while True:
            price=input("Enter a product cost: ")
            #try/except block if price does not convert into float
            try:
                if float(price)> 0:
                    product_costs += [float(price)]
                    break
                else:
                    print("Invalid price. Try again")
            except:
                print("Invalid price. Try again.")
        #inventory
        while True:
            quantity=input("How many of these products do we have? ")
            #if quantity is a float
            if float(quantity)%1 != 0:
                print("Invalid quantity. Try again.")
            #if quantity is greater than 0, convert to int and add to list
            elif float(quantity)> 0:
                product_inventory += [int(quantity)]
                break
            else:
                print("Invalid quantity. Try again.")
    #remove a product
    elif option == "r":
            discard=input("Enter a product name: ")
            #if the word to discard is in your list, delete the name, cost, and location
            if discard in product_names:
                try:
                    location=product_names.index(discard)
                    del product_names[location]
                    del product_costs[location]
                    del product_inventory[location]
                    print("Product removed!")
                except:
                    print("Sorry, there are no more products left!")
            else:
                print("Product doesn't exist. Can't remove.")
    #update a product
    elif option == "u":
        entry=input("Enter a product name: ")
        #see if product exists
        if entry in product_names:
            print("What would you like to update?")
            #what can be updated
            update=input("(n)ame, (c)ost or (q)uantity: ")
            #new name
            if update == "n":
                while True:
                    new_name=input("Enter a new name: ")
                    if new_name in product_names:
                        print("Duplicate name!")
                    else:
                        location=product_names.index(entry)
                        product_names[location]=new_name
                        print("Product name has been updated!")
                        break
            #new cost
            elif update == "c":
                while True:
                    new_cost=input("Enter a new cost: ")
                    #try/exception loop if cost is not a float
                    try:
                        if float(new_cost)> 0:
                            #find location of old product and replace
                            location=product_names.index(entry)
                            product_costs[location]=float(new_cost)
                            print("Product price has been updated!")
                            break
                        else:
                            print("Invalid price. Try again.")
                    except:
                        print("Invalid price. Try again.")
            #new quantity
            elif update == "q":
                while True:
                    new_inventory=input("How may of these products do we have? ")
                    #if inventory is a float
                    if float(new_inventory)%1 != 0:
                        print("Invalid quantity. Try again.")
                    elif float(new_inventory)> 0:
                        #find location of old product and replace
                        location=product_names.index(entry)
                        product_inventory[location]=new_inventory
                        print("Product inventory has been updated!")
                        break
                    else:
                        print("Invalid quantity. Try again.")
            else:
                print("Invalid entry.")
        else:
            print("Product doesn't exist. Can't update.")
    #report
    elif option == "e":
        #most expensive
        most_expensive=max(product_costs)
        #find location of product after finding highest price
        location=product_costs.index(most_expensive)
        product=product_names[location]
        print("Most expensive product:", format(most_expensive, ">10.2f"), " (", product,")", sep="")
        #least expensive
        least_expensive=min(product_costs)
        #find location of product after finding lowest price
        location=product_costs.index(least_expensive)
        productmin=product_names[location]
        print("Least expensive product:", format(least_expensive, ">10.2f"), " (", productmin,")", sep="")
        #total value
        #for loop with accumulator variable
        total=0
        for i in product_costs:
            #find number of inventory
            location=product_costs.index(i)
            inventory=product_inventory[location]
            total += (inventory*i)
        print("Total value of all products:", format(total, ".2f"))
    else:
        print ("Invalid option, try again")
    print()

print("See you soon!")
