n = 0
z = 0
while n < 20 and z <= 100:
    if (z <= 100):
        z_string = "0" + str(z)
    else:
        z_string = str(z)
    print("results_n" + str(n) + "_z" + z_string + ".bin")
    if (z != 100):
        z += 10
    else:
        z = 0
        n += 5
    

