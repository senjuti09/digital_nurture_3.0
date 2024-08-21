customer_data={'Alice': 120, 'Bob': 75, 'Charlie': 90}
def update_purchase(customer_data,name,amount):
    if name in customer_data:
        customer_data[name]=amount
        print('Updated data:')
        print(customer_data)
    else:
        print('customer not found')
update_purchase(customer_data,'Bob',100)
