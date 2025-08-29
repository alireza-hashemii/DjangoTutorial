from . import jalali

def replace_numbers(text: str):
    nums = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for e, p in nums.items():
        text = text.replace(e, p)

    return text

def jalali_converter(time):
    jmonth = ["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","ابان","اذر","دی","بهمن","اسفند"]
    
    time_to_str = f"{time.year}.{time.month}.{time.day}"
    str_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(str_to_tuple)

    for index, month in enumerate(jmonth):
        if time_to_list[1] == index:
            time_to_list[1] = month
    
    output = f'{time_to_list[2]} {time_to_list[1]} {time_to_list[0]}'
    return replace_numbers(output)