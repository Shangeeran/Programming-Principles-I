print("Let's encode and decode")
print("e-encode")
print("d-decode")
print("q-quit")
ask=input("Chosse your mode = ")
while ask!=0:
    if ask=="d":
        alphabet =  "abcdefghijklmnopqrstuvwxyz"
        text = str(input("Enter the text = ")) #input text
        shift = int(input("Shift Number = "))  #shift number
        decoded_text = ""
        for l in text:
            position = alphabet.find(l)
            if (position!=-1): #check position
                shifted_position = position - shift
                
                if (shifted_position > 25): #alphabet letters
                    shifted_position = (shifted_position-25)

                    
                shifted_letter = alphabet[shifted_position]
                decoded_text = decoded_text + shifted_letter
            else:
                decoded_text = decoded_text + l

        print("-----------------------------------------------------------------------")
        print("-----------------------------------------------------------------------")
        print("Please wait...........")
        print("Processing............")
        print("This is your encode - ",decoded_text)
        print("Thank you.....")
        print("-----------------------------------------------------------------------")
        print("-----------------------------------------------------------------------")
        ask=input("choose your mode = ")

    elif ask=="e":
        alphabet =  "abcdefghijklmnopqrstuvwxyz"
        text = str(input("Enter the text = ")) #input text
        shift = int(input("Shift Number = ")) #shift steps
        encoded_text = "" #receive the text
        for l in text:
            position = alphabet.find(l) #position
            if (position!=-1):
                shifted_position = position + shift
                if (shifted_position > 25): #because alphabet letters count
                    shifted_position = (shifted_position-26)
                    
                shifted_letter = alphabet[shifted_position]
                encoded_text = encoded_text + shifted_letter
            else:
                encoded_text = encoded_text + l
        print("-----------------------------------------------------------------------")
        print("-----------------------------------------------------------------------")
        print("Please wait...........")
        print("Processing............")
        print("This is your encode - ",encoded_text)
        print("Thank you.....")
        print("-----------------------------------------------------------------------")
        print("-----------------------------------------------------------------------")
        ask=input("Choose the mode = ")


    elif ask=="q":
        print("You are quiting your program")
        break

print("Thank you........!")
        
    
