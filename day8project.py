import string
alphabets=list(string.ascii_lowercase)
userchoice=input("Type 'encode' to encode and 'decode' to decode:").lower()
if(userchoice!='decode' and userchoice!='encode'):
    print("Please enter a right option")
else:
    text=input("Type your message:").lower()
    shift=int(input("Enter the shift number:"))
    def encrypt(text2,shift2):
        cipher_text=""
        for letter in text2:
            shifted_pos=alphabets.index(letter)+shift2
            shifted_pos%=len(alphabets)
            cipher_text+=alphabets[shifted_pos]
        print(f"Encoded result is:{cipher_text}")
    def decode(text2,shift2):
        actual_text=""
        for letter in text2:
            actual_position=alphabets.index(letter)-shift2
            actual_position%=len(alphabets)
            actual_text+=alphabets[actual_position]
        print(f"Decoded text is {actual_text}")  
    if(userchoice=='encode'):
        encrypt(text,shift) 
    if(userchoice=='decode'):
        decode(text,shift)