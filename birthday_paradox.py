import random
# in a group of 23 people there's a 50% chance of a matching birthday
# list of dates?
# each month has 30,31 except feb=28 once every 4 years 29 if leap year
# leap year = divisible by 4 and years at end of century unless div by 400
def main():
    #birthdays = input("How many birthdays shall I generate?")
    birthdays = []
    for _ in range(int(input("How many birthdays shall I generate? "))):
        birthdays.append(generate_birthday())
    print(birthdays)



def generate_birthday():
    date = random.randint(0, 366)
    #print("test: ", date)
    months = {
        'january': range(0,32),
        'febuary': range(31,60),
        'march': range(59,91),
        'april': range(90,121),
        'may': range(120,152),
        'june': range(151,182),
        'july': range(181,212),
        'august': range(212,244),
        'september': range(243,274),
        'october': range(273,305),
        'november': range(304,335),
        'december': range(334,366),
        }
     # print key if value 
    for month, m in months.items():
        if date in range(0,32):
            return date, month
        elif date in m:
            fixed_date = date - m.start
            return fixed_date, month

main()
