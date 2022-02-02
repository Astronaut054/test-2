# #-------------------------<<<<<توضیحات کلی>>>>>------------------------# #
print("-------------------------------------------------"'\n'
    "<<<Convert seconds to year, month, week and...>>>"'\n'
    "-------------------------------------------------"'\n'
    "Made By:"'\n'
    "   o----[=====Amir.hz=====>"'\n'
    "-------------------------------------------------"'\n'
    "To buy Key enter the channel below"'\n'
    " → → → → → → @TEST-2 ← ← ← ← ← ←")
# #----------------------<<<<<حلقه اول،وارد کردن کلید>>>>>--------------------# #
while 1:
    print("-------------------------------------------------")
    Point = 0
    key = input("Enter your Key: ")
    if key == "exit" or key == "out" : # #----------<<<Exit>>>---------# #
        print("-------------------------------------------------")
        print("<<<<<<<<Exit>>>>>>>>")
        break 
    elif key == "04143242466" : # #-------------<<<Keys>>>-------------# #
        Point = 9999999999
    elif key == "5394545874" :
        Point = 250
    elif key == "5896242452" :
        Point = 200
    elif key == "8962114142" :
        Point = 150
    elif key == "1654869754" :
        Point = 100
    elif key == "1574896423" :
        Point = 50
    elif key == "5354588742" : # #-----------<<<End_Keys>>>-----------# #
        Point = 10 
    else :
        print("The code entered is wrong.")
    while Point > 1 : # #---------------<<<<<حلقه دوم>>>>>--------------# #
        print("-------------------------------------------------")
        print("Point: ", Point)
        time = input("Enter seconds: ")
        if time == "exit" or time == "out" : # #------<<<Exit>>>------# #
            print("-------------------------------------------------")
            print("<<<<<<<Exit>>>>>>>")
            break
        else : # #---------------<<<<<Convert Time>>>>>---------------# #
            time = int(time)
        year = time // 31536000
        time -= year * 31536000
        month = time // 2628000
        time -= month * 2628000
        week = time // 604800
        time -= week * 604800
        day = time // 86400
        time -= day * 86400
        hour = time // 3600
        time -= hour * 3600
        minute = time // 60
        time -= minute * 60
        if key == "04143242466" : # #------<<<Infinite Point>>>------# #
            Point = 9999999999
        else :
            Point -= 5
# #--------------------------<<<<<Print>>>>>-------------------------# #
        print(year,"years",month,"months",week,"weeks",day,
        "days",hour,"hors",minute,"minutes",time,"seconds")
        if Point <= 0 :
            print("-------------------------------------------------")
            print('Your inventory is over.')


#Power by:
#   Hilda \(^-^)/
