print("Welcome to my quiz game")

playing = input("Do you want to play? ")

if playing == 'yes' or playing == 'Yes':
    print("Great, let's play!")
else:
    exit()

tries = [1,2,3]

for x in tries:

    answer = input("How many surahs are in the Quran? ")

    if answer == '114':
        print('Allahumma Barik, good job!')
        break;

    else:
        print('Are you sure?')
        print('Try again InshaAllah')

for x in tries:

    answer = input("How many juz are in the Quran?")

    if answer == '30':
        print('Allahumma Barik, good job!')
        break;

    else:
        print('Are you sure?')
        print('Try again InshaAllah')
        
for x in tries:

    answer = input("What month comes before Ramadhan?")

    if answer == 'Shaban':
        print('Allahumma Barik, good job!')
        break;

    else:
        print('Are you sure?')
        print('Try again InshaAllah')

for x in tries:
    answer = input("What is the name of our Beloved Prophet?")

    if answer == 'Muhammad':
       print('Allahumma Barik, good job!')
       break;

    else:
        print('Are you sure?')
        print('Try again InshaAllah')

for x in tries:
    answer = input("")