str="";    
for r in range(0,7):    
    for c in range(0,7):     
        if (c == 1 or ((r== 0 or r == 3 or r == 6) and (c < 5 and c > 1)) or (c == 5 and (r != 0 and r != 3 and r != 6))) :  
            str=str+"B"    
        else:      
            str=str+" "    
    str=str+"\n"    
print(str);    
