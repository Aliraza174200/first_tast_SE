# Ali raza
# NIM - BSCS - 2021 -09

'''In this file i am going to build the calculator with the basic functionality such that (+,-,*,/,%)'''

def calculator():
    NUM1 =  int(input("Enter the 1st number: "))
    NUM2 =  int(input("Enter the 2nd number: "))
    oper =  str(input("Enter the operation \n1.Add \n2.Subtract \n3.Multiply \n4.Divide \n5.Modulas   : ")).lower()
    #hello
    if oper == "add" :
        add_res = NUM1 + NUM2
        print(f"The result of the addition of {NUM1} and {NUM2} is :",add_res)
    elif oper == "subtract" :
        sub_res = NUM1 - NUM2
        print(f"The result of the subtraction of {NUM1} and {NUM2} is :",sub_res)
    elif oper == "multiply" :
        mul_res = NUM1 * NUM2
        print(f"The result of the multiplication of {NUM1} and {NUM2} is :",mul_res)
    elif oper == "divide" :
        div_res = NUM1 / NUM2
        print(f"The result of the division of {NUM1} and {NUM2} is :",div_res)
    elif oper == "modulas" :
        mod_res = NUM1 % NUM2
        print(f"The result of the modulas of {NUM1} and {NUM2} is :",mod_res)
    
    
calculator() 


    
    
    
    


