for i in range(1,101):
    if i%5==0 and i%2 ==0:
        if i == 100: 
            print(100, "babax.")
            break
        print(i,"babax")
        continue
    elif i%2 == 0:
        print(i, "bym,", end="")
        continue
    elif i%5 == 0:
        print(i,"bam,",end="")
        continue
    
    else: print(i,"-,",end="")
print(".", end="")