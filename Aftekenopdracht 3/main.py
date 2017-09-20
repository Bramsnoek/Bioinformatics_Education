from enum import IntEnum


class DayOfWeek(IntEnum):
    Monday = 1,
    Tuesday = 2,
    Wednesday = 3,
    Thursday = 4,
    Friday = 5,
    Saturday = 6,
    Sunday = 7


def print_day_of_week(day_of_week):
    try:
        print(DayOfWeek(int(day_of_week)))
    except ValueError:
        print('Please enter a valid day number')


def print_rectangles(l_w):
    area1 = l_w[0] * l_w[1]
    area2 = l_w[2] * l_w[3]

    if area1 > area2:
        print("The first area is bigger than the second")
        return

    print("The second area is bigger than the first")


def print_pocket(pocket_number, color_even, color_uneven):
    if pocket_number % 2 == 0:
        print("Pocketnumber {} is {}".format(str(pocket_number), color_even))
        return
    print("Pocketnumber {} is {}".format(str(pocket_number), color_uneven))


def print_color_pocket(pocket_number):
    if pocket_number > 36:
        print("Please enter a valid pocket number!")
        return

    if 0 < pocket_number <= 10:
        print_pocket(pocket_number, "black", "red")
    elif 10 < pocket_number <= 18:
        print_pocket(pocket_number, "red", "black")
    elif 19 < pocket_number <= 28:
        print_pocket(pocket_number, "black", "red")
    elif 29 < pocket_number <= 36:
        print_pocket(pocket_number, "red", "black")
    else:
        print("Pocketnumber {} is {}".format(str(pocket_number), "green"))


def main():
    number_of_day = input("What day number is it? ")
    print_day_of_week(number_of_day)

    l_w = [float(x.strip()) for x in input("What are the length and width of both (seperate each length/width by ,): ").split(',')]
    print_rectangles(l_w)

    pocket_number = input("What is the pocket number? ")
    print_color_pocket(int(pocket_number))


if __name__ == '__main__':
    main()
