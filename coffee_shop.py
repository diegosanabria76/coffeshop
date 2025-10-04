MENU = { "espresso" : {
	"ingredients":{
		"water":100,
		"coffee":120,
		},
   	 "cost":1.5,
	},
 	"latte" : { 
        	"ingredients":{
                "water":100,
                "coffee":120,
		"milk": 80,
                },
         "cost":2.5,
        },
 	"capuccino" : { 
        	"ingredients":{
                "water":100,
                "coffee":120,
		"milk":50,
                },
         "cost":4.7,
        }
}

profit = 0

resources = {
	"water" :5000,
	"milk":1000,
	"coffee":15000,
	}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry there is not enough {item}.")
            return false
    return True



def process_coins():
    print("Please insert coins")
    total = int(input("how many quarters ? ")) *0.25
    total += int(input("how many dimes ? ")) *0.1
    total += int(input("how many nickels ? ")) *0.05
    total += int(input("how many pennies ? ")) *0.01
    return total


def is_transaction_succesfull(money_received, drink_cost):
    if money_received >= drink_cost:
        change =  round(money_received- drink_cost,2)
        print(f"Here is $ {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money, money refounded!!!")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"here is yout drink {drink_name}, enjoy!!!!")


is_on = True
while is_on:
    choice = input("what would you like?  (espresso, latte, capuccino):")
    if choice =="off":
        is_on = False
    elif choice == "report":
        print(f"Water:  {resources['water']}ml ")
        print(f"Milk:  {resources['milk']}ml ")
        print(f"Coffee:  {resources['coffee']}ml ")
        print(f"Money: $ {profit}  Lukitas   ")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesfull(payment, drink["cost"]):
                make_coffee(choice,  drink["ingredients"])







