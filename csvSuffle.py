from random import randint
import time
mise = ["店名","店名２","店名３"]
while True:
    msg = ""
    with open("info.csv","w",encoding="utf_8",newline='\n') as fileobj:
        fileobj.write("店名,混雑率,フラグ")
        for i in mise:
            msg += i + "," + str(randint(0,100)) + "," + str(randint(0,1)) + "\n"
        fileobj.write(msg)
    time.sleep(30)