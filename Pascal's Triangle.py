

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

def main():
    user = int(input('Please enter an integer:'))
    for row in pascal(user):
        print(row)
main()
