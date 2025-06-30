tv_on = 1
counter = 10
while tv_on <= 1:
    power = True
    print(("TV is on for ") + str(tv_on) + (" minutes"))
    (tv_on) = tv_on + 29
while tv_on <= 30:
    power = True
    print(("Are you still watching ,") + (" TV is on for ") + str(tv_on) + (" minutes"))
    (tv_on) = tv_on + 30
for i in range(10):
    power = False
    print(("TV is on for ") + str(tv_on) + (" minutes"))
    print("TV will shut itself in " + str(counter) + " seconds")

    counter = counter - 1
    



