#Rajveer
#nov 27 2023
def biggest_of_three(num_1: float, num_2: float, num_3: float):
    """returns the biggest of three numbers"""
    if num_1 > num_2 and num_1 > num_3:
        return num_1
    elif num_2 > num_3:
        return num_2
    else:
        return num_3

print(f"{biggest_of_three(132,113,111)} is the biggest number")