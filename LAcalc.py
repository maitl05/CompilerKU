from enum import Enum
from decimal import Decimal
# inn = open("myinput.txt","rt")
# #print(inn.read())
# for i in inn.read():
#     if i=="\n":
#         print("enter zaaade")


with open("myinput.txt", "rt") as inn:
    buffer = inn.read()

class Type(Enum):
    EndOfEntery = 0 #$
    ID = 1
    Equal = 2
    Number = 3
    MathOperator = 4
    Parenthesis = 5

class Token:
    def __init__(self, types=None, value=None):
        self.Type = Type[types].value
        self.Value = value

Ltokens = []

#ltokens.append(Token("EndOfEntry","End"))
#print(ltokens[0].Type, ltokens[0].Value)

def getToken(buffer):
    
    tokenCounter=0
    state=0
    tempEntery=""
    i = 0

    while i < len(buffer):
        
        if(state==0):
            if(buffer[i]==' ' or buffer[i]=="\n"):
                i += 1
            
            elif(buffer[i].isalpha() or (buffer[i] == "_")):
                state = 10

            elif(buffer[i] == '='):
                state = 20

            elif(buffer[i].isdigit()):
                state = 30
            
            elif((buffer[i] == '+') or (buffer[i] == '-') or (buffer[i] == '*') or (buffer[i] == '/')):
                state = 40
            
            elif((buffer[i] == '(') or (buffer[i] == ')')):
                state = 50
            
            elif(buffer[i] == "$"):
                Ltokens.append(Token("EndOfEntery", "$"))
                print("compiled!!! or input finished!!! :)")
                break

            else:
                print("Bad input ERROR!!!")
                break
        
        elif(state==10):
            if((buffer[i].isdigit()) or (buffer[i] == '_') or (buffer[i].isalpha())):
                state = 10
                tempEntery += buffer[i]
                
                i += 1
            
            if(not((buffer[i].isdigit()) or (buffer[i] == '_') or (buffer[i].isalpha()))):
                state = 0
                Ltokens.append(Token("ID", tempEntery))
                
                tempEntery = ""
                
       
        elif(state==20):
            if(buffer[i] == "="):
                Ltokens.append(Token("Equal", "="))
                i += 1
                if(buffer[i] == "="):
                    print(" bad entry '==' exit!!!")
                    break
            
            if(not(buffer[i] == "=")):
                state = 0

        elif(state==30):
            if(buffer[i].isdigit()):
                state = 30
                tempEntery += buffer[i]
                i += 1
                if(buffer[i].isalpha()):
                    print("bad entry alphabet inside number exit!!!")
                    break
            
            if(not(buffer[i].isdigit()) and not(buffer[i] == ".")):
                state = 0
                Ltokens.append(Token("Number", int(tempEntery)))
                tempEntery = ""
            
            if(buffer[i]=="."):
                state = 31
                tempEntery += buffer[i]
                i += 1

        elif(state == 31):
            if(buffer[i].isdigit()):
                state = 31
                tempEntery += buffer[i]
                i += 1
            
            if( not(buffer[i].isdigit()) ):
                state = 0
                Ltokens.append(Token("Number",Decimal(tempEntery)))
                tempEntery=""
            
            if(not(buffer[i]==".")):
                print("bad entry number with two or more '.' exit!!!")
                break

        elif(state==40):
            if((buffer[i] == '+') or (buffer[i] == '-') or (buffer[i] == '*') or (buffer[i] == '/')):
                Ltokens.append(Token("MathOperator", buffer[i]))
                state = 0
                i += 1

        elif(state==50):
            if( (buffer[i] == ')') or (buffer[i] == '(') ):
                Ltokens.append(Token("Parenthesis",buffer[i]))
                state = 0
                i += 1

        else:
            state = 0

try:
    # i =0
    # while i < len(buffer):
    #     print(buffer[i])
    #     i+=1

    # print(buffer)

    getToken(buffer)
    
    j = 0
    while j < len(Ltokens):
        print("_______________")
        print(Ltokens[j].Type)
        print(Ltokens[j].Value)
        print("_______________")
        j+=1

except:
    print("something went wrong!!!")
