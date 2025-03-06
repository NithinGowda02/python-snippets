import random
char_generator=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z','A',
                'B','C','D','E','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']

Numbers=['0','1','2','3','4','5','6','7','8','9']

Symbols=['!','@','#','$','%','^','&','*','(',')','-','+','+']

char=int(input("How many number of characters do you want... >> "))
num=int(input("How many number of Integers do you want... >> "))
sym=int(input("How many number of symbols do you want..."))
password=[]
for _ in range(1,char+1):
    pass_char=random.choice(char_generator)
    password+=pass_char
for _ in range(1,num+1):
    pass_num=random.choice(Numbers)
    password+=pass_num 
for _ in range(1,sym+1):
    pass_sym=random.choice(Symbols)
    password+=pass_sym
random.shuffle(password)    

final_password=""
for i in password:
    final_password+=i
print(f"Your Strong Password >> \n {final_password}")    