#           Linky Plugin
#
#           Authors:
#                       Copyright (C) 2016 Baptiste Candellier
#                       Modified (C) 2017 Asdepique777
#                       Corrected (C) 2017 epierre
#                       Modified (C) 2017 Asdepique777
#                       Modified (C) 2018 Barberousse
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
<plugin key="linky" name="Linky" author="Barberousse" version="1.0.0" externallink="https://github.com/guillaumezin/DomoticzLinky">
    <params>
        <param field="Username" label="Username" width="200px" required="true" default=""/>
        <param field="Password" label="Password" width="200px" required="true" default="" password="true"/>
        <param field="Mode1" label="Number of days to grab for days view (1 min, 7 max)" width="50px" required="false" default="7"/>
        <param field="Mode2" label="Number of days to grab for others view (28 min)" width="50px" required="false" default="366"/>
        <param field="Mode3" label="Debug" width="75px">
            <options>
                <option label="True" value="Debug"/>
                <option label="False" value="Normal"  default="true" />
            </options>
        </param>
    </params>
</plugin>
"""

# https://www.domoticz.com/wiki/Developing_a_Python_plugin

import Domoticz
from base64 import b64encode
import json
from urllib.parse import quote
import re
from datetime import datetime
from datetime import timedelta
import time
#from random import randint
import html

LOGIN_BASE_URI = 'espace-client-connexion.enedis.fr'
API_BASE_URI = 'espace-client-particuliers.enedis.fr'
BASE_PORT = '443'

API_ENDPOINT_LOGIN = '/auth/UI/Login'
API_ENDPOINT_DATA = '/group/espace-particuliers/suivi-de-consommation'
#HEADERS = {
    #'Accept':'application/json, text/javascript, */*; q=0.01',
    #'Accept-Language':'fr,fr-FR;q=0.8,en;q=0.6',
    #"Content-Type": "application/x-www-form-urlencoded",
    #"Connection": "keep-alive",
    #"X-Requested-With": "XMLHttpRequest",
    #'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
#}
HEADERS = {
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept-Language" : "fr,fr-FR;q=0.8,en;q=0.6",
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0"
}

class BasePlugin:
    # boolean to check that we are started, to prevent error messages when disabling or restarting the plugin
    isStarted = None
    # http connection
    httpConn = None
    iIndexUnit = 1
    sDeviceName = "Linky"
    sDescription = "Compteur Linky"
    iType = 0xF3
    iSubType = 0x21
    iSwitchType = 0
    sConnectionStep = None
    bHasAFail = None
    dCookies = None
    dateBeginDay = None
    dateEndDay = None
    dateBeginMonth = None
    dateEndMonth = None
    historyDays = None
    historyMonths = None
    daysLeft = None
    savedDateEndMonth = None
    firstMonths = None
    
    def __init__(self):
        self.isStarted = False
        self.httpConn = None
        self.sConnectionStep = "idle"
        self.bHasAFail = False

    def resetCookies(self):
        self.dCookies = {}
    
    def getCookies(self, Data):
        if Data and ("Headers" in Data) and ("Set-Cookie" in Data["Headers"]):
            # lCookies = re.findall("^(.*?)=(.*?)[;$]", Data["Headers"]["Set-Cookie"], re.MULTILINE)
            for match in re.finditer("^(.*?)=(.*?)[;$]", Data["Headers"]["Set-Cookie"], re.MULTILINE):
                self.dCookies[match.group(1)] = match.group(2)

    def setCookies(self, headers):
        headers["Cookie"] = ""        
        for sKey, sValue in self.dCookies.items():
            if headers["Cookie"]:
                headers["Cookie"] += "; "
            headers["Cookie"] += sKey + "=" + sValue

    def initHeaders(self):
        return dict(HEADERS)
                
    def login(self, username, password):
        payload = {
            'IDToken1': username,
            'IDToken2': password,
            'SunQueryParamsString': b64encode(b'realm=particuliers').decode(),
            'encoded': 'true',
            'gx_charset': 'UTF-8'
        }
        
        headers = self.initHeaders()
        headers["Host"] = LOGIN_BASE_URI + ":" + BASE_PORT
        
        sendData = {
                    "Verb" : "POST",
                    "URL"  : API_ENDPOINT_LOGIN,
                    "Headers" : headers,
                    "Data" : dictToQuotedString(payload)
        }
        
        #DumpDictToLog(sendData)
        self.resetCookies()
        self.httpConn.Send(sendData)

    def getData(self, resource_id, start_date, end_date):
        req_part = 'lincspartdisplaycdc_WAR_lincspartcdcportlet'

        payload = {
            '_' + req_part + '_dateDebut': datetimeToEnderdisDateString(start_date),
            '_' + req_part + '_dateFin': datetimeToEnderdisDateString(end_date)
        }
        
        headers = self.initHeaders()
        headers["Host"] = API_BASE_URI + ":" + BASE_PORT
        
        #Copy cookies
        self.setCookies(headers)
        
        params = {
            'p_p_id': req_part,
            'p_p_lifecycle': 2,
            'p_p_state': 'normal',
            'p_p_mode': 'view',
            'p_p_resource_id': resource_id,
            'p_p_cacheability': 'cacheLevelPage',
            'p_p_col_id': 'column-1',
            'p_p_col_pos': 1,
            'p_p_col_count': 3
        }
        
        sendData = {
                    "Verb" : "POST",
                    "URL"  : API_ENDPOINT_DATA + "?" + dictToQuotedString(params),
                    "Headers" : headers,
                    "Data" : dictToQuotedString(payload)
        }
        
        #DumpDictToLog(sendData)
        self.httpConn.Send(sendData)

    def createDevice(self):
        if not self.iIndexUnit in Devices:
            Domoticz.Device(Name=self.sDeviceName,  Unit=self.iIndexUnit, Type=self.iType, Subtype=self.iSubType, Switchtype=self.iSwitchType, Description=self.sDescription, Used=1).Create()
    
    def createAndAddToDevice(self, counter, Date):
        self.createDevice()
        Devices[self.iIndexUnit].Update(nValue=0, sValue="-1.0;"+ str(counter) + ";"  + str(Date), Type=self.iType, Subtype=self.iSubType, Switchtype=self.iSwitchType,)

    def updateDevice(self, val):
        self.createDevice()
        Devices[self.iIndexUnit].Update(nValue=0, sValue="-1.0;"+ str(val), Type=self.iType, Subtype=self.iSubType, Switchtype=self.iSwitchType)
        
    def showStepError(self, day, logMessage):
        if day:
            Domoticz.Error(logMessage + " during step " + self.sConnectionStep + " from " + datetimeToEnderdisDateString(self.dateBeginDay) + " to " + datetimeToEnderdisDateString(self.dateEndDay))
        else:
            Domoticz.Error(logMessage + " during step " + self.sConnectionStep + " from " + datetimeToEnderdisDateString(self.dateBeginMonth) + " to " + datetimeToEnderdisDateString(self.dateEndMonth))
       
    def exploreDataDay(self, Data):
        DumpDictToLog(Data)
        if Data and ("Data" in Data):
            try:
                dJson = json.loads(Data["Data"].decode())
            except ValueError as err:
                self.showStepError(False, "Data received are not JSON: " + str(err))
                return False
            except TypeError as err:
                self.showStepError(False, "Data type received is not JSON: " + str(err))
                return False
            else:
                if dJson and ("etat" in dJson) and ("erreurText" in dJson["etat"]):
                    #self.showStepError(True, "Error received: " + html.unescape(dJson["etat"]["erreurText"]))
                    pass
                if dJson and ("etat" in dJson) and ("valeur" in dJson["etat"]) and (dJson["etat"]["valeur"] == "termine"):
                    try:
                        beginDate = enerdisDateToDatetime(dJson["graphe"]["periode"]["dateDebut"])
                        endDate = enerdisDateToDatetime(dJson["graphe"]["periode"]["dateFin"])
                    except (TypeError, ValueError) as err:
                        self.showStepError(True, "Error in received JSON data time format: " + str(err))
                        return False
                    accumulation = 0.0
                    steps = 1.0
                    expectedDateBeginDay = beginDate + timedelta(days=1)
                    # Stop at 22h, to get 0 at 23h to show nothing for day after
                    expectedDateEndDay = endDate - timedelta(hours=1)
                    dataSeenToTheEnd = False
                    for index, data in enumerate(dJson["graphe"]["data"]):
                        try:
                            val = float(data["valeur"]) * 1000.0
                        except ValueError:
                            val = -1.0
                        if (val >= 0.0):
                            curDate = beginDate + timedelta(minutes=(index+2)*30)
                            accumulation = accumulation + val
                            #Domoticz.Log("Value " + str(val) + " " + datetimeToSQLDateTimeString(curDate))
                            #if (curDate >= expectedDateBeginDay) and (curDate <= expectedDateEndDay) and (curDate.minute == 0):
                            if (curDate >= expectedDateBeginDay) and (curDate.minute == 0):
                                #Domoticz.Log("accumulation " + str(accumulation / steps) + " " + datetimeToSQLDateTimeString(curDate))
                                self.createAndAddToDevice(accumulation / steps, datetimeToSQLDateTimeString(curDate))
                                if curDate >= expectedDateEndDay:
                                        dataSeenToTheEnd = True
                            steps = steps + 1.0
                            if curDate.minute == 0:
                                accumulation = 0.0
                                steps = 1.0
                    return dataSeenToTheEnd
                else:
                    #self.showStepError(True, "Error in received JSON data")
                    pass
        else:
            #self.showStepError(True, "Didn't received data")
            pass
        return False
    
    def exploreDataMonth(self, Data):
        DumpDictToLog(Data)
        if Data and "Data" in Data:
            try:
                dJson = json.loads(Data["Data"].decode())
            except ValueError as err:
                self.showStepError(False, "Data received are not JSON: " + str(err))
                return False
            except TypeError as err:
                self.showStepError(False, "Data type received is not JSON: " + str(err))
                return False
            else:
                if dJson and ("etat" in dJson) and ("erreurText" in dJson["etat"]):
                    self.showStepError(False, "Error received: " + html.unescape(dJson["etat"]["erreurText"]))
                if dJson and ("etat" in dJson) and ("valeur" in dJson["etat"]) and (dJson["etat"]["valeur"] == "termine"):
                    try:
                        beginDate = enerdisDateToDatetime(dJson["graphe"]["periode"]["dateDebut"])
                        endDate = enerdisDateToDatetime(dJson["graphe"]["periode"]["dateFin"])
                    except ValueError as err:
                        self.showStepError(False, "Error in received JSON data time format: " + str(err))
                        return False
                    for index, data in enumerate(dJson["graphe"]["data"]):
                        try:
                            val = float(data["valeur"]) * 1000.0
                        except ValueError:
                            val = -1.0
                        if (val >= 0.0):
                            curDate = beginDate + timedelta(days=index)
                            #Domoticz.Log("Value " + str(val) + " " + datetimeToSQLDateString(curDate))
                            #DumpDictToLog(values)
                            self.createAndAddToDevice(val, datetimeToSQLDateString(curDate))
                            if self.firstMonths and (curDate == endDate):
                                #Domoticz.Log("Update " + str(val) + " " + datetimeToSQLDateString(curDate))
                                self.updateDevice(val)
                                self.firstMonths = False
                    return True
                else:
                    self.showStepError(False, "Error in received JSON data")
        else:
            self.showStepError(False, "Didn't received data")
        return False
        
    def calculateDaysLeft(self):
        # No more than 28 days at once
        self.daysLeft = self.daysLeft - 28
        if self.daysLeft <= 0:
            daysToGet = self.daysLeft + 28
        else:
            daysToGet = 28
        self.dateBeginMonth = self.savedDateEndMonth - timedelta(days=daysToGet+2)
        self.dateEndMonth = self.savedDateEndMonth - timedelta(days=1)
        self.savedDateEndMonth = self.dateBeginMonth

    def setNextConnection(self, tomorrow):
        if tomorrow:
            self.nextConnection = datetime.now() + timedelta(days=1)
            self.nextConnection = self.nextConnection.replace(hour=5)
        else:
            self.nextConnection = datetime.now() + timedelta(hours = 1)
        #randint makes domoticz crash on RPI
        #self.nextConnection = self.nextConnection + timedelta(minutes=randint(0, 59), seconds=randint(0, 59))
        minutesRand = round(datetime.now().microsecond / 10000) % 60
        self.nextConnection = self.nextConnection + timedelta(minutes=minutesRand)

    def handleConnection(self, Data = None):
        if self.sConnectionStep == "idle":
            Domoticz.Log("Getting data...")
            self.bHasAFail = False
            if self.httpConn and self.httpConn.Connected():
                self.httpConn.Disconnect()

            self.httpConn = Domoticz.Connection(Name="HTTPS connection", Transport="TCP/IP", Protocol="HTTPS", Address=LOGIN_BASE_URI, Port=BASE_PORT)

            Domoticz.Debug("Connect")
            self.sConnectionStep = "logconnecting"
            self.httpConn.Connect()
            
        elif self.sConnectionStep == "logconnecting":
            if not self.httpConn.Connected():
                Domoticz.Error("Connection failed for login")
                self.sConnectionStep = "idle"
                self.bHasAFail = True
            else:
                self.sConnectionStep = "logconnected"
                self.login(Parameters["Username"], Parameters["Password"])
                
        elif self.sConnectionStep == "logconnected":
            if self.httpConn and self.httpConn.Connected():
                self.httpConn.Disconnect()
            DumpDictToLog(Data)
            
            self.getCookies(Data)
            if ("iPlanetDirectoryPro" in self.dCookies) and self.dCookies["iPlanetDirectoryPro"]:
                self.sConnectionStep = "dataconnecting"
                self.httpConn = Domoticz.Connection(Name="HTTPS connection", Transport="TCP/IP", Protocol="HTTPS", Address=API_BASE_URI, Port=BASE_PORT)
                self.httpConn.Connect()
            else:
                Domoticz.Error("Login failed, will try again later")
                self.sConnectionStep = "idle"
                self.bHasAFail = True

        elif self.sConnectionStep == "dataconnecting":
            if not self.httpConn.Connected():
                Domoticz.Error("Connection failed for data")
                self.sConnectionStep = "idle"
                self.bHasAFail = True
            else:
                self.getCookies(Data)
                self.sConnectionStep = "getcookies"
                self.getData("urlCdcHeure", self.dateBeginDay, self.dateEndDay)
                
        elif self.sConnectionStep == "getcookies":
            if not self.httpConn.Connected():
                Domoticz.Error("Connection failed for cookies read")
                self.sConnectionStep = "idle"
                self.bHasAFail = True
            else:
                self.getCookies(Data)
                self.sConnectionStep = "getdatadays"
                self.getData("urlCdcHeure", self.dateBeginDay, self.dateEndDay)
                
        elif self.sConnectionStep == "getdatadays":
            if not self.httpConn.Connected():
                self.showStepError(True, "Get data failed for day view")
                self.sConnectionStep = "idle"
                self.bHasAFail = True
            else:
                self.getCookies(Data)
                if not self.exploreDataDay(Data):
                    self.bHasAFail = True
                self.sConnectionStep = "getdatamonths"
                self.firstMonths = True
                self.getData("urlCdcJour", self.dateBeginMonth, self.dateEndMonth)
                
        elif self.sConnectionStep == "getdatamonths":
            if not self.httpConn.Connected():
                self.showStepError(False, "Get data failed for month view")
                self.sConnectionStep = "idle"
                self.bHasAFail = True
            else:
                if not self.exploreDataMonth(Data):
                    self.bHasAFail = True
                if self.daysLeft > 0:
                    self.calculateDaysLeft()
                    self.sConnectionStep = "getdatamonths"
                    self.getData("urlCdcJour", self.dateBeginMonth, self.dateEndMonth)
                else:
                    self.sConnectionStep = "idle"
                    Domoticz.Log("Done")

        if (self.sConnectionStep == "idle"):
                if self.bHasAFail:
                        self.setNextConnection(False)            
                Domoticz.Log("Next connection: " + datetimeToSQLDateTimeString(self.nextConnection))

    def onStart(self):
        Domoticz.Debug("onStart called")
        Domoticz.Log("This plugin is compatible with Domoticz version 3.9517 onwards")
        Domoticz.Log("Username set to " + Parameters["Username"])
        if Parameters["Password"]:
            Domoticz.Log("Password is set")
        else:
            Domoticz.Log("Password is not set")
        Domoticz.Log("Days to grab for days view set to " + Parameters["Mode1"])
        Domoticz.Log("Days to grab for others view set to " + Parameters["Mode2"])
        Domoticz.Log("Debug set to " + Parameters["Mode3"])
        # most init
        self.__init__()
        
        try:
            self.historyDays = int(Parameters["Mode1"])
        except ValueError:
            self.historyDays = 7
        if self.historyDays < 1:
            self.historyDays = 1
        elif self.historyDays > 7:
            self.historyDays = 7
        Domoticz.Log("If you don't see enough data in days view of the device log, expand Short Log Sensors value the in Setup/Settings/Log History")
            
        try:
            self.historyMonths = int(Parameters["Mode2"])
        except ValueError:
            self.historyMonths = 366
        if self.historyMonths < 28:
            self.historyMonths = 28
        elif self.historyMonths > 100000:
            self.historyMonths = 100000

        # enable debug if required
        if Parameters["Mode3"] == "Debug":
            Domoticz.Debugging(1)            

        self.createDevice()

        self.nextConnection = datetime.now()
        
        self.isStarted = True

    def onStop(self):
        Domoticz.Debug("onStop called")
        # prevent error messages during disabling plugin
        self.isStarted = False

    def onConnect(self, Connection, Status, Description):
        Domoticz.Debug("onConnect called")
        if self.isStarted and (Connection == self.httpConn):
            self.handleConnection()

    def onMessage(self, Connection, Data):
        Domoticz.Debug("onMessage called")
        
        # if started and not stopping
        if self.isStarted and (Connection == self.httpConn):
            self.handleConnection(Data)

    def onDisconnect(self, Connection):
        Domoticz.Debug("onDisconnect called")
        
    def onHeartbeat(self):
        Domoticz.Debug("onHeartbeat() called")
        
        if datetime.now() > self.nextConnection:
            self.savedDateEndMonth = self.nextConnection
            self.setNextConnection(True)

            self.dateBeginDay = self.savedDateEndMonth - timedelta(days=(self.historyDays + 1))
            self.dateEndDay = self.savedDateEndMonth

            self.daysLeft = self.historyMonths
            self.calculateDaysLeft()
            self.handleConnection()

global _plugin
_plugin = BasePlugin()

def onStart():
    global _plugin
    _plugin.onStart()

def onStop():
    global _plugin
    _plugin.onStop()

def onConnect(Connection, Status, Description):
    global _plugin
    _plugin.onConnect(Connection, Status, Description)

def onMessage(Connection, Data):
    global _plugin
    _plugin.onMessage(Connection, Data)

def onCommand(Unit, Command, Level, Hue):
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Hue)

def onDeviceAdded(Unit):
    global _plugin

def onDeviceModified(Unit):
    global _plugin

def onDeviceRemoved(Unit):
    global _plugin

def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    global _plugin
    _plugin.onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile)

def onDisconnect(Connection):
    global _plugin
    _plugin.onDisconnect(Connection)

def onHeartbeat():
    global _plugin
    _plugin.onHeartbeat()

# Generic helper functions
def dictToQuotedString(dParams):
    result = ""
    for sKey, sValue in dParams.items():
        if result:
            result += "&"
        result += sKey + "=" + quote(str(sValue))
    return result

def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            Domoticz.Debug( "'" + x + "':'" + str(Parameters[x]) + "'")
    Domoticz.Debug("Device count: " + str(len(Devices)))
    for x in Devices:
        Domoticz.Debug("Device:           " + str(x) + " - " + str(Devices[x]))
        Domoticz.Debug("Device ID:       '" + str(Devices[x].ID) + "'")
        Domoticz.Debug("Device Name:     '" + Devices[x].Name + "'")
        Domoticz.Debug("Device iValue:    " + str(Devices[x].iValue))
        Domoticz.Debug("Device sValue:   '" + Devices[x].sValue + "'")
        Domoticz.Debug("Device LastLevel: " + str(Devices[x].LastLevel))
    return

def enerdisDateToDatetime(datetimeStr):
    #Buggy
    #return datetime.strptime(datetimeStr, dateFormat)
    #Not buggy
    return datetime(*(time.strptime(datetimeStr, "%d/%m/%Y")[0:6]))

def datetimeToEnderdisDateString(datetimeObj):
    return datetimeObj.strftime("%d/%m/%Y")

def datetimeToSQLDateString(datetimeObj):
    return datetimeObj.strftime("%Y-%m-%d")

def datetimeToSQLDateTimeString(datetimeObj):
    return datetimeObj.strftime("%Y-%m-%d %H:%M:%S")

def DumpDictToLog(dictToLog):
    if Parameters["Mode4"] == "Debug":
        if isinstance(dictToLog, dict):
            Domoticz.Debug("Dict details ("+str(len(dictToLog))+"):")
            for x in dictToLog:
                if isinstance(dictToLog[x], dict):
                    Domoticz.Debug("--->'"+x+" ("+str(len(dictToLog[x]))+"):")
                    for y in dictToLog[x]:
                        if isinstance(dictToLog[x][y], dict):
                            for z in dictToLog[x][y]:
                                Domoticz.Debug("----------->'" + z + "':'" + str(dictToLog[x][y][z]) + "'")
                        else:
                            Domoticz.Debug("------->'" + y + "':'" + str(dictToLog[x][y]) + "'")
                else:
                    Domoticz.Debug("--->'" + x + "':'" + str(dictToLog[x]) + "'")
