#Anne Xie
#August 20, 2023
#Food Ordering Program 
#Based on https://plainenglish.io/blog/build-a-fast-food-order-taker-in-python-87188efcbbdd


menu = {"soju", "noodles", "rice", "pineapple bun", "milk tea", "katsu", "dumplings"}

def get_order():
    current_order = []
    while True:
        print("What would you like?")
        for item in menu:
            print(item)
        order = input()
        if order in menu:
            current_order.append(order)
        else:
            print ("I'm sorry we don't serve that")
        if order_complete():
            return current_order

def order_complete():
    print("Would you like anything else? (yes/no)")
    choice = input()
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        raise Exception("invalid response")

def final_order(current_order):
    print ("Okay, so your order is ")
    for order in current_order:
        print(order)

def main():
    order = get_order()
    final_order(order)


if __name__ == "__main__":
    main()