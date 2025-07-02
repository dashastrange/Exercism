months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date_input = input("Date: ")
    cleaned_date = date_input.title().replace(",", "").strip()

#divide date on chunks
    if "/" in cleaned_date:
        date_list = cleaned_date.split("/")
        if date_list[0].isalpha():
            continue
    else:
        date_list = cleaned_date.split(" ")

#year is always the last
    year = date_list[2]

# if second place is literal month -- exit the loop
    if date_list[1].isalpha():
        continue

#if first place is literal month -- assign places to month and day
    if date_list[0] in months and "," in date_input:
        month = months.index(date_list[0])+1
        day = date_list[1]

        if int(day) > 31:
            continue

    elif date_list[0] in months and "," not in date_input:
        continue

    else:
        month = date_list[0]
        day = date_list[1]

        if int(month) > 12:
            continue
        if int(day) > 31:
            continue

    d = f'{int(day):02d}'
    m = f'{int(month):02d}'

    flipped_date = [str(year), m, d]
    new_date = "-".join(flipped_date)
    print(new_date)
    break
