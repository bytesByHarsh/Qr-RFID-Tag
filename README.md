# QR RFID Tag

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

**Notification and Temprature Control**

![](https://imgur.com/L3Wcrj3.jpg)

* LM35 sensor is used.

* Since the expiry date is stores in the servers notification is directly send to the mobilephone or any other platform where the user is notified
* Temprature Sensors keep on sending the information to the micro-controller for eg arduino and it sets the temperature of cooling system accordingly.


**Packet Authentication**

* Check information using RFID tag if hammpered or no responce then either RFID has default or packet is tamperred.
* Compare with the original image to find if the product is tampered or not using ML.

![Reader RFID](https://imgur.com/G38B6VJ.jpg)


**For the network of such sensors**

![Network RFID](https://imgur.com/4d584yP.jpg)
