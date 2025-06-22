def main():
    time = input("What time is it now? ")
    new_time = convert(time)

    if 7 <= new_time <= 8 :
        print("breakfast time")
    elif 12 <= new_time <= 13:
        print("lunch time")
    elif 18 <= new_time <= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    time_list = time.split(":")
    hour = float(time_list[0])
    minutes = float(time_list[1])

    if minutes == 0:
        time = hour + 0.0
    if 1 <= minutes <= 10:
        time = hour + 0.1
    elif 11 <= minutes <= 15:
        time = hour + 0.25
    elif 16 <= minutes <= 20:
        time = hour + 0.3
    elif 21 <= minutes <= 25:
        time = hour + 0.4
    elif 26 <= minutes <=30:
        time = hour + 0.5
    elif 31 <= minutes <= 35:
        time = hour + 0.6
    elif 36 <= minutes <= 40:
        time = hour + 0.7
    elif 41 <= minutes <= 45:
        time = hour + 0.8
    elif 46 <= minutes <= 59:
        time = hour + 0.9
    return time

if __name__ == "__main__":
    main()
