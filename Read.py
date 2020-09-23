import time
import RPi.GPIO as GPIO
import MFRC522
 
# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
 
# Welcome message
print("Looking for cards")
print("Press Ctrl-C to stop.")
 
# This loop checks for chips. If one is near it will get the UID
try:
   
  while True:
 
    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
 
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
 
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
 
      # Print UID
      print("UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
 
      time.sleep(2)
 
except KeyboardInterrupt:
  GPIO.cleanup()