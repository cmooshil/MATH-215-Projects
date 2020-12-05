import turtle

def pascal(n):
    '''
    Creates a Pascal's triangle with n steps:

    n -- user-generated length of triangle;
    result -- printed list, created via comprehension;
    lem -- length of result;
    '''
    pt = []
    result = []
    for i in range(1, n+1):
        lem = len(result)
        result = [1 if i == 0 or i == lem else result[i-1]+result[i] for i in range(lem+1)]
        #print(result)
        pt.append(result)
    return pt

def draw(p):
    n = len(p)
    turtle.setworldcoordinates(0, 0, n+1, n+1)
    turtle.tracer(0)  
    t = turtle.Turtle()
    position = (n+1)/2 - 1/2
        
        
    for row in range(n):
        newPosition = position - row*0.5
        #newPosition = position + row*0.5
        for column in range(len(p[row])):
            x = p[row][column]
            if x % 2 == 0:
                #even numbers
                t.color('blue')
            elif x % 3 == 1:
                #remainder upon division by 3
                t.color('green')
            else:
                #odd numbers
                t.color('yellow')
        
            t.hideturtle()
            t.penup()
            t.goto(newPosition+column,n-row)
            t.pendown()
            t.begin_fill()
            t.forward(1)
            t.left(90)
            t.forward(1)
            t.left(90)
            t.forward(1)
            t.left(90)
            t.forward(1)
            t.left(90)
            t.end_fill()
    


def main():
    user = int(input('Enter a number of rows: '))
    p = pascal(user)
    #print(p)
    draw(p)
    
    turtle.mainloop()

    restart = input ("Run again? y or n: ")
    if restart == "y":
        main()

    else:
        exit()


main()
