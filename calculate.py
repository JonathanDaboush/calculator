targetList=[]
class calculate:
    
   
    
    def tabulate(self,newlist):
        legitkeys = ['+','-','*','/','^','%']
        islegit = True
        loopiterate=False
        for item in newlist:
            for character in legitkeys:
                if loopiterate==True:
                    continue
                 
                elif item.isnumeric()==True or item == character:
                    loopiterate=True
                   
                    
            if loopiterate == False:
                islegit=False
                break
            symbolToDigit=''
            if (item.isnumeric()==True) and ( symbolToDigit.isnumeric() == True):
                islegit=False
                break
            elif (item.isnumeric()==False) and ( symbolToDigit.isnumeric() == False) and symbolToDigit != '':
                 islegit=False
                 break
            
            loopiterate=False
            symbolToDigit=item
        if islegit == True:
            targetList=newlist
        else:
            targetList=[]
            
                    
        return targetList
    
    def calculating(self,list):
        
        answer=""
        symbol=""
        
        for item in list:
            if item.isnumeric()==True:
                item=float(item)
                if answer=='':
                    answer=item
                else:
                    match symbol:
                        case "+":
                            answer=answer+item
                        case "-":
                            answer=answer-item
                        case "*":
                            answer=answer*item
                        case "/":
                            answer=answer/item
                        case "^":
                            answer=answer**item
                        case "%":
                            answer=answer%item
                        case _:
                            print('default')
                    
            elif type(item)==str:
                symbol=item
                
                  
        return answer
        
    
