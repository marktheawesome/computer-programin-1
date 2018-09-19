#fahernheight

#celsis = ((farerheight - 32) * (5/9))

def farerheight_to_celsius (f):
    celsius = ((f - 32) * (5/9))
    return celsius

print ("degree farerheight")
f = input()
f = float(f)
print (str (farerheight_to_celsius (f)))