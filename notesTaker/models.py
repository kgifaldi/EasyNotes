from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.

#   - class : [0:[M, W, F], 1:startTime(int), 2: endTime(int), 3:notes{date("03:22:13" : notes(str) } ]

    #classData = [] # [0] = ["M", "W"], [1] = startTime(int:1230), [2] = endTime(int), [3] = notesData {date("03:22:13") : notes("blah balh")}

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    userData = {}
    tempList = []
    emptyList = []
    emptyDict = {}
    tempList.append(emptyList)
    tempList.append(0000)
    tempList.append(2400)
    tempList.append(emptyDict)
    userData['MISC'] = tempList

    #            "biology", [0:["M", "W"], 1:1323, 2:1440, 3:{}
    def addClass(self, CLASSNAME, CLASSDATA):
        self.userData[CLASSNAME] = CLASSDATA

    #            "biology:, "W", "1200", "02:21:20", "balh balh"
    def addNotes(self, CLASSNAME, DAY, TIME, DATE, NOTES):
        classFound = False
        for tempClass, tempList in self.userData.keys():
            if DAY in tempList[0] and TIME > tempList[1] and TIME < tempList[2]:
                classFound = True
                # add notes to self.userData:
                ((self.userData[tempClass])[3])[DATE] = NOTES
                break
        if not classFound:
            ((self.userData['MISC'])[3])[DATE] = NOTES

    def __str__(self):
        return self.username
