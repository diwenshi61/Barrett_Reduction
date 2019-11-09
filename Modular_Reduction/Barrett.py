def check_power_of_two(n):
    return (not (n & (n-1))) and n

if __name__ == "__main__":
    print("c = a mod b")
    try:
        a_size = int(raw_input("Size in bits of a: "))
    except ValueError:
        print("Error, try again")
        try:
            a_size = int(raw_input("Size in bits of a: "))
        except:
            print("An error occurred in the input")
            quit()
    try:
        b = int(raw_input("Value of b: "))
    except ValueError:
        print("Error, try again")
        try:
            b = int(raw_input("Value of b: "))
        except:
            print("An error occurred in the input")
            quit()
    if a_size < 1 or b < 1:
        print("Error: Values must be positive integers")
        quit()
    if check_power_of_two(b):
        print("Error: b must not be a power of two")
        quit()
    b_size = b.bit_length()
    max_error = -a_size
    
