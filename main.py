import products
import store

def start(store_object):
    while True:


        print("""Store Menu
    ----------
    1. List all products in store
    2. Show total amount in store
    3. Make an order
    4. Quit """)

        user_input = input("Please choose a number: ")
        if user_input == "1":

            for item in store_object.get_all_products():
                print(item.show())
        elif user_input == "2":
            print("The total amount in store is:",store_object.get_total_quantity())
        elif user_input == "3":
            print("Please place an order!")
            for idx, product in enumerate(store_object.get_all_products(), start = 1):
                print(f"{idx}. {product.show()}")
            product_input = int(input("Choose a product: "))
            quantity_input = int(input("Enter the number of items that you wish:"))
            if product_input >= 1 and product_input <=len(store_object.get_all_products()):
                product = store_object.get_all_products()[product_input - 1]
                total_price = store_object.order([(product,quantity_input)])
                print(f"The total price of the chosen products is {total_price}.")
        elif user_input == "4":
            print("Thank you and Goodbye!")
            break







    # setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)
start(best_buy)








