from . import jalali
from django.utils import timezone

def persian_numbers_converter(mystr):
    numbers= {
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

    for e,p in numbers.items():
        mystr = mystr.replace(e,p)
    return mystr


def jalali_converter(time):
    a1 = "فروردین"
    a2 = "اردیبهشت"
    a3 = "خرداد"
    a4 = "تیر"
    a5 = "مرداد"
    a6 = "شهریور"
    a7 = "مهر"
    a8 = "آبان"
    a9 = "آذر"
    a10 = "دی"
    a11 = "بهمن"
    a12 = "اسفند"
    jmonths = [a1, a2 ,a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]

    time_to_str = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break
    output = "{} {} {}, ساعت {}:{}".format(
        time_to_tuple[2],
        time_to_tuple[1],
        time_to_tuple[0],
        time.hour,
        time.minute,
    )
    return persian_numbers_converter(output)
