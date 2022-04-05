def feet_to_steps(user_feet):
    
    feet = user_feet / 2.5 
    return int(feet)


if __name__ == '__main__':
    user_feet = float(input())
    print(f'{feet_to_steps(user_feet):0.0f}') 