from menu2 import usermenu
from makedir2 import mk_dir

curr_dir = 'ParentFile'
file_ary = [[curr_dir]]

done = 0
while done == 0:
    opt = usermenu()
    print('\n Input Value= ' + opt)

    if opt == 'q' or opt is None:
        print('\nExiting Program...')
        done = 1
        break

    elif opt == 'mkdir':
        print('\n')
        file_nam = input("Name your new file: ")
        if file_nam is None:
            print('\nNull input detected, please try again...\n')
        else:
            appendhere = mk_dir(file_ary, curr_dir)
            file_ary.insert(appendhere, file_nam)

    elif opt == 'ls':
        print('\nListing Contents...\n')
        for r in file_ary:
            for c in r:
                print(c, end=" ")
            print()

    elif opt == 'cd':
        new_dir = input("\nEnter desired directory path: ")
        exists = new_dir in file_ary
        if exists:
            curr_dir = new_dir
        else:
            print('No such file was found...')

    else:
        print('\nUser input error.\n Please enter one of the following values at the menu prompt: \nmkdir,cd,ls, or q')
quit()
