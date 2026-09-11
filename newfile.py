def AND_gate(a, b):
    return a & b
    
print("AND Gate Truth Table")
print("A B | Output")

for a in [0, 1]:
    for b in [0, 1]:
        print(f"{a} {b} | {AND_gate(a, b)}")
        
      
def full_adder(a, b, cin):
    
    sum_bit = a^b^cin
    
    carry1 = a&b
    
    carry2 = cin&(a^b)
    
    cout = carry1 | carry2
    
    return sum_bit, cout 
   
print("Full Adder Truth Table")
print("A B Cin | Sum Cout")
for a in [0, 1]:
    for b in [0, 1]:
        for cin in [0, 1]:
            s, c = full_adder(a, b, cin)
            print(f"{a} {b} {cin} | {s} {c}")
            
