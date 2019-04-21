def card_validator(str):
    length = "".join(str.split(" "))
    if str.startswith('4') and len(length) == 16:
        return "Visa"
    elif (str.startswith('37') or str.startswith('34')) and len(length) == 15:
        return "American Express"
    elif str.startswith('5') and len(length) == 16:
        ar = ['51', '52', '53', '54', '55']
        for i in ar:
            if str.startswith(i):
                return "Master"
    else:
        raise ValueError("Invalid Card Number")
