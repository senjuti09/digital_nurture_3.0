salesamounts=[200,600,150,800,300]
def generate_reports(sales):
    total=0
    for i in sales:
        total=total+i
        if i>500:
            print(f'{i} (over 500)')
        else:
            print(i)
generate_reports(salesamounts)
        
