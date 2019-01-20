# Qr-RFID-Tag
A simple IoT based packaging solution


**Basic Algorithm:-**

![Basic Algorithm Image](https://i.imgur.com/zzq8xef.png)

*	Camera takes in the image and identify the size of the packet and other features like its type, if any tampering with packaging.
*	Weighs the packet
*	Stores the info and other details along with the ID of the packet in the database.
*	Generate *QR code* and a custom *RFID tag* and stick on the package

> The QR code is used so that directly information can be verified just by scanning.

> RFID tag are used so that information for the package can be transferred using sensors without physically to be present near the packet. It can be used for indoor tracking of the package and for real time location of the package. This can be done by placing several RFID sensors across the warehouse and then looking for the ID of that package.
>
> In *Type* of QR code different type is stored along with whether it is hazardous or not as extra precautions will be taken for hazardous packages.
```

## Python3 Code for QR code Generation and Reader
import pyqrcode
import datetime
from pyzbar import pyzbar
import cv2

def make_qr(text):
    
    qr = pyqrcode.create(text)
    qr.png('test.png',scale=4)

def main():
    
    action = input("Enter R for read and W for write\n")
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
                 "Temp:" + Temp)
        make_qr(text)
        print("QR Code Saved..")
    elif (action=="R" or action=="r"):
        # load the input image
        image = cv2.imread("test.png")
        # find the barcodes in the image and decode each of the barcodes
        barcodes = pyzbar.decode(image)
        
        # loop over the detected barcodes
        for barcode in barcodes:
            
            # the barcode data is a bytes object so if we want to draw it on
            # our output image we need to convert it to a string first
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            # print the barcode data to the terminal
            print(barcodeData)
        # This part is for further processing with the data read 
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
            
        

if __name__=="__main__":
    main()
    
```



**Notification and Temprature Control**

![](https://imgur.com/L3Wcrj3.jpg)

* Since the expiry date is stores in the servers notification is directly send to the mobilephone or any other platform where the user is notified
* Temprature Sensors keep on sending the information to the micro-controller for eg arduino and it sets the temperature of cooling system accordingly.

> LM35 sensor is used

```
float tem;
int tempPin = 0;
int relay = 13;

void setup() {
   Serial.begin(9600);
	 pinMode(relay,OUTPUT)
	 digitalWrite(relay,LOW);
}

void loop() {
   tem = analogRead(tempPin);
   // read analog volt from sensor and save to variable temp
   tem = tem * 0.48828125;
   // convert the analog volt to its temperature equivalent
   Serial.print("TEMPERATURE FROM THE SENSOR = ");
   Serial.print(tem); // display temperature value
   Serial.print("*C");
   Serial.println();
   delay(1000); // update sensor reading each one second
	 
	 if(tem>desired_temp){
		 digitalWrite(relay,HIGH);
		 Serial.print("Temprature Going Higher,Starting the cooling system...");
	 }
	 else{
	 digitalWrite(relay,LOW);
	 }
	 
	 
}
```


**Packet Authentication**

* Check information using RFID tag if hammpered or no responce then either RFID has default or packet is tamperred.
* Compare with the original image to find if the product is tampered or not using ML.
