# -*- coding: utf-8 -*-

stack = "$"
status = "A"

input = raw_input ("Δώσε συμβολοσειρά:").decode('utf-8')

if input=='':
	print ("\nstack:"), stack, ("\t\tstatus:"), status, ("\t\tInput Symbols:"), input
	print("\nΔεν έχεις εισάγει δεδομένα...")
	quit()


print ("\nstack:"), stack, ("\t\tstatus:"), status, ("\t\tInput Symbols:"), input



for i in range(len(input)):
    if input[i].encode('utf-8') == "Μ":                                                                             
        stack = stack + input[i]  
        print ("stack:"), stack, ("\t\tstatus:"), status, ("\t\tInput Symbols:"), input[i + 1:]        
    elif input[i].encode('utf-8') == "Σ" and stack.encode('utf-8').endswith("Μ"):
        stack = stack[:-1]    
        print ("stack:"), stack, ("\t\tstatus:"), status, ("\t\tInput Symbols:"), input[i + 1:]
    else:
		status = "error"
		break
	

	   
        

	
if stack == "$" and status == "A":
	print ("\nYES")
else:
	print ("NO")



