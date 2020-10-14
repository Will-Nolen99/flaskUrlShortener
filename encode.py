key = "abcdefghijkllmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~"
base = len(key)


def encode(modifier, id_num):
    
    num = id_num
    digits = []
    
    while num > 0:
        remainder = num % base
        digits.append(remainder)
        num = num // base
        
        
    shortened = ""
    
    for digit in digits:
        shortened += key[digit]
        
    print(shortened)
    
    return "http://127.0.0.1:5000/" + modifier + shortened