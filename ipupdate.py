#!/usr/bin/env python
#
# ipupdate.py
# Check public IP, on change send out sms and email notification
# http://linux-101.org
#
 
import string
import httplib
import smtplib
from sms import Sms
from email.Utils import formatdate
 
# Set some variables
smtpServer = "smtp.gmail.com"
smtpUser = "fhlipZero@gmail.com"
smtpPass = "00190LZLNGZKLISORHMQZECTTNVZLF"
fromAddress = "fhlipZero@gmail.com"
toAddress = ("fhlipZero@gmail.com")
mobileNumber = "4125822951"
logFile = "/var/log/ip-log.log"
 
try:
    conn = httplib.HTTPConnection("ip.appspot.com")
    conn.request("GET", "/")
    r1 = conn.getresponse()
#    print r1.status, r1.reason
        # If IP is unchanged, close and exit.
        if oldip.strip() == straddr:
            logfile.close()
            conn.close()
        else:
            # If new IP, first write to log, then send SMS, then send email
            logfile = open(logFile,"a")
            logfile.write(straddr + "\n")
            logfile.close()
            conn.close()
            sms = TextMessage(recipient=mobileNumber, message="New IP address is: \r" + straddr)
            sms.connectPhone()
            sms.sendMessage()
            sms.disconnectPhone()
            s = smtplib.SMTP(smtpServer)
            s.set_debuglevel(0)
            s.ehlo()
            s.starttls()
            s.ehlo()
            # Hash out below line if login is not needed
            s.login(smtpUser, smtpPass)
            emailDate = formatdate(localtime=True)
            emailMsg = """From: Home PC &lt;home-pc@example.com&gt;
Date: """ + emailDate + """
Subject: IP Address has changed.
 
New IP address is: """ + straddr + """
"""
            s.sendmail(fromAddress, toAddress, emailMsg)
            s.close()
except:
    print "Exception raised! Something's not working."
