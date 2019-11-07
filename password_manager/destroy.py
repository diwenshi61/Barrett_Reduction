def destroy(file):
    import random
    import os
    c = 0
    while c < 100:
        f = open(file,"w")
        g = 0
        while g < 100:
            h = 0
            while h < 500:
                f.write(str(int(round(random.random()))))
                h += 1
            f.write("\n")
            g += 1
        c += 1
        f.close()
    os.remove(file)