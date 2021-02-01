# Program for the Inland Revenue Department (IRD) named Integrated Tax System(ITS) for multiple users
# Taking user input
def choice():
    print("""
                                Inland Revenue Department
                            Welcome to Integrated Tax System
        """)
    number_of_users = int(input("Enter the number of users: "))
    people = []
    for n in range(number_of_users):
        print("For user {0}".format(n))
        people.append(person())

    for n in people:
        main(n)


def person():
    name = print("Enter name: ")
    address = print("Enter address: ")
    married_status = input("Enter 'Y' for Married and 'N' for Unmarried: ").upper()
    pan_no = int(input("Enter PAN No.: "))
    monthly_income = int(input("Enter Monthly Income: "))
    annual_income = monthly_income * 12
    information = {'name': name, 'address': address, 'married_status': married_status,
                   'pan_no': pan_no, 'monthly_income': monthly_income, 'annual_income': annual_income}

    return information


# Displaying the output in the specified format
def main(person):
    print(person)

    print("success")


choice()