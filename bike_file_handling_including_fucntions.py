# Program for the Inland Revenue Department (IRD) named Integrated Tax System(ITS)
# Taking user input
def customer_input():
    print("""
                        Department of Transport Management
                                Baneswor, Kathmandu
                        Welcome to DOTM Bike Renewal System
                                Fiscal Year 2020/21
    """)
    name = input("Customer Name: ")
    address = input("Customer Address: ")
    bike_cc = int(input("Customer Bike in cc: "))
    phone_number = input("Phone No.: ")
    tax_amount = checking_condition(bike_cc)
    main(name, address, bike_cc, phone_number, tax_amount)


def checking_condition(bike_cc):
    # Checking Condition
    if bike_cc <= 125:
        tax_amount = 2800
    elif 126 < bike_cc <= 160:
        tax_amount = 4500
    elif 161 < bike_cc <= 250:
        tax_amount = 5500
    elif 251 < bike_cc <= 400:
        tax_amount = 9000
    elif 501 < bike_cc <= 650:
        tax_amount = 20000
    else:
        tax_amount = 30000

    return tax_amount


def main(name, address, bike_cc, phone_number, tax_amount):
    name, address, bike_cc, phone_number, tax_amount = name, address, bike_cc, phone_number, tax_amount
    # Displaying the output
    print("""
                        Department of Transport Management
                                Baneswor, Kathmandu
                        Welcome to DOTM Bike Renewal System
                                Fiscal Year 2020/21
    Customer Name: {0}                     Address: {1}
    Customer Bike[cc]: {2}                 Phone No.: {3}
    {0} with {2} cc Bike has to pay Tax of [Rs.] = {4}
    """.format(name, address, str(bike_cc), phone_number, str(tax_amount)))


customer_input()

# f = open('bike.txt', 'w')
# f.write("""
#                     Department of Transport Management
#                             Baneswor, Kathmandu
#                     Welcome to DOTM Bike Renewal System
#                             Fiscal Year 2020/21
# Customer Name: {0}                     Address: {1}
# Customer Bike[cc]: {2}                 Phone No.: {3}
# {0} with {2} cc Bike has to pay Tax of [Rs.] = {4}
# """.format(name, address, str(bike_cc), phone_number, str(tax_amount)))
# f.close()
