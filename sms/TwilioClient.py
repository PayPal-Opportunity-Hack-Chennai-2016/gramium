# coding=latin-1
from twilio.rest import TwilioRestClient

class TwilioClient:
    account = "ACf77bdabb559d9880ded6f082f11f4578"
    token = "a3abea2206d16a0551d0501f31728474"

    def createClient(self):
        client = None
        try:
            client = TwilioRestClient(self.account, self.token)
        except:
            print "Error while creating twilio client"
        return client

    def sendSMS(self, to, from_, body):
        client = self.createClient()
        try:
            client.messages.create(to=to, from_=from_,body=body)
            return_status = 0
        except Exception as e:
            print "Error while sending SMS"
            print e
            return_status = 1
        return return_status

    def makeCall(self, to, from_, url):
        client = self.createClient()
        try:
            client.calls.create(to=to,from_=from_,url=url)
            return_status = 0
        except Exception as e:
            print e
            print "Error while making call"
            return_status = 1
        return return_status

if __name__ == "__main__":
    client = TwilioClient()
    #client.sendSMS(to="+917358232971",  from_="(267) 433-0959", body="Hello There!")
    client.makeCall(to="+918056903214", from_="(267) 433-0959",
                            url="http://twimlets.com/menu?Message=Message+From+GrawMeYum+Organization.+Pay+Your+Due+Amount+Rupees+765.00+before+5+December+2016")