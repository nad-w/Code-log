
def simple_interest(P, R, T): 
    return (P * R * T)/100
    
P = float(input("principal")) 
R = float(input("Rate of interest")) 
T = float(input("Time (in years)")) 

si = simple_interest(P, R, T) 
print("Future Value:", round(si, 2))