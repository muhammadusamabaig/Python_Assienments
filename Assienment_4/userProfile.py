def user_profile(*profileinfo):
    print(f'name : {profileinfo[0]}')
    print(f'f_name : {profileinfo[1]}')
    print(f'position : {profileinfo[2]}')
    print(f'company : {profileinfo[3]}')    

def show_magicians(magList):
    for i in magList:
        print(i)
    