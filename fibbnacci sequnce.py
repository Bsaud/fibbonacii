sequence=[0,1] #creates the first items on the Fibonacci sequence  

def Fibonacci ():
    new_num=int(sequence[-1])+int(sequence[-2]) #calculates the next number in the sequence
    while new_num < 25:  #checks if the next number in the sequence  smaller than 25 and goes through loop if true
        sequence.append(new_num) #appends the new number to the sequence  
        new_num=int(sequence[-1])+int(sequence[-2]) #calculates the next number in the sequence  
    return sequence #returns sequence  list

print(Fibonacci())
