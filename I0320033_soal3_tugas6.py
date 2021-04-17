x = 10
y = 24

for hasil in range(x ,y + 1):
    if hasil > 1:
        for i in range(2, hasil):
            if (hasil % i) == 0:
                print(hasil,"bukan prima")
                break
        else:
            print(hasil, "adalah bilangan prima")