from time import sleep

wher = input("Where file: ")
howSleep = int(input("how mach the output be? "))
try:
    file1 = open(f"{wher}","r")

    text = list(file1.readlines())
except:
    print("No file found")





# Do to print staf
#: Do ***,a save the fuc to a and print it
#: Do %a it print what in a


# to do print the z whith out z equals: Sucsess



num = 0
poc = list()
on = 0
bo = ""
bonc = True
bon = 0
loly = {}
hen = str()
boo = 0



for i in text:
    for i in text[boo]:
        if i in "+-*/ (),%\n":
            poc.append(hen)
            hen = str()
            poc.append(str(i))
        else:
            hen += i
    if hen != "":
        poc.append(hen)
    
    on = 0
    for i in poc:
        try:
            num = float(poc[on])
            
        except:
            on += 1
            continue
    on = 0


    





    for i in poc:
        try:
            if i == "Do":
                for i in poc:    
                    try:
                        cock = True
                        if i != ' ' and i != '' and i != "(" and i != ")" and i != "%" and i not in "abcdefghijklmnopqrstuvwxyz":
                            
                            if poc[on] == "+":
                                num = num + float(poc[on+1])
                                
                                on += 1
                            if poc[on] == "*":
                                num = num * float(poc[on+1])
                                
                                on += 1
                            if poc[on] == "/":
                                num = num / float(poc[on+1])
                                
                                on += 1
                            if poc[on] == "-":
                                num = num - float(poc[on+1])
                                
                                on += 1
                            
                                

                            else:
                                on += 1 
                                continue 
                        
                        
                        else:
                            if i != ' ' and i != '' and i != "(" and i != ")":
                                try:
                                    
                                    bon = 0
                                    for w in poc:   
                                        
                                        if poc[bon] == "%" and poc[bon+1] in "abcdefghijklmnopqrstuvwxyz":
                                                
                                            
                                                
                                                num = (loly.get(poc[bon+1]))
                                                
                                                break
                                                    
                                        else:
                                            bon += 1

                                    
                                except:
                                    pass
                    except:
                        continue
                print(num)   
            
            elif i == "In":
                bon = 0
                
                for i in poc:
                    cock = False
                    if poc[bon] == "," and poc[bon+1] in "abcdefghijklmnopqrstuvwxyz":
                        do = input(" ")
                        loly[poc[bon+1]] = do
                        break
                    else:
                        bon += 1
            elif i == "Ln":
                bon = 0
                
                for i in poc:
                    cock = False
                    if poc[bon] == "," and poc[bon+1] in "abcdefghijklmnopqrstuvwxyz":
                        do = poc[bon-1]
                        loly[poc[bon+1]] = do
                        break
                    else:
                        bon += 1
            else:
                on += 1    
                

        except:
            continue

    
    
    try:
        if cock:
            bon = 0
            for i in poc:   
                if poc[bon] == "," and poc[bon+1] in "abcdefghijklmnopqrstuvwxyz":
                    loly[poc[bon+1]] = num
                else:
                    bon += 1
        
    except:
        pass
    print(loly)
    
    for i in poc:
        
        if i == "Do" or i == "In" or i == "Ln":
            bonc = False
            break
        else:
            bonc = True

    if bonc == True: 
        print("NO func Found")
    
    num = 0
    hen = ""
    poc = list()
    boo += 1 
    bonc = True
    bon = 0
    

    
sleep(howSleep)
