import time
def time_convertor(diffrence_time):
    diffrence_time = (diffrence_time)
    miin = diffrence_time // 60
    hour = miin // 60
    sec = diffrence_time % 60
    print(f'the time is {int(hour)}:{int(miin)}:{round(sec,2)}')
    
input('press enter to start the stopwacth: ')
start_time = time.time()
input('press enter to stop the stopwacth: ')
stop_time = time.time()
diffrence_time = stop_time - start_time
time_convertor(diffrence_time)
