#function to find biggest number

def fn_big(num_list):
    big=max(num_list)
    return big

#function to find the grnder 

def fn_gen(gender):
    gender=gender.lower()
    if gender=="m":
        return "Male"
    elif gender=="f":
        return "Female"
    else:
        return "Others"
    return gender

#function to find the prime number or not

def fn_prime(num):
    if num<2:
        print("its not a prime number")
    else:
        for i in range(2,num):
            if num%i==0:
                return "Its not a prime number"
                break
        else:
            return "its a prime number"
    return num
