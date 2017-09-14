from pprint import pprint


def print_personal_information():
    personal_information = \
        {
            'name': 'Bram Snoek',
            'address': 'Lithsedijk 33, 5397ea, Lith',
            'phone': '0636489308',
            'college major': 'Bioinformatics'
        }

    print("\n My name is {}, my address is {}, my phone number is {} and my college major is {}".format(personal_information['name'],
                                                                                                     personal_information['address'],
                                                                                                     personal_information['phone'],
                                                                                                     personal_information['college major']))


def print_sales_prediction(sales_prediction: int):
    print("Projected amount of sales after multiplication: {0} \n".format(str(0.23 * sales_prediction)))


def print_total_purchase(prices: list):
    total_amount = sum(prices)

    print("Subtotal: ${} \n Amount of sales tax: ${} \n Total amount: ${} \n".format(str(total_amount),
                                                                                     str(round(total_amount * 0.07, 2)),
                                                                                     str(round(total_amount * 1.07, 2))))


def print_distance_drive(speed: int, hours: list):
    for hour in hours:
        print("Distance driven: {} ".format(str(speed * hour)))

    print('\n')


def print_price_per_gallon(mpg_info: list):
    mpg = round(mpg_info[0] / mpg_info[1], 2)
    print("Your mpg value is: {} \n".format(str(mpg)))


def print_how_many_cookies(num_cookies: int, cups_sugar: float, cups_butter: float, cups_flour: float, makeable_cookies: int):
    cookies_ratio = num_cookies / makeable_cookies
    print("You'll need {} cups of sugar, {} cups of butter and {} cups of flour".format(str(round(cups_sugar * cookies_ratio, 2)),
                                                                                        str(round(cups_butter * cookies_ratio, 2)),
                                                                                        str(round(cups_flour * cookies_ratio, 2))))


def main():
    sales_prediction = input("What is your projected amount of sales? ")
    print_sales_prediction(int(sales_prediction))

    prices = [float(x.strip()) for x in input("What are your prices (seperate each price by ,): ").split(',')]
    print_total_purchase(prices)

    print_distance_drive(70, [6, 10, 15])

    mpg = [float(x.strip()) for x in input("How many miles have you driven and how much gallons of gas has been used (seperate by ,)").split(',')]
    print_price_per_gallon(mpg)

    num_cookies = int(input("How many cookies do you want to make?"))
    print_how_many_cookies(num_cookies, 1.5, 1, 2.75, 48)

    print_personal_information()


if __name__ == '__main__':
    main()