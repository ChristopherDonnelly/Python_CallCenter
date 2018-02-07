'''
You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.

You will create two classes. One class should be Call, the other CallCenter.

Call Class
• Create your call class with an init method. Each instance of Call() should have:

Attributes:
• unique id
• caller name
• caller phone number
• time of call
• reason for call

Methods:
• display: that prints all Call attributes.

CallCenter Class
• Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:

Attributes:
• calls: should be a list of call objects
• queue size: should be the length of the call list

Methods:
• add: adds a new call to the end of the call list
• remove: removes the call from the beginning of the list (index 0).
• info: prints the name and phone number for each call in the queue as well as the length of the queue.

You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!

Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.

Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.
'''

import datetime
import time

class Call(object):
    def __init__(self, uniqueId, name, number, reason):
        self.uniqueId = uniqueId
        self.name = name
        self.number = number
        self.time = datetime.datetime.now().strftime('%I:%M:%S%p %m/%d/%Y')
        self.reason = reason
        # self.display()
    def display(self):
        print 'Unique ID: {}\nName: {}\nNumber: {}\nTime: {}\nReason: {}'.format(self.uniqueId, self.name, self.number, self.time, self.reason)
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0
        self.unique_callId = 0
    def add(self, name, number, reason):
        self.unique_callId += 1
        self.calls.append(Call(self.unique_callId, name, number, reason))
        self.queue_size += 1
        self.info()
        return self
    def remove(self):
        self.calls.pop(0)
        self.queue_size -= 1
        self.info()
        return self
    def removeByNumber(self, num):
        for idx, call in enumerate(self.calls):
            if call.number == num:
                print "Removing Call with phone number {} from queue:".format(num)
                call.display()
                self.calls.pop(idx)
                self.queue_size -= 1
                break

        print '\n'
        return self
    def info(self):
        print 'Queue Size:',self.queue_size
        for call in self.calls:
            call.display()

        print '\n'
        return self


myCallCenter = CallCenter()

myCallCenter.add('Chris', '805-588-4780', "I broke my plumbus and I cannot push my dinglebop through the grumbo so the fleeb doesn't fill up with its schleem")
time.sleep(5)
myCallCenter.add('David', '805-588-4781', "MY LAPTOP HAS BEEN STOLEN!")
time.sleep(.5)
myCallCenter.add('Donnelly', '805-588-4782', "I got charged fees and I want them all reversed. I wasn’t aware that I was being charged.")
time.sleep(1)
myCallCenter.add('Tom', '805-588-4783', "My laptop is frozen.")
time.sleep(3)
myCallCenter.add('Bob', '805-588-4784', "I would like to report a broken modem, and I want I changed now.")
time.sleep(.3)
myCallCenter.add('Larry', '805-588-4785', "I need my overages credited this instant. I never used this much data before, and I need it credited.")

myCallCenter.removeByNumber('805-588-4782').remove()