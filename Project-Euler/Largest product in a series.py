number =  7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
length = len(str(number))
n = 0 
ni = 0
nf = 13
n0_13 = str(number)[ni:nf]
#print(n0_13)
product0 = 1
product = 1
while nf < 1000:
    ni += 1
    nf += 1  
    n1_13 = str(number)[ni:nf]
    if '0' in n1_13:
        pass
    else:
        if product0 < product:
            product0 = product
            
        #print(n1_13)
        n1 = str(n1_13)[n]
        n2 = str(n1_13)[n+1]
        n3 = str(n1_13)[n+2]
        n4 = str(n1_13)[n+3]
        n5 = str(n1_13)[n+4]
        n6 = str(n1_13)[n+5]
        n7 = str(n1_13)[n+6]
        n8 = str(n1_13)[n+7]
        n9 = str(n1_13)[n+8]
        n10 = str(n1_13)[n+9]
        n11 = str(n1_13)[n+10]
        n12 = str(n1_13)[n+11]
        n13 = str(n1_13)[n+12]
        product = int(n1) * int(n2) * int(n3) * int(n4) * int(n5) * int(n6) * int(n7) * int(n8) * int(n9) * int(n10) * int(n11) * int(n12) * int(n13)  
        
print(product0)