from calculate import calculate
def GUI():
    c=calculate
    go=True
    calculating=True
    values=[]
    while go == True:
        print('welcome to my calculator.')
        print('symbols accepted are \n + for add \n - for subtraction \n * for multiplication')
        print('^ for power \n /%/ for modulus \n - for subtraction \n // for multiplication \n')
        print('= for equal \n')
        while calculating==True:
            value=input("enter your digit or symbol:")
            print("\n")
            if value == '=':
                flits=c().tabulate(values)
                if len(flits)!=0 :
                    answer=c().calculating(flits)
                    print('the answer is:',answer)
                    go=False
                    break
                else:
                    print('there was an error\n please, do not enter two numbers or symbols in a row.\n PROGRAM TERMINATED!') 
                    go=False
                    break
            print(value)
            
            values.append(value)
GUI()
            