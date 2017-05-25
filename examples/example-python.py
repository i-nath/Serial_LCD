import serial
import yweather
import time
client=yweather.Client()
city="isukapudi"
country="india"
cid=client.fetch_woeid((city+','+country))
while 1:
    winfo=client.fetch_weather(cid,metric=True)
    print type(winfo)
    th=winfo["forecast"][0]["high"]
    tl=winfo["forecast"][0]["low"]
    co=winfo["condition"]["text"]
    hu=winfo["atmosphere"]["humidity"]
    tp=winfo["condition"]["temp"]
    line1="11 H:"+th+"CL:"+tl+"CHu:"+hu+"%"
    line2="12 "+co
    se=serial.Serial("/dev/ttyACM1")
    se.baudrate=9600
    se.write("11    Updating    ")
    se.flush()
    se.close()
    print se.isOpen()
    time.sleep(1)
    se.open()
    se.write(line1)
    se.flush()
    se.close()
    print se.isOpen()
    time.sleep(1)
    se.open()
    se.write("12                ")
    se.flush()
    se.close()
    print se.isOpen()
    time.sleep(1)
    se.open()
    se.flush()
    se.write(line2)
    print line2
    se.close()
    time.sleep(120)
