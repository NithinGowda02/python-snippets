Pizza = input("Select your Pizza..L/M/S..>>")
bill=0
if Pizza == "L" or Pizza == "l":
    print("Price of Small Pizza is $300..")
    bill+=300
elif Pizza == "M" or Pizza == "m":  
    print("Price of Small Pizza is $200..")
    bill+=200
elif Pizza == "S" or Pizza == "s":  
    print("Price of Small Pizza is $100..")
    bill+=100   

pepporoni=input("Do you want pepperoni..(Y/N)")
if pepporoni =="Y"  or pepporoni =="y":
    if Pizza == "L" or Pizza == "l":
        print("$50 for pepporoni for Large Pizza...")  
        bill+=50 
    elif Pizza == "S" or Pizza == "s":  
        print("$30 for pepporoni for small Pizza...")
        bill+=30
    elif Pizza == "M" or Pizza == "m":  
        print("Price of medium Pizza is $40..")
        bill+=40
extra_cheese=input("Do you want Extra Cheese...(Y/N)") 
if extra_cheese == "Y"  or extra_cheese == "y":
    print("$20 for extra cheese...")   
    bill +=20
print(f"Total bill amount of your PIZZA.....${bill}")             

