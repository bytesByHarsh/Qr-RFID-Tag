# Python3 Code for QR code Generation and Reader
from pyzbar import pyzbar

import pyqrcode
import datetime
import cv2

def make_qr(text): 
    qr = pyqrcode.create(text)
    qr.png('test.png', scale=4)

def main():
    action = input("Enter R for read and W for write: ")
    
    if (action=="W" or action=="w"):
        print("Enter the Following details")
        
        ID = input("ID: ")
        Type = input("Type: ")
        Size = input("Size(LxBxH in cm): ")
        Fragile = input("Fragile(Y/N): ")
        now = datetime.datetime.now()
        #Date = str(now)
        Expiry = input("Expiry Date(if none enter N else DD/MM/YYYY): ")
        Temp = input("Ideal Temp: ")

        text = ( "ID:" + ID + "\n" +
                 "Type:" + Type + "\n" +
                 "Size:" + Size + "\n" +
                 "Fragile:" + Fragile + "\n" +
                 "Date:" + str(now.date()) + "\n" +
                 "Time;" + str(now.time()) + "\n" +
                 "Expiry:" + Expiry + "\n" +
                 "Temp:" + Temp )
        
        make_qr(text)
        print("QR Code Saved..")
    
    elif (action=="R" or action=="r"):
        # load the input image
        image = cv2.imread("test.png")
        
        # find the barcodes in the image and decode each of the barcodes
        barcodes = pyzbar.decode(image)
        barcodeData = barcodes[0].data.decode("utf-8")
        barcodeType = barcodes[0].type
        ID,Type,Size,Fragile,Date,Time,Expiry,Temp=barcodeData.split("\n")         
        _,ID=ID.split(":")
        _,Type=Type.split(":")
        _,Size=Size.split(":")
        _,Fragile=Fragile.split(":")
        _,Date=Date.split(":")
        _,Time=Time.split(";")
        _,Expiry=Expiry.split(":")
        _,Temp=Temp.split(":")
        l,b,h = Size.split("x")
        l=int(l)
        b=int(b)
        h=int(h)
        print('Package Information: ')
        print('ID: ',ID)
        print('Type: ',Type)
        print('Size: ',l*b*h)
        print('    Length: ',l)
        print('    Breath: ',b)
        print('    Height: ',h)
        print('Fragile: ',Fragile)
        print('Time: ',Time)
        print('Expiry: ',Expiry)
        print('Desired Temprature: ',Temp)


if __name__=="__main__":
    main()
