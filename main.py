import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




#Defined function
def caesar(text,shift,direction):
  
  end_text = ''
  if direction == 'decode':
    shift *= -1;
  for letter in text:
    if letter in alphabet:
      letter = alphabet[alphabet.index(letter)+shift]
      end_text = end_text + letter
    else :
      end_text += letter

  print(f"The {direction}d text is {end_text}.")
  
  
    
  




# def encrypt(text,shift):
  
#   cipher_text =''
#   for letter in text:
#     letter = alphabet[alphabet.index(letter)+shift]
#     cipher_text = cipher_text + letter
#   print(f"Encoded text is {cipher_text}.")


# def decrypt(text,shift):
  
#   plain_text =''
#   for letter in text:
#     letter = alphabet[(alphabet.index(letter))-shift]
#     plain_text = plain_text + letter
#   print(f"Decoded text is {plain_text}.")

# #Calling functions
# if direction == 'encode':
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   encrypt(text,shift)
# elif direction == 'decode':
#   text = input("Type your message:\n").lower()
#   shift = int(input("Type the shift number:\n"))
#   decrypt(text,shift)
# else:
#   print('OOPS!! INVALID!!')
restart = True
while restart:
  
  
  
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26 :
    shift = round(shift % 26)
  
  
  caesar(text,shift,direction)
  n = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if n == 'no':
    restart = False
    print('Good Bye!')