burger=input("would you like a burger for 5$ (yes/no) ")
fries=input("would you like fries for 3$ (yes/no) ")
totalCost=0

if burger.lower()== "yes":
    totalCost+=5
if fries.lower()=="yes":
    totalCost+=3
tax=totalCost* 0.14    
print(f"${tax+ totalCost}")