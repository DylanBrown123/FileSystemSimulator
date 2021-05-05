def usermenu():
    print('\n\nHello, Welcome to my File System Simulator \nPlease Input one of the following options: \n'
          'ls)    - Display Contents \n'
          'mkdir) - Make Directory \n'
          'cd)    - Change Directory \n'
          'q)     - Quits Program')
    option = input("Enter command: ")
    if option is None:
        return None

    print("option")
    return option