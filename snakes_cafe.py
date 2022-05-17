intro = '''
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
'''
prompt = """
***********************************
** What would you like to order? **
***********************************
"""

Menu={
    "Appetizers": ['Wings', 'Cookies', 'Spring Rolls'],
    "Entrees": ['Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden'],
    "Dessert": ['Ice Cream', 'Cake', 'Pie'],
    "Drinks": ['Coffee', 'Tea', 'Unicorn Tears']
}
allItems =[]
order=[]

def display_menu():
    print(intro);
    for menu in Menu:
        print(menu)
        print("-" *6)
        for item in Menu[menu]:
            print(item)
            allItems.append(item.lower())
display_menu()
def user_order():
    print(prompt)
    user_input = input("> ")
    for menu in Menu:
        output = user_input.title()
        if output in Menu[menu]:
            print('That is on the Menu added ', output, ' into your cart ')
            order.append(output);
            print('Cart: ', order);
        else:
            print('Sorry that is not in the menu')
        if user_input.lower().startswith("q"):
            print('This is what you ordered: ', order)
            import sys
            sys.exit('Thank for visiting Snakes Cafe')
        break
while True:
    user_order()
