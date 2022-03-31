def laps_to_miles(user_laps):
    mile = user_laps / 4 
    return mile


if __name__ == '__main__':
    user_laps = float(input())
    print(f'{laps_to_miles(user_laps):.2f}') 
    
    
