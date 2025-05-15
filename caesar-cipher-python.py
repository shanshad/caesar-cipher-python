alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']


def encrypt(n,*word):
    encrypted=[]
    for char in word:
        if char not in alphabet:
              encrypted.append(char) 
        for i,j in enumerate(alphabet):
            if char==j:
                k=(i+n)%26
                encrypted.append(alphabet[k])
            
    print(f"Your encrypted word is : {''.join(encrypted)}")

def decrypt(n,*word):
    decrypted=[]
    for char in word:
        if char not in alphabet:
              decrypted.append(char) 
        for i,j in enumerate(alphabet):
            if char==j:
                k=(i-n)%26
                decrypted.append(alphabet[k])
    print(f"Your decrypted word is : {''.join(decrypted)}")

l=0
while l==0:
    choice=input("Do you want to encrypt or decrypt : ").lower()
    
    if choice=='encrypt' :
        word=list(input("Enter the word you want to encrypt : ").lower())
        n=int(input("enter key number : "))
        encrypt(n,*word)
    elif choice=='decrypt':
        word=list(input("Enter the word you want to decrypt : ").lower())
        n=int(input("enter key number : "))
        decrypt(n,*word)
    else:
        print("Invalid input!")
        exit()
    print("\n")
    l=int(input("Enter 0 to loop and 1 to exit : "))
    print("\n")