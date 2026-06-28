
# geez_to_arabic.py

VALUES = {
    "፩": 1,
    "፪": 2,
    "፫": 3,
    "፬": 4,
    "፭": 5,
    "፮": 6,
    "፯": 7,
    "፰": 8,
    "፱": 9,
    "፲": 10,
    "፳": 20,
    "፴": 30,
    "፵": 40,
    "፶": 50,
    "፷": 60,
    "፸": 70,
    "፹": 80,
    "፺": 90
}


def convert_to_arabic(geez):
    total = 0
    current = 0

    for symbol in geez:

        if symbol == "፻":
            if current == 0:
                current = 1
            total += current * 100
            current = 0

        elif symbol in VALUES:
            current += VALUES[symbol]

        else:
            return "Invalid Geez numeral."

    total += current

    return total


if __name__ == "__main__":
    geez = input("Enter a Geez number: ")
    print("Arabic Number:", convert_to_arabic(geez))
