result_str="";      
for r in range(0,7):      
    for c in range(0,7):       
        if (((c == 1 or c == 5) and r != 0) or ((r == 0 or r == 3) and (c > 1 and c < 5))):      
            result_str=result_str+"A"      
        else:        
            result_str=result_str+" "      
    result_str=result_str+"\n"      
print(result_str);  
