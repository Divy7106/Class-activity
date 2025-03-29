def find_cube_pairs(target): # NO COLON AFTER DEFINING FUNCTION
    solutions = [];
    max_num = round(target ** (1/3))  # THERE SHOULD BE 2 STAR FOR TAKING (1/3) POWER 
    # ALSO VARIABLE NAME SHOULD BE target NOT targ

    for a in range(1, max_num + 1): # NO COLON AFTER FOR LOOP # ALSO IT SHOULD BE range NOT ranges
        for b in range(a, max_num + 1): # NO COLON AFTER FOR LOOP # IT SHOULD BE range NOT ranges 
            if a**3 + b**3 == target: # THERE SHOULD BE 2 STAR FOR TAKING CUBE # VARIABLE NAME SHOULD BE CORRECTED
                # ALSO COLON FOR IF(^) BLOCK
                solutions.append((a, b)); # AGAIN VARIABLE NAME SHOULD BE ADJUSTED
    return solutions # AGAIN VARIABLE NAME IS WRONG

pairs = find_cube_pairs(1729) # THERE SHOULD BE NO COMMA
print("Valid cube pairs for 1729:"), # USE PRINT THERE IS NO FUNCTION LIKE printf # THERE SHOULD BE 1729 INSTEAD OF 1728
for a, b in pairs: # NO COLON AFTER FOR LOOP # IT SHOULD BE pair INSTEAD OF pairs
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1728") # USE PRINT THERE IS NO FUNCTION LIKE printf  # THERE SHOULD BE 1729 INSTEAD OF 1728
    # THERE SHOULD BE a**3 and b**3 instead of a**2 and b**2