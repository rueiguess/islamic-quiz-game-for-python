print("Welcome to my quiz game")

playing = input("Do you want to play? ")

if playing == 'yes' or playing == 'Yes':
    print("Great, let's play!")
else:
    exit()

score = 0

tries = [1,2,3]

for x in tries:

    answer = input("How many surahs are in the Quran? ")
    if answer == '114':
        print('Allahumma Barik, good job!')
        score += 1
        break;

    else:
        print('Are you sure?')
        print('Try again InshaAllah')

for x in tries:
    answer = input("How many juz are in the Quran? ")
    if answer == '30':
        print('Allahumma Barik, good job!')
        score += 1
        break;
    else:
        print('Are you sure?')
        print('Try again InshaAllah')
        
for x in tries:
    answer = input("What month comes before Ramadhan? ").lower()

    if answer == 'shaban':
        print('Allahumma Barik, good job!')
        score += 1
        break;

    else:
        print('Are you sure?')
        print('Try again InshaAllah')

for x in tries:
    answer = input("What is the name of our Beloved Prophet? ").lower()

    if answer == 'muhammad':
       print('Allahumma Barik, good job!')
       score += 1
       break;

    else:
        print('Are you sure?')
        print('Try again InshaAllah')

print('Allahumma barik, you got ' + str(score) + ' points! May Allah increase you in knowledge!')