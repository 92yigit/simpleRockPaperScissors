import random
pcScore=0
userScore=0




while True:
    pcnumber = random.randint(1, 3)
    firstnumber = int(input('what is ur first number'))
    if pcnumber==firstnumber:
        print('berabere')
    elif pcnumber==1 and firstnumber==2:
        firstnumber=firstnumber+1

    elif pcnumber==1 and firstnumber==3:
        pcScore+=1
    elif pcnumber==2 and firstnumber==1:
        pcScore+=1
    elif pcnumber==2 and firstnumber==3:
        userScore+=1
    elif pcnumber==3 and firstnumber==1:
        userScore+=1
    elif pcnumber==3 and firstnumber==2:
        pcScore+=1
    print(userScore,pcScore,pcnumber,firstnumber)

    if pcScore==3 or userScore==3:
        print(userScore,pcScore)
        break

