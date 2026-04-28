def get_input(min, max):
    while True:
        try:
            choice = int(input(">" ))
            if choice < min or choice > max:
                print(f"Please choose a number from {min} to {max} ")
            else:
                return choice
        except ValueError:
            print(f"Please choose a number from {min} to {max} ")