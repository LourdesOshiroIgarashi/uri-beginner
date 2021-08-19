x, y = map(float, input().split(" "))

if x >= 0:
    if x > 0:
        if y >= 0:
            if y > 0:
                print("Q1")
            else:
                # y == 0
                print("Eixo X")
        else:
            # y < 0:
            print("Q4")
        
    else:
        # x == 0
        if y ==0:
            print("Origem")
        else:
            print("Eixo Y")
else:
    #  x < 0
    if y >= 0:
        if y > 0:
            print("Q2")
        else:
            print("Eixo X")
                
    else:
        print("Q3")
    
