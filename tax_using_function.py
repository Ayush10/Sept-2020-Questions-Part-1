# Program for the Inland Revenue Department (IRD) named Integrated Tax System(ITS)
# Taking user input
def person():
    print("""
                            Inland Revenue Department
                        Welcome to Integrated Tax System
    """)
    name = input("Enter your name: ")
    address = input("Address: ")
    married_status = input("Enter 'Y' for Married and 'N' for Unmarried: ")
    pan_no = int(input("Enter your PAN No.: "))
    monthly_income = int(input("Enter your monthly income: "))
    annual_income = monthly_income * 12

    information = [name, address, married_status, pan_no, monthly_income, annual_income]

    return information


# Function that is called if the person is married
def married(income):
    total = 450000
    tax_rate = 0
    rate = 0
    extra_income = 0
    if income <= total:
        tax_rate = 1
    elif total < income <= total + 100000:
        rate = 10
        extra_income = 100000
    elif total + 100000 < income <= total + 200000:
        rate = 20
        extra_income = 200000
    elif (total + 200000 < income <= total + 1250000) or (total + 200000 < income < total + 2000000):
        rate = 30
        extra_income = 1250000
    elif income > total + 1300000 and income >= total + 2000000:
        rate = 36
        extra_income = 2000000

    tax = ((tax_rate / 100) * income) + ((rate / 100) * extra_income)
    return [rate, tax]


# Function that is called if the person is unmarried
def unmarried(income):
    total = 400000
    tax_rate = 0
    rate = 0
    extra_income = 0
    if income <= total:
        tax_rate = 1
    elif total < income <= total + 100000:
        rate = 10
        extra_income = income - total
    elif total + 100000 < income <= total + 200000:
        rate = 20
        extra_income = income - total + 100000
    elif (total + 200000 < income <= total + 1300000) or (total + 200000 < income < total + 2000000):
        rate = 30
        extra_income = income - total + 200000
    elif income > total + 1300000 and income >= total + 2000000:
        rate = 36
        extra_income = 2000000

    tax = ((tax_rate / 100) * income) + ((rate / 100) * extra_income)
    return [rate, tax]


# Temporary placeholder for use during printing
temp = 0


# Displaying the output in the specified format
def main(person):
    if person.married_status == 'Y':
        temp = married(person.annual_income)
    else:
        temp = unmarried(person.annual_income)

    print("""
                            Inland Revenue Department
                                Lazimpat, Kathmandu
                                    Welcome to 
                            Integrated Tax System
    Tax Payee: {0}                              Address: {1}
    PAN No: {2}             FY: 2020/2021       Married Status: {3}
    Tax Payee {0} with PAN {2} falls under (1 + {4})% Tax salb.
    {0} (PAN {2}) to pay tax to government is [Rs.] = {5}
    """.format(person.name, person.address, person.pan_no, person.married_status, str(temp[0]),
               str(temp[1])))

if __name__ == '__main__':
    main(person())