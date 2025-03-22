#importing library

import pandas as pd   

#initialising variables

cust_name = '' 
cust_number = ''
cust_address = ''
cust_email = ''
user = -1 #To store user input 
df = pd.DataFrame() #Stores csv file as dataframe
count = -1 #Counts number of iterations
cat = -1 
dic = {"Item code" : [],	"Item" : [], "Net Wt./Vol." : [],	'Rate' : [],	'Category Name' : [],	'Category' : []}
bill = pd.DataFrame(dic) #Stores bill

print("Greetings! And a warm Welcome to KuroMart!!")

for k in range(1,100):
    print('What are you planning to do today?')
    user = int(input('1} Fill customer details\n2} Display customer details\n3} Shop\n4} Remove items from cart\n5} Show bill\n6} Checkout\n\nEnter number:'))
    
    if user == 1:
        print("Enter customer details:") #accepts user details from user
        cust_name = input('Name:')
        cust_number = input('Contact Number: ')
        cust_address = input('Address: ') 
        cust_email = input('Email ID: ')
        
    elif user == 2:
        print("\tCUSTOMER DETAILS\t")  #displays all the customer details
        print('Name:', cust_name)
        print('Contact Details:', cust_number)
        print('Address:', cust_address)
        print('Email ID:', cust_email)
        
    elif user == 3:
        print("\nWhat would you like to buy today?\n") 
        df = pd.read_csv("C:\\Users\\AARYAL\\OneDrive\\Desktop\\Aaryan\\hmm\\CSV File.csv")                                                        #check csv
        count = 0
        for i in range(1, 51) :
            for j,row in df.iterrows():
                if j < 8:
                    print(j + 1, row["Category"])
            cat = int(input("\nEnter category(enter 0 if you want to stop shopping): "))
            if cat == 0:
                break;
            else:
                start = 4 * (cat - 1) + (cat - 1)  #establishing a relationship between category entered by user and rows in csv
                ends = start + 5
                df2 = df[start : ends]
                print(df2['Item'])
                item = int(input("\nWhat item do you want? \n"))
                if (not(item >= start) & (item < ends)):
                    print("\nWrong item number selected! Please try again!")
                else:
                    bill.loc[count] = df.loc[item]
                    print("\nItem added to cart successfully!\n")
                    count = count + 1
                if(count == 50):
                    print("\nSorry! You can only buy 50 items at a time!") #main loop ends here
         
    elif user == 4:
        print(bill.loc[:]['Item'])
        delete = int(input('Which item do you want to delete?(enter serial number):'))
        bill.drop(delete, inplace = True)
         
    elif user == 5:
        print("\tCUSTOMER DETAILS\t") #displays bill
        print('Name:', cust_name) 
        print('Contact Details:', cust_number)
        print('Address:', cust_address)
        print('Email ID:', cust_email)
        print("\t BILL \t")
        print(bill.loc[:][['Item', 'Rate']])
        print("\t~~~~~~~~~~~~~~~~~~\t")
        print("You have to pay:", sum(bill.loc[:]['Rate']), "(No Tax Applicable)")
         
    elif user ==6:
        print("\t BILL \t")  #checkout
        print(bill.loc[:][['Item', 'Rate']])
        print("\t~~~~~~~~~~~~~~~~~~\t")
        print("You have to pay:", sum(bill.loc[:]['Rate']), "(No Tax Applicable)")
        pay_mode = input("How would you like to pay?(enter c for cash, d for card and u for UPI):")
        if pay_mode == 'c' or pay_mode == 'C':
            print("Please proceed to the counter to pay.")
        elif pay_mode == 'd' or pay_mode == 'D':
            print('Please swipe card')
            password = input("Enter pin: ")
        elif pay_mode == 'u' or pay_mode == 'U':
            print('Please scan QR code here or pay to the number 8699800406')
        else:
            print('Invalid input. Please try again.') #To be safe from getting an error
        break
    
    else:
       print('Invalid input! Please try again')
print("Thank you for shopping with us. Do visit soon!")

