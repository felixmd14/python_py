'''
SIMULATE A SALES AND OPERATIONS PLANNING USING THE ZER0-STOCK LEVEL STRATEGY.

PROGRAM ASKS USER TO ENTER:
1. AN INITIAL STOCK LEVEL FOR A PRODUCT
2. THE NUMBER OF MONTH(S) TO PLAN
3. THE PLANNED SALES QUANTITY FOR EACH MONTH
BASED ON THIS DATA, CALCULATE THE REQUIRED PRODUCTION QUANTITY AS FOLLOWS:
4. IF THE SALES QUANTITY IS SMALLER THAN THE STOCK LEVEL OF THE PREVIOUS MONTH, THE PRODUCTION QUANTITY IS 0
5. IF THE SALES QUANTITY IS LARGER THAN THE STOCK LEVEL OF THE PREVIOUS MONTH, THE PRODUCTION QUANTITY IS THE DIFFERENCE
'''

print()
print('HERE IS A SIMULATION OF SALES AND OPERATIONS PLANNING USING THE ZERO-STOCK LEVEL STRATEGY. \n___________________________________________________________________________________________ \n')

# PROGRAM ASKS USER TO ENTER:
# AN INITIAL STOCK LEVEL FOR A PRODUCT
initial_stock = int(input('Please enter an initial stock level: '))

# THE NUMBER OF MONTH(S) TO PLAN
initial_month = 1
months_to_plan = int(input('Please enter the number of month(s) to plan: '))

# THE PLANNED SALES QUANTITY FOR EACH MONTH
sales_quantity = []
while initial_month <= months_to_plan:
    monthly_sales_planned = int(input(f'Please enter the planned sales quantity for month {initial_month}: '))
    sales_quantity.append(monthly_sales_planned)
    initial_month += 1
    # prompts the user to input the planned sales quantity for each month till the last month to plan
    # inserts the planned sales quantity for each month into an empty list (sales_quantity)
print()
print(f'The list of the planned sales quantity for each month is: \n{sales_quantity} \n')

# BASED ON THIS DATA, CALCULATE THE REQUIRED PRODUCTION QUANTITY AS FOLLOWS:
# IF THE SALES QUANTITY IS SMALLER THAN THE STOCK LEVEL OF THE PREVIOUS MONTH, THE PRODUCTION QUANTITY IS 0
stock_list = []
stock_list.append(initial_stock) # inserts the initial stock into an empty list (stock_list)
product_quantity = []
index = 0

while sales_quantity[index] < stock_list[-1]:
    stock_list.append(stock_list[-1] - sales_quantity[index])
    product_quantity.append(0)
    index += 1
    # if current month stock level is larger than sales quantity of following month
    # following month stock level = current month stock level - sales quantity of following month
    # current month production cost is zero (0)
# if the condition is met, the while loop above calculates the stock levels and production quantities;
# and inserts them into the (stock_list) list and (production_quantity) list respectively
    if index == len(sales_quantity):
        break
    # after incrementing the counter, the if condition checks whether the incremented index is greater than the index of the last item in the sales_quantity list, i.e.(equal to the number of items in list)
    # while the incremented index exists within the sales_quantity list, the loop will run and the code will execute
    # if the incremented index is equal to the number of items in list, the loop will terminate
print(f'The list of production quantities where sales quantity is smaller than the stock level of previous months is: \n{product_quantity} \n')
print(f'The list of stock level(s) larger than the sales quantity of the next month(s) starting with the initial stock to the resulting stock of the following month(s) where the resulting production quantity is 0 is: \n{stock_list}')
print()

# IF THE SALES QUANTITY IS LARGER THAN THE STOCK LEVEL OF THE PREVIOUS MONTH, THE PRODUCTION QUANTITY IS THE DIFFERENCE
while sales_quantity[index] > stock_list[-1]:
    stock_list.append(0)
    product_quantity.append(sales_quantity[index] - stock_list[-1])
    index += 1
    # if current month stock level is smaller than sales quantity of following month
    # following month stock level is zero (0)
    # current month production cost = sales quantity of following month - current month stock level
# if the condition is met, the while loop above calculates the stock levels and production quantities;
# and inserts them into the (stock_list) list and (production_quantity) list respectively
    if index == len(sales_quantity):
        del stock_list[0] # removes the initial stock from the stock_list
        break
print(f'The list of the resulting stock levels, not including the initial stock, of the of each month till the last month to plan, is: \n{stock_list} \n')
print(f'The list of production quantities of each month, starting with the first to the last month to plan; where production quantity is 0 if the sales quantity is smaller than the stock level of the previous month and the difference of the sales quantity and the stock level of the previous month otherwise, is: \n{product_quantity}')

print(' \n________________________________________________________________________________________________________________________________ \n')