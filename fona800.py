import serial
import time



modem = serial.Serial('/dev/ttyUSB0',115200,timeout=5)


def send (number,message):
    print('Sending message ......')
    number_str = 'AT+CMGS=\"' + number + '\"\r\n'
    message_str = message + '\r'
    modem.write("AT+CMGF=1\r".encode())    #set it to TEXT mode
    time.sleep(1)
    modem.write(number_str.encode())    #write number_str to uart
    time.sleep(1)
    modem.write(message_str.encode())    #write message_str to uart
    time.sleep(1)
    modem.write('\x1a'.encode())    #send ctrl+z to uart
    time.sleep(1)
    print(modem.read(200).decode())    #read uart


def credit():
    modem.write("ATD\r".encode())
    time.sleep(5)
    print(modem.read(200).decode())
    time.sleep(10)
    modem.write("ATH\r".encode())

def read_unread ():
    modem.write("AT+CMGL=\"REC UNREAD\"\r".encode())
    time.sleep(5)
    print(modem.read(1000).decode())

def read_all ():
    modem.write("AT+CMGL=\"ALL\"\r".encode())
    time.sleep(5)
    print(modem.read(1000).decode())

def delete_one ():
    read_all()
    num = input('enter location index of message you want to delete : ')
    num_str = "AT+CMGD=" + num + "\r"
    modem.write(num_str.encode())
    time.sleep(1)
    print(modem.read(200).decode())
