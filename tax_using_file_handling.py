# Program for the Inland Revenue Department (IRD) named Integrated Tax System(ITS)
# Taking user input
def customer_input():
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
    rate, tax_calculated = tax_calculation(married_status, annual_income)
    customer_output(name, address, married_status, pan_no, annual_income, rate, tax_calculated)


def tax_calculation(married_status, annual_income):
    married_status, annual_income = married_status, annual_income

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

    # Condition that checks if the person is married or not
    if married_status == 'Y' or married_status == 'y':
        return married(annual_income)
    else:
        return unmarried(annual_income)


def customer_output(name, address, married_status, pan_no, annual_income, rate, tax_calculated):
    name, address, married_status, pan_no, annual_income, rate, tax_calculated = name, address, married_status, pan_no, annual_income, rate, tax_calculated
    # Displaying the output in the specified format
    print("""
                            Inland Revenue Department
                                Lazimpat, Kathmandu
                                    Welcome to 
                            Integrated Tax System
    Tax Payee: {0}                              Address: {1}
    PAN No: {2}             FY: 2020/2021       Married Status: {3}
    Tax Payee {0} with PAN {2} falls under (1 + {4})% Tax salb.
    {0} (PAN {2}) to pay tax to government is [Rs.] = {5}
    """.format(name, address, pan_no, married_status, str(rate), str(tax_calculated)))
