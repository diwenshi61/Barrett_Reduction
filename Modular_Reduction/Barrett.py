def check_power_of_two(n):
    return (not (n & (n-1))) and n

def find_inverse(n, max_error):
    i = 1
    digits_found = 0
    inverse = ""
    numerator = 1
    denominator = n
    while digits_found < -max_error:
        if (2 ** i) * numerator > denominator:
            inverse += "1"
            numerator = numerator * (2 ** i ) - denominator
            denominator = denominator * (2 ** i)
        else:
            inverse += "0"
        digits_found += 1
        i += 1
    return inverse

def write_multiplier_floor(inv_b, a_size):
    name = "multiplier_by_" + inv_b
    io = "a  :  in unsigned (" + str(a_size - 1) + " downto 0);\n    "\
         + "a_inv_b  :  out unsigned (" + str(a_size - 1) + " downto 0)"
    signal_comps = "  signal mult_result  :  unsigned (" + str(a_size + len(inv_b) - 1) + " downto 0);\n"
    process = "mult_result <= a * \"" + inv_b + "\";\n"\
              + "process(clk)\nbegin\n  if rising_edge(clk) then\n    "\
              + "a_inv_b <= mult_result(" + str(a_size + len(inv_b) - 1) + " downto "\
              + str(a_size) + ");\n  end if;\nend process;"
    f = open("template.txt", "r")
    lines = ""
    for line in f:
        lines += line.replace("[1]", name).replace("[2]", io).replace("[3]", signal_comps).replace("[4]", process)
    f.close()
    f = open(name + ".vhd", "w")
    f.write(lines)

def write_multiplier(b, b_size, a_size):
    name = "multiplier_" + str(a_size) + "bits_by_" + str(b)
    io = "a_inv_b_floor  :  in unsigned (" + str(a_size - 1) + " downto 0);\n    "\
         + "b_a_inv_b_floor  :  out unsigned (" + str(a_size - 1) + " downto 0)\n"
    signal_comps = "constant b  :  unsigned (" + str(b_size - 1) + " downto 0) := to_unsigned(" + str(b) + "," + str(b_size) + ");\n"
    process = "process(clk)\nbegin\n  if rising_edge(clk) then\n    "\
              + "b_a_inv_b_floor <= a_inv_b_floor * b;\n  end if;\nend process;"
    f = open("template.txt", "r")
    lines = ""
    for line in f:
        lines += line.replace("[1]", name).replace("[2]", io).replace("[3]", signal_comps).replace("[4]", process)
    f.close()
    f = open(name + ".vhd", "w")
    f.write(lines)

def write_subtractor_and_comparator(b, b_size, a_size):
    name = "subtract_" + str(b) + "_and_reduce"
    io = "b_a_inv_b_floor  :  in unsigned (" + str(b_size + a_size - 1) + " downto 0);\n    "\
         + "a  :  in unsigned (" + str(a_size - 1) + " downto 0);\n    "\
         + "c  :  out unsigned (" + str(b_size - 1) + " downto 0)\n"
    signal_comps = "signal sub_res  :  unsigned (" + str(b_size) + " downto 0);\n"
    process = "process(clk)\nbegin\n  if rising_edge(clk) then\n    "\
              + "sub_res <= a - b_a_inv_b_floor;\n    if sub_res >= " + str(b) + " then\n      c <= sub_res - " + str(b)\
              + ";\n    else\n      c <= sub_res - 0;\n    end if;\n  end if;\nend process;"
    f = open("template.txt", "r")
    lines = ""
    for line in f:
        lines += line.replace("[1]", name).replace("[2]", io).replace("[3]", signal_comps).replace("[4]", process)
    f.close()
    f = open(name + ".vhd", "w")
    f.write(lines)

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
    inv_b = find_inverse(b, max_error)
    write_multiplier_floor(inv_b, a_size)
    write_multiplier(b, b_size, a_size)
    write_subtractor_and_comparator(b, b_size, a_size)
    
    
