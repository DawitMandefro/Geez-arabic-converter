# arabic_to_geez.py

ONES = {
    1: "፩",
    2: "፪",
    3: "፫",
    4: "፬",
    5: "፭",
    6: "፮",
    7: "፯",
    8: "፰",
    9: "፱"
}

TENS = {
    10: "፲",
    20: "፳",
    30: "፴",
    40: "፵",
    50: "፶",
    60: "፷",
    70: "፸",
    80: "፹",
    90: "፺"
}


def convert_to_geez(number):
    if number <= 0:
        return "Only positive integers are supported."

    if number > 9999:
        return "Current implementation supports numbers up to 9,999."

    result = ""

    # Hundreds
    hundreds = number // 100

    if hundreds > 0:
        if hundreds > 1:
            result += ONES[hundreds]
        result += "፻"

    number %= 100

    # Tens
    tens = (number // 10) * 10

    if tens > 0:
        result += TENS[tens]

    # Ones
    ones = number % 10

    if ones > 0:
        result += ONES[ones]

    return result


if __name__ == "__main__":
    number = int(input("Enter an Arabic number: "))
    print("Geez Number:", convert_to_geez(number))
