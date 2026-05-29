def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (letters(s) == True and maxL(s) == True and number(s) == True and formaT(s) == True):
        return True
    else:
        return False
   
def letters(s):
    if (len(s)<2):
        return False
    if (s[0].isalpha() == True and s[1].isalpha() == True):
        return True

def maxL(s):
    if (2 <= len(s) <= 6):
        return True

def number(s):
    if (zeroes(s) == True and middledigits(s) == True):
        return True
    
def zeroes(s):
    
    for i in s:
        if (i.isdigit()==True):
            if (i == "0"):
                return False
            else:
                return True
    return True
        

def middledigits(s):
    found_digit = False
    for i in s:
        if (i.isdigit()==True):
            found_digit=True
        elif (found_digit==True):
            return False
    return True

def formaT(s):
    for i in s:
        if (i.isdigit()==False and i.isalpha()==False):
            return False
    return True


    

main()