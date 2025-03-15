alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
def encryption(plain_text,shift):
    caesar_text=''
    for char in user_choice:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position+shift)%26
            caesar_text+=alphabets[new_position]
        else:
            caesar_text+=char
    print(f"Text after encryption >>{caesar_text}")      

def decryption(cipher_text,shift):
    caesar_text=''
    for char in user_choice:
        if char in alphabets:
            position=alphabets.index(char)
            new_position=(position-shift)%26
            caesar_text+=alphabets[new_position]
        else:
            caesar_text+=char
    print(f"Text after decryption >>{caesar_text}") 
game_end=False
while not game_end:       
    choice=input("Type 'encrypt' for encryption and 'decrypt' for discription >> ")
    user_choice=input("Enter the word that you want to encrypt or decrypt >> ").lower()
    shift=int(input("Enter number of shift >> "))
    if choice=='encrypt':
        encryption(plain_text=user_choice,shift=shift)
    elif choice=='decrypt':
        decryption(cipher_text=user_choice,shift=shift)
    play_again=input("type 'yes' to continue 'no' to end.. >> ").lower()  
    if play_again=="yes":
        game_end
    elif play_again=="no" :
        game_end=True
    else:
        print("invalid input ..")       

