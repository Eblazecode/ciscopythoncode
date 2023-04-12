print(" WELCOME EXPENSE TRACKER {- _ -}")
amount = float(input(" ENTER THE TOTAL AMOUNT OF MONEY TO THE MARKET"))
VAT = 0.01
acc_balance = 0
def expense_tracker():
    expense_list = {}
    # KEY : VALUE PAIR
    no_itms = int(input("  HOW MANY THINGS DID YOU BUY ..?"))
    for i in range(no_itms):
        itms = input(" WHAT DID YOU BUY ?")
        cost_itms = float(input(" WHAT IS THE COST "))
        expense_list.update({
            itms:cost_itms
        })
    for x in expense_list.values():
        total_exp = 0
        total_exp +=x

    acc_balance =  amount - total_exp*VAT

    return acc_balance

x = expense_tracker()
def compound_int():
    comp_int = x * (1.05) **5
    return  comp_int

print(" COMPOUND INT", compound_int())


