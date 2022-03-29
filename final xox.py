 
from turtle import*
import turtle

square = turtle.Turtle()

square.width("5")

for i in range(4):
    square.forward(300)
    square.left(90)
for i in range (1,3):
    square.up()
    square.goto(0,i*100)
    square.down()
    square.fd(300)
square.lt(90)
for i in range(1,3):
    square.up()
    square.goto(i*100,0)
    square.down()
    square.fd(300)

    

list1=[1,3,5,7,9]
list2=[0,2,4,6,8]
player1 = []
player2 = []

square2=[200,200,200,200,200,200,200,200,200]
print(square2)

line1 = [1,2,3]
line2 = [4,5,6]
line3 = [7,8,9]
all_lines = [line1 , line2 , line3]



while True:
    while 200 in square2:
            
            
        First_player=int(input("player1 please enter your number: "))

        place=int(input("please enter your place: "))-1

        if First_player in list1:
        
            if square2[place]==200:

            
                player1.append(First_player)
                print("your numbers are:",player1)
                list1.remove(First_player)
                square2.pop(place)
                square2.insert(place,First_player)
                
                print(square2)

                

                if place+1 in line1 :
                    a = 0
                    for i in range(3) :
                        if line1[i] == place+1:
                                break

                if place+1 in line2 :
                    a = 1
                    for i in range(3) :
                        if line2[i] == place+1:
                                    break

                if place+1 in line3 :
                    a = 2
                    for i in range(3) :
                        if line3[i] == place+1:
                                    break

                square.up()
                square.goto(i*100 + 30,-a*100+230)
                square.down()
                square.write(First_player , font=("calibri" , 40 , "bold"))

                if square2[0]+  square2[1]+ square2[2]==15:
                    print(" Player1 is winner")
                    break
                elif square2[3]+square2[4]+square2[5]==15:
                    print(" Player1 is winner")
                    break
                elif square2[6]+square2[7]+square2[8]==15:
                    print(" Player1 is winner")
                    break
                elif square2[0]+square2[3]+square2[6]==15:
                    print(" Player1 is winner")
                    break
                elif square2[1]+square2[4]+square2[7]==15:
                    print(" Player1 is winner")
                    break
                elif square2[2]+square2[5]+square2[8]==15:
                    print(" Player1 is winner")
                    break
                elif square2[0]+square2[4]+square2[8]==15:
                    print(" Player1 is winner")
                    break
                elif square2[2]+square2[4]+square2[6]==15:
                    print(" Player1 is winner")
                    break




            else:
                place2=int(input("please enter a valid place: "))-1
                square2.pop(place2)

                square2.insert(place2,First_player)
                print(square2)  




                if place2+1 in line1 :
                    a = 0
                    for i in range(3) :
                        if line1[i] == place2+1:
                         break

                if place2+1 in line2 :
                    a = 1
                    for i in range(3) :
                        if line2[i] == place2+1:
                            break

                if place2+1 in line3 :
                    a = 2
                    for i in range(3) :
                        if line3[i] == place2+1:
                            break

                square.up()
                square.goto(i*100 + 30,-a*100+230)
                square.down()
                square.write(First_player , font=("calibri" , 40 , "bold"))

                if square2[0]+  square2[1]+ square2[2]==15:
                    print(" Player1 is winner")
                    break
                elif square2[3]+square2[4]+square2[5]==15:
                    print(" Player1 is winner")
                    break
                elif square2[6]+square2[7]+square2[8]==15:
                    print(" Player1 is winner")
                    break
                elif square2[0]+square2[3]+square2[6]==15:
                    print(" Player1 is winner")
                    break
                elif square2[1]+square2[4]+square2[7]==15:
                    print(" Player1 is winner")
                    break
                elif square2[2]+square2[5]+square2[8]==15:
                    print(" Player1 is winner")
                    break
                elif square2[0]+square2[4]+square2[8]==15:
                    print(" Player1 is winner")
                    break
                elif square2[2]+square2[4]+square2[6]==15:
                    print(" Player1 is winner")
                    break
                    
                    
        else:
            x=int(input("please enter another odd number"))
            place=int(input("please enter your place: "))-1
            player1.append(x)
            print("your numbers are:",player1)
            list1.remove(x)
            square2.pop(place)
            square2.insert(place,x)
            
            print(square2)


            if place+1 in line1 :
                a = 0
                for i in range(3) :
                    if line1[i] == place+1:
                     break

            if place+1 in line2 :
                a = 1
                for i in range(3) :
                    if line2[i] == place+1:
                        break

            if place+1 in line3 :
                a = 2
                for i in range(3) :
                    if line3[i] == place+1:
                        break

            square.up()
            square.goto(i*100 + 30,-a*100+230)
            square.down()
            square.write(x , font=("calibri" , 40 , "bold"))


            if square2[0]+  square2[1]+ square2[2]==15:
                print(" Player1 is winner")
                break
            elif square2[3]+square2[4]+square2[5]==15:
                print(" Player1 is winner")
                break
            elif square2[6]+square2[7]+square2[8]==15:
                print(" Player1 is winner")
                break
            elif square2[0]+square2[3]+square2[6]==15:
                print(" Player1 is winner")
                break
            elif square2[1]+square2[4]+square2[7]==15:
                print(" Player1 is winner")
                break
            elif square2[2]+square2[5]+square2[8]==15:
                print(" Player1is winner")
                break
            elif square2[0]+square2[4]+square2[8]==15:
                print(" Player1 is winner")
                break
            elif square2[2]+square2[4]+square2[6]==15:
                print(" Player1 is winner")
                break 

        second_player=int(input("player2 please enter your number: "))
        place=int(input("please enter your place: "))-1
        if second_player in list2:  

            if square2[place]==200:
                
                    player2.append(second_player)
                    print("your numbers are:",player2)
                    list2.remove(second_player)
                    square2.pop(place)
                    square2.insert(place,second_player)
                    print(square2)


                    if place+1 in line1 :
                        a = 0
                        for i in range(3) :
                            if line1[i] == place+1:
                                break

                    if place+1 in line2 :
                        a = 1
                        for i in range(3) :
                            if line2[i] == place+1:
                                break

                    if place+1 in line3 :
                        a = 2
                        for i in range(3) :
                            if line3[i] == place+1:
                                break

                    square.up()
                    square.goto(i*100 + 30,-a*100+230)
                    square.down()
                    square.write(second_player , font=("calibri" , 40 , "bold"))


                    if square2[0]+  square2[1]+ square2[2]==15:
                        print(" Player2 is winner")
                        break
                    elif square2[3]+ square2[4]+ square2[5]==15:
                        print(" Player2 is winner")
                        break
                    elif square2[6]+ square2[7]+ square2[8]==15:
                        print(" Player2 is winner")
                        break
                    elif square2[0]+ square2[3]+ square2[6]==15:
                        print(" Player2 is winner")
                        break
                    elif square2[1]+ square2[4]+ square2[7]==15:
                        print(" Player2 is winner")
                        break
                    elif square2[2]+ square2[5]+ square2[8]==15:
                        print(" Player2 is winner")
                        break
                    elif square2[0]+ square2[4]+ square2[8]==15:
                        print(" Player2 is winner")
                        break
                    elif square2[2]+ square2[4]+ square2[6]==15:
                        print(" Player2 is winner")
                        break
    
            else:
                place2=int(input("please enter a valid place: "))-1
                square2.pop(place2)
                square2.insert(place2,second_player)
                
                print(square2)

                

                if place2+1 in line1 :
                    a = 0
                    for i in range(3) :
                        if line1[i] == place2+1:
                            break

                if place2+1 in line2 :
                    a = 1
                    for i in range(3) :
                        if line2[i] == place2+1:
                            break

                if place2+1 in line3 :
                    a = 2
                    for i in range(3) :
                        if line3[i] == place2+1:
                            break

                square.up()
                square.goto(i*100 + 30,-a*100+230)
                square.down()
                square.write(second_player , font=("calibri" , 40 , "bold"))


                if square2[0]+  square2[1]+ square2[2]==15:
                    print(" Player2 is winner")
                    break
                elif square2[3]+square2[4]+square2[5]==15:
                    print(" Player2 is winner")
                    break
                elif square2[6]+square2[7]+square2[8]==15:
                    print(" Player2 is winner")
                    break
                elif square2[0]+square2[3]+square2[6]==15:
                    print(" Player2 is winner")
                    break
                elif square2[1]+square2[4]+square2[7]==15:
                    print(" Player2 is winner")
                    break
                elif square2[2]+square2[5]+square2[8]==15:
                    print(" Player2 is winner")
                    break
                elif square2[0]+square2[4]+square2[8]==15:
                    print(" Player2 is winner")
                    break
                elif square2[2]+square2[4]+square2[6]==15:
                    print(" Player2 is winner")
                    break                

        else:
            y=int(input("please enter another even number"))
            place=int(input("please enter your place: "))-1
            player2.append(y)
            print("your numbers are:",player2)
            list2.remove(y)
            square2.pop(place)
            square2.insert(place,y)
            print(square2)


            if place+1 in line1 :
                a = 0
                for i in range(3) :
                    if line1[i] == place+1:
                     break

            if place+1 in line2 :
                a = 1
                for i in range(3) :
                    if line2[i] == place+1:
                        break

            if place+1 in line3 :
                a = 2
                for i in range(3) :
                    if line3[i] == place+1:
                        break

            square.up()
            square.goto(i*100 + 30,-a*100+230)
            square.down()
            square.write(y , font=("calibri" , 40 , "bold"))    
                
                    
            if square2[0]+  square2[1]+ square2[2]==15:
                print(" Player2 is winner")
                break
            elif square2[3]+square2[4]+square2[5]==15:
                print(" Player2 is winner")
                break
            elif square2[6]+square2[7]+square2[8]==15:
                print(" Player2 is winner")
                break
            elif square2[0]+square2[3]+square2[6]==15:
                print(" Player2 is winner")
                break
            elif square2[1]+square2[4]+square2[7]==15:
                print(" Player2 is winner")
                break
            elif square2[2]+square2[5]+square2[8]==15:
                print(" Player2 is winner")
                break
            elif square2[0]+square2[4]+square2[8]==15:
                print(" Player2 is winner")
                break
            elif square2[2]+square2[4]+square2[6]==15:
                print(" Player2 is winner")
                break









    