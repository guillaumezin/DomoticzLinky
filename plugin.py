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
<plugin key="linky" name="Linky" author="Barberousse" version="2.0.0-sandbox" externallink="https://github.com/guillaumezin/DomoticzLinky">
    <params>
        <param field="Mode5" label="Consommation à montrer sur le tableau de bord" width="200px">
            <options>
                <option label="Journée dernière" value="day"  default="true" />
                <option label="Semaine en cours" value="cweek" />
                <option label="Semaine dernière" value="lweek"  />
                <option label="Mois en cours" value="cmonth" />
                <option label="Mois dernier" value="lmonth"  />
                <option label="Année en cours" value="year"  />
                <option label="Pic journée dernière" value="peak_day"/>
                <option label="Pic semaine en cours" value="peak_cweek" />
                <option label="Pic semaine dernière" value="peak_lweek"  />
                <option label="Pic mois en cours" value="peak_cmonth" />
                <option label="Pic mois dernier" value="peak_lmonth"  />
                <option label="Pic année en cours" value="peak_year"  />
            </options>
        </param>
        <param field="Mode1" label="Nombre de jours à récupérer pour la vue par heures (0 min, pour désactiver la récupération par heures, 7 max)" width="50px" required="false" default="7"/>
        <param field="Mode2" label="Nombre de jours à récupérer pour les autres vues (1095 max)" width="50px" required="false" default="365"/>
        <param field="Mode3" label="Debug" width="170px">
            <options>
                <option label="Non" value="0"  default="true" />
                <option label="Simple" value="1"/>
                <option label="Avancé" value="2"/>
                <option label="Reset consentement" value="3"/>
            </options>
        </param>
    </params>
</plugin>
"""

# https://www.domoticz.com/wiki/Developing_a_Python_plugin

import Domoticz
import sys
from base64 import b64encode
import json
from urllib.parse import quote
import re
from datetime import datetime
from datetime import timedelta
from datetime import time
from time import strptime
#from random import randint
import html

CLIENT_ID = "9c551777-9d1b-447c-9e68-bfe6896ee002"

LOGIN_BASE_URI = "opensrcdev.alwaysdata.net"
LOGIN_BASE_PORT = "443"
# Sandbox
API_BASE_URI = "gw.hml.api.enedis.fr"
# Production
#API_BASE_URI = "gw.prd.api.enedis.fr"
API_BASE_PORT = "443"

VERIFY_CODE_URI = "https://opensrcdev.alwaysdata.net/domoticzlinkyconnect/auth/verify_code?code="

API_ENDPOINT_DEVICE_CODE = "/domoticzlinkyconnect/device/code"
API_ENDPOINT_DEVICE_TOKEN = "/domoticzlinkyconnect/device/token"
API_ENDPOINT_PROXY = "/domoticzlinkyconnect/device/proxy"
API_ENDPOINT_DATA_CONSUMPTION_LOAD_CURVE = '/v3/metering_data/consumption_load_curve'
API_ENDPOINT_DATA_CONSUMPTION_MAX_POWER = '/v3/metering_data/consumption_max_power'
API_ENDPOINT_DATA_DAILY_CONSUMPTION = '/v3/metering_data/daily_consumption'

#HEADERS = {
    #'Accept':'application/json, text/javascript, */*; q=0.01',
    #'Accept-Language':'fr,fr-FR;q=0.8,en;q=0.6',
    #"Content-Type": "application/x-www-form-urlencoded",
    #"Connection": "keep-alive",
    #"X-Requested-With": "XMLHttpRequest",
    #'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'
#}
HEADERS = {
    "Accept" : "application/json",
    #"Connection" : "keep-alive",
    "Content-Type" : "application/x-www-form-urlencoded"
}

class BasePlugin:
    # boolean: is plugin isEnabled
    isEnabled = True
    # boolean: to check that we are started, to prevent error messages when disabling or restarting the plugin
    isStarted = None
    # object: http connection for login
    httpLoginConn = None
    # object: http connection for data
    httpDataConn = None
    # integer: index of the Linky device
    iIndexUnit = 1
    # string: name of the Linky device
    sDeviceName = "Linky"
    # string: description of the Linky device
    sDescription = "Compteur Linky"
    # integer: type (pTypeGeneral)
    iType = 0xF3
    # integer: subtype (sTypeManagedCounter)
    iSubType = 0x21
    # integer: switch type (Energy)
    iSwitchType = 0
    # string: step name of the state machine
    sConnectionStep = None
    # string: step name of the next state machine during connection
    sConnectionNextStep = None
    # boolean: true if a step failed
    bHasAFail = None
    # dict: cookies
    dCookies = None
    # datetime: start date for short log
    dateBeginHours = None
    # datetime: end date for short log
    dateEndHours = None
    # datetime: start date for history
    dateBeginDays = None
    # datetime: end date for history
    dateEndDays = None
    # integer: number of days of data to grab for short log
    iHistoryDaysForHoursView = None
    # integer: number of days of data to grab for history
    iHistoryDaysForDaysView = None
    # integer: number of days left fot next batch of data
    iDaysLeft = None
    # datetime: backup end date
    savedDateEndDays = None
    # datetime: backup 2 end date
    savedDateEndDays2 = None
    # boolean: is this the batch of the most recent history
    bFirstMonths = None
    # string: usage point id
    sUsagePointId = None
    # string: consumption to show = current week ("cweek"), the previous week ("lweek", the current month ("cmonth"), the previous month ("lmonth"), or year ("cyear"), prefix "peak_" for peak calculation
    sConsumptionType = None
    # boolean: auto accept terms
    bAutoAcceptTerms = None
    # integer: number of days for hours view
    iHistoryDaysForHoursView = None
    # integer: number of other view (peak)
    iHistoryDaysForPeakDaysView = None
    # boolean: debug mode
    iDebugLevel = None
    # previous day
    pday = None
    # first day of month
    fdmonth = None
    # last day of previous month
    ldpmonth = None
    # first day of previous month
    fdpmonth = None
    # first day of week
    fdweek = None
    # last day of previous week
    ldpweek = None
    # first day of previous week
    fdpweek = None
    # first day of year
    fdyear = None
    # received device code
    sDeviceCode = None
    # interval to ask for device authorization
    iInterval = 5
    # peak mode
    bPeakMode = None
    # send nuffer
    sBuffer = None
    
    def __init__(self):
        self.isStarted = False
        self.httpLoginConn = None
        self.httpDataConn = None
        self.sConnectionStep = "idle"
        self.bHasAFail = False
        self.sBuffer = None
        
    def myDebug(self, message):
        if self.iDebugLevel:
            Domoticz.Log(message)

    # Prepare buffer and connect
    def connectAndSend(self, conn, data, address, port):
        self.sBuffer = data
        self.sConnectionNextStep = self.sConnectionStep
        self.sConnectionStep = "connecting"
        conn = Domoticz.Connection(Name="HTTPS connection", Transport="TCP/IP", Protocol="HTTPS", Address=address, Port=port)
        conn.Connect()
        return conn

    # Connect for login
    def connectAndSendForAuthorize(self, data):
        self.httpLoginConn = self.connectAndSend(self.httpLoginConn, data, LOGIN_BASE_URI, LOGIN_BASE_PORT)
        
    # Connect for metering data
    def connectAndSendForMetering(self, data):
        self.httpDataConn = self.connectAndSend(self.httpDataConn, data, API_BASE_URI, API_BASE_PORT)

    # get default headers
    def initHeaders(self, uri):
        headers = dict(HEADERS)
        headers["Host"] = uri;
        return headers

    # get access token
    def getDeviceCode(self):
        headers = self.initHeaders(LOGIN_BASE_URI + ":" + LOGIN_BASE_PORT)
        
        postData = {
            "client_id": CLIENT_ID
        }
        
        sendData = {
                    "Verb" : "POST",
                    "URL"  : API_ENDPOINT_DEVICE_CODE,
                    "Headers" : headers,
                    "Data" : dictToQuotedString(postData)
        }
        
        self.dumpDictToLog(sendData)
        self.connectAndSendForAuthorize(sendData)

    def showStatusError(self, hours, Data):
        sErrorSentence = "Erreur status : " + str(getStatus(Data))
        if Data and ("Data" in Data):
            try:
                dJson = json.loads(Data["Data"].decode())
            except ValueError:
                self.showSimpleStepError(sErrorSentence)
            else:
                if dJson and ("error" in dJson):
                    sErrorSentence = sErrorSentence + " - code : " + dJson["error"]
                if dJson and ("error_description" in dJson):
                    sErrorSentence = sErrorSentence + " - description : " + dJson["error_description"]
                if dJson and ("error_uri" in dJson):
                    sErrorSentence = sErrorSentence + " - URI : " + dJson["error_uri"]
        self.showStepError(hours, sErrorSentence)

    def showSimpleStatusError(self, Data):
        sErrorSentence = "Erreur status : " + str(getStatus(Data))
        if Data and ("Data" in Data):
            try:
                dJson = json.loads(Data["Data"].decode())
            except ValueError:
                self.showSimpleStepError(sErrorSentence)
            else:
                if dJson and ("error" in dJson):
                    sErrorSentence = sErrorSentence + " - code " + dJson["error"]
                if dJson and ("error_description" in dJson):
                    sErrorSentence = sErrorSentence + " - description : " + dJson["error_description"]
                if dJson and ("error_uri" in dJson):
                    sErrorSentence = sErrorSentence + " - URI : " + dJson["error_uri"]
        self.showSimpleStepError(sErrorSentence)

    def parseDeviceCode(self, Data):
        self.dumpDictToLog(Data)
        if getStatus(Data) == 200:
            if Data and ("Data" in Data):
                try:
                    dJson = json.loads(Data["Data"].decode())
                except ValueError as err:
                    self.showSimpleStepError("Les données reçues ne sont pas du JSON : " + str(err))
                    return False
                count = 0
                if dJson and ("device_code" in dJson):
                    self.sDeviceCode = dJson["device_code"]
                    count = count + 1
                if dJson and ("user_code" in dJson):
                    sUserCode = dJson["user_code"]
                    count = count + 1
                if count == 2:
                    Domoticz.Error("Connectez-vous à l'adresse " + VERIFY_CODE_URI + quote(sUserCode) + " pour lancer la demande de consentement")
                    return True
            else:
                self.showSimpleStepError("Pas de données reçue")
        else:
            self.showSimpleStatusError(Data)
        return False
        
    # get access token
    def getAccessToken(self):
        headers = self.initHeaders(LOGIN_BASE_URI + ":" + LOGIN_BASE_PORT)
        
        postData = {
            "client_id" : CLIENT_ID,
            "grant_type" : "urn:ietf:params:oauth:grant-type:device_code",
            "device_code" : self.sDeviceCode
        }
        
        sendData = {
                    "Verb" : "POST",
                    "URL"  : API_ENDPOINT_DEVICE_TOKEN,
                    "Headers" : headers,
                    "Data" : dictToQuotedString(postData)
        }
        
        self.dumpDictToLog(sendData)
        self.connectAndSendForAuthorize(sendData)

    # Refresh token
    def refreshToken(self):
        headers = self.initHeaders(LOGIN_BASE_URI + ":" + LOGIN_BASE_PORT)

        postData = {
            "grant_type" : "refresh_token",
            "client_id" : CLIENT_ID,
            "refresh_token" : getConfigItem("refresh_token", "")
        }

        sendData = {
                    "Verb" : "POST",
                    "URL"  : API_ENDPOINT_PROXY,
                    "Headers" : headers,
                    "Data" : dictToQuotedString(postData)
        }
        
        self.dumpDictToLog(sendData)
        self.connectAndSendForAuthorize(sendData)
        
    # Parse access token
    def parseAccessToken(self, Data):
        self.dumpDictToLog(Data)
        if getError(Data) == "authorization_pending":
            self.myDebug("pending")
            if Data and ("Data" in Data):
                try:
                    dJson = json.loads(Data["Data"].decode())
                except ValueError as err:
                    self.showSimpleStepError("Les données reçues ne sont pas du JSON : " + str(err))
                    return False
                if dJson and ("interval" in dJson):
                        try:
                            self.iInterval = int(dJson["interval"])
                        except:
                            self.iInterval = 5
            return "pending";
        elif getError(Data) == "invalid_grant":
            resetTokens()
            self.showSimpleStatusError(Data)
        elif getStatus(Data) == 200:
            if Data and ("Data" in Data):
                try:
                    dJson = json.loads(Data["Data"].decode())
                except ValueError as err:
                    self.showSimpleStepError("Les données reçues ne sont pas du JSON : " + str(err))
                    return False
                if dJson and ("usage_point_id" in dJson):
                    setConfigItem("usage_point_id", dJson["usage_point_id"])
                count = 0
                if dJson and ("refresh_token" in dJson):
                    setConfigItem("refresh_token", dJson["refresh_token"])
                    count = count + 1
                if dJson and ("access_token" in dJson):
                    setConfigItem("access_token", dJson["access_token"])
                    count = count + 1
                if dJson and ("token_type" in dJson):
                    setConfigItem("token_type", dJson["token_type"])
                    count = count + 1
                if count == 3:
                    return "done"
                else:
                    self.showSimpleStepError("Pas assez de données reçue")
            else:
                self.showSimpleStepError("Pas de données reçue")
        else:
            self.showSimpleStatusError(Data)
        return "error"
        
    # Get data
    def getData(self, uri, start, end):
        headers = self.initHeaders(API_BASE_URI + ":" + API_BASE_PORT)
        headers["Authorization"] = getConfigItem("token_type", "") + " " + getConfigItem("access_token", "")
        
        query = {
            "start" : datetimeToEnedisDateString(start),
            "end" : datetimeToEnedisDateString(end),
            "usage_point_id" : getConfigItem("usage_point_id", "")
        }
        
        sendData = {
            "Verb" : "GET",
            "URL"  : uri + "?" + dictToQuotedString(query),
            "Headers" : headers
        }
        
        self.dumpDictToLog(sendData)
        self.connectAndSendForMetering(sendData)

    # Create Domoticz device
    def createDevice(self):
        # Only if not already done
        if not self.iIndexUnit in Devices:
            Domoticz.Device(Name=self.sDeviceName,  Unit=self.iIndexUnit, Type=self.iType, Subtype=self.iSubType, Switchtype=self.iSwitchType, Description=self.sDescription, Used=1).Create()
            if not (self.iIndexUnit in Devices):
                Domoticz.Error("Ne peut ajouter le dispositif Linky à la base de données. Vérifiez dans les paramètres de Domoticz que l'ajout de nouveaux dispositifs est autorisé")
                return False
        return True

    # Create device and insert usage in Domoticz DB
    def createAndAddToDevice(self, usage, Date):
        if not self.createDevice():
            return False
        # -1.0 for counter because Linky doesn't provide absolute counter value via Enedis website
        sValue = "-1.0;"+ str(usage) + ";"  + str(Date)
        self.myDebug("Mets dans la BDD la valeur " + sValue)
        Devices[self.iIndexUnit].Update(nValue=0, sValue=sValue, Type=self.iType, Subtype=self.iSubType, Switchtype=self.iSwitchType)
        return True

    # Update value shown on Domoticz dashboard
    def updateDevice(self, usage):
        if not self.createDevice():
            return False
        # -1.0 for counter because Linky doesn't provide absolute counter value via Enedis website
        sValue="-1.0;"+ str(usage)
        self.myDebug("Mets sur le tableau de bord la valeur " + sValue)
        Devices[self.iIndexUnit].Update(nValue=0, sValue=sValue, Type=self.iType, Subtype=self.iSubType, Switchtype=self.iSwitchType)
        return True

    # Show error in state machine context
    def showSimpleStepError(self, logMessage):
        Domoticz.Error(logMessage + " durant l'étape " + self.sConnectionStep)

    # Show error in state machine context with dates
    def showStepError(self, hours, logMessage):
        if hours:
            Domoticz.Error(logMessage + " durant l'étape " + self.sConnectionStep + " de " + datetimeToEnedisDateString(self.dateBeginHours) + " à " + datetimeToEnedisDateString(self.dateEndHours))
        else:
            Domoticz.Error(logMessage + " durant l'étape " + self.sConnectionStep + " de " + datetimeToEnedisDateString(self.dateBeginDays) + " à " + datetimeToEnedisDateString(self.dateEndDays))

    # Grab hours data inside received JSON data for short log
    def exploreDataHours(self, Data):
        self.dumpDictToLog(Data)
        if Data and ("Data" in Data):
            try:
                dJson = json.loads(Data["Data"].decode())
            except ValueError as err:
                self.showStepError(True, "Les données reçues ne sont pas du JSON : " + str(err))
                return False
            except TypeError as err:
                self.showStepError(True, "Le type de données reçues n'est pas JSON : " + str(err))
                return False
            except:
                self.showStepError(True, "Erreur dans les données JSON : " + str(sys.exc_info()[0]))
                return False
            else:
                if dJson and ("usage_point" in dJson):
                    try:
                        beginDate = enedisDateToDatetime(dJson["usage_point"][0]["meter_reading"]["start"])
                        endDate = enedisDateToDatetime(dJson["usage_point"][0]["meter_reading"]["end"])
                    except (TypeError, ValueError) as err:
                        self.showStepError(True, "Erreur dans le format de donnée de date JSON : " + str(err))
                        return False
                    except:
                        self.showStepError(True, "Erreur dans la donnée de date JSON : " + str(sys.exc_info()[0]) + dJson["graphe"]["periode"]["dateDebut"] + dJson["graphe"]["periode"]["dateFin"])
                        return False
                    # We accumulate data because Enedis sends kWh for every 30 minutes and Domoticz expects data only for every hour
                    accumulation = 0.0
                    currentDay = -1
                    steps = 1.0
                    dataSeenToTheEnd = False
                    for index, data in enumerate(dJson["usage_point"][0]["meter_reading"]["interval_reading"]):
                        try:
                            val = float(data["value"])
                            rank = int(data["rank"])
                        except:
                            val = -1.0
                            rank = index
                        if (val >= 0.0):
                            # Shift to +1 hour for Domoticz, because bars/hours for graph are shifted to -1 hour in Domoticz, cf. constructTime() call in WebServer.cpp
                            # Enedis and Domoticz doesn't set the same date for used energy, add offset
                            curDate = beginDate + timedelta(hours=1, minutes=((rank+1)*30))
                            #Domoticz.Log("date " + datetimeToSQLDateTimeString(curDate) + " " + datetimeToSQLDateTimeString(endDate))
                            accumulation = accumulation + val
                            #Domoticz.Log("Value " + str(val) + " " + datetimeToSQLDateTimeString(curDate))
                            if curDate.minute == 0:
                                # Check that we had enough data, as expected
                                if curDate >= endDate:
                                    #Domoticz.Log("Last val")
                                    dataSeenToTheEnd = True
                                #Domoticz.Log("accumulation " + str(accumulation / steps) + " " + datetimeToSQLDateTimeString(curDate))
                                if not self.createAndAddToDevice(accumulation / steps, datetimeToSQLDateTimeString(curDate)):
                                    return False
                                accumulation = 0.0
                                steps = 0.0
                            steps = steps + 1.0
                    if not dataSeenToTheEnd:
                        self.showStepError(True, "Données manquantes")                        
                    return dataSeenToTheEnd
                else:
                    self.showStepError(True, "Erreur à la réception de données JSON")
        else:
            self.showStepError(True, "Aucune donnée reçue")
        return False
    
    # Reset counters for power consumption
    def resetDayAccumulate(self):
        self.pday = self.dateEndDays.replace(hour=0, minute=0, second=0, microsecond=0)
        endDate = self.pday + timedelta(days=1)
        self.daysCalculate = 0.0
        self.fdmonth = endDate.replace(day=1)
        self.ldpmonth = self.fdmonth - timedelta(days=1)
        self.fdpmonth = self.ldpmonth.replace(day=1)
        self.fdweek = endDate - timedelta(days=endDate.weekday())
        self.ldpweek = self.fdweek - timedelta(days=1)
        self.fdpweek = self.ldpweek - timedelta(days=6)
        self.fdyear = endDate.replace(day=1,month=1)
        #Domoticz.Log(str(self.pday) + " " + str(endDate) + " " + str(self.fdmonth) + " " + str(self.ldpmonth) + " " + str(self.fdpmonth) + " " + str(self.fdweek) + " " + str(self.ldpweek) + " " + str(self.fdpweek) + " " + str(self.fdyear))

    # Accumulate power consumption
    def dayAccumulate(self, curDate, val):
        bDoIt = False
        if self.sConsumptionType.endswith("cweek"):
            if (curDate >= self.fdweek):
                #Domoticz.Log(str(curDate) + " " + str(val) + " " + str(self.daysCalculate))
                bDoIt = True
        elif self.sConsumptionType.endswith("lweek"):
            if (self.fdpweek <= curDate <= self.ldpweek):
                #Domoticz.Log(str(curDate) + " " + str(val) + " " + str(self.daysCalculate))
                bDoIt = True
        elif self.sConsumptionType.endswith("cmonth"):
            if (curDate >= self.fdmonth):
                #Domoticz.Log(str(curDate) + " " + str(val) + " " + str(self.daysCalculate))
                bDoIt = True
        elif self.sConsumptionType.endswith("lmonth"):
            if (self.fdpmonth <= curDate <= self.ldpmonth):
                #Domoticz.Log(str(curDate) + " " + str(val) + " " + str(self.daysCalculate))
                bDoIt = True
        elif self.sConsumptionType.endswith("year"):
            if (curDate >= self.fdyear):
                #Domoticz.Log(str(curDate) + " " + str(val) + " " + str(self.daysCalculate))
                self.daysCalculate = self.daysCalculate + val
        elif curDate == self.pday:
            #Domoticz.Log(str(curDate) + " " + str(self.pday) + " " + str(val) + " " + str(self.daysCalculate))
            self.daysCalculate = val;
        if bDoIt:
            self.daysCalculate = self.daysCalculate + val
    
    # Look for max power consumption
    def getMax(self, curDate, val):
        bDoIt = False
        if self.sConsumptionType.endswith("cweek"):
            if (curDate >= self.fdweek):
                #Domoticz.Log(str(curDate) + " " + str(val) + " " + str(self.daysCalculate))
                bDoIt = True
        elif self.sConsumptionType.endswith("lweek"):
            if (self.fdpweek <= curDate <= self.ldpweek):
                #Domoticz.Log(str(curDate) + " " + str(val) + " " + str(self.daysCalculate))
                bDoIt = True
        elif self.sConsumptionType.endswith("cmonth"):
            if (curDate >= self.fdmonth):
                #Domoticz.Log(str(curDate) + " " + str(val) + " " + str(self.daysCalculate))
                bDoIt = True
        elif self.sConsumptionType.endswith("lmonth"):
            if (self.fdpmonth <= curDate <= self.ldpmonth):
                #Domoticz.Log(str(curDate) + " " + str(val) + " " + str(self.daysCalculate))
                bDoIt = True
        elif self.sConsumptionType.endswith("year"):
            if (curDate >= self.fdyear):
                #Domoticz.Log(str(curDate) + " " + str(val) + " " + str(self.daysCalculate))
                bDoIt = True
        elif curDate == self.pday:
            #Domoticz.Log(str(curDate) + " " + str(self.pday) + " " + str(val) + " " + str(self.daysCalculate))
            self.daysCalculate = val;
        if bDoIt:
            if val > self.daysCalculate:
                self.daysCalculate = val            
    
    # Grab days data inside received JSON data for history
    def exploreDataDays(self, Data, bPeak):
        self.dumpDictToLog(Data)
        if Data and "Data" in Data:
            try:
                dJson = json.loads(Data["Data"].decode())
            except ValueError as err:
                self.showStepError(False, "Les données reçues ne sont pas du JSON : " + str(err))
                return False
            except TypeError as err:
                self.showStepError(False, "Le type de données reçues n'est pas JSON : " + str(err))
                return False
            except:
                self.showStepError(False, "Erreur dans les données JSON : " + str(sys.exc_info()[0]))
                return False
            else:
                if dJson and ("usage_point" in dJson):
                    try:
                        beginDate = enedisDateToDatetime(dJson["usage_point"][0]["meter_reading"]["start"])
                        endDate = enedisDateToDatetime(dJson["usage_point"][0]["meter_reading"]["end"])
                    except ValueError as err:
                        self.showStepError(False, "Erreur dans le format de donnée de date JSON : " + str(err))
                        return False
                    except:
                        self.showStepError(False, "Erreur dans la donnée de date JSON : " + str(sys.exc_info()[0]))
                        return False
                    for index, data in enumerate(dJson["usage_point"][0]["meter_reading"]["interval_reading"]):
                        try:
                            val = float(data["value"])
                            rank = int(data["rank"]) - 1
                        except:
                            val = -1.0
                            rank = index
                        if (val >= 0.0):
                            curDate = beginDate + timedelta(days=rank)
                            #Domoticz.Log("Value " + str(val) + " " + datetimeToSQLDateString(curDate))
                            #self.dumpDictToLog(values)
                            if bPeak:
                                self.getMax(curDate, val)
                            else:
                                self.dayAccumulate(curDate, val)
                                if not self.createAndAddToDevice(val, datetimeToSQLDateString(curDate)):
                                    return False
                    return True
                else:
                    self.showStepError(False, "Erreur à la réception de données JSON")
        else:
            self.showStepError(False, "Aucune donnée reçue")
        return False

    # Update dashboard with accumulated value
    def updateDashboard(self):
        return self.updateDevice(self.daysCalculate)
        
    # Calculate days and date left for next batch
    def resetDates(self, dDateEnd = None):
        if dDateEnd:
            self.savedDateEndDays = dDateEnd
            self.savedDateEndDays2 = self.savedDateEndDays
            self.iDaysLeft = self.iHistoryDaysForDaysView
        else:
            self.savedDateEndDays = self.savedDateEndDays2
            self.iDaysLeft = self.iHistoryDaysForPeakDaysView
        
        self.dateBeginHours = self.savedDateEndDays - timedelta(days=self.iHistoryDaysForHoursView)
        self.dateEndHours = self.savedDateEndDays
        
        self.calculateDaysLeft()
        self.resetDayAccumulate()
        
    # Calculate days and date left for next batch
    def calculateDaysLeft(self):
        # No more than 365 days at once
        self.iDaysLeft = self.iDaysLeft - 365
        if self.iDaysLeft <= 0:
            daysToGet = self.iDaysLeft + 365
        else:
            daysToGet = 365
        self.dateBeginDays = self.savedDateEndDays - timedelta(days=daysToGet)
        self.dateEndDays = self.savedDateEndDays - timedelta(days=1)
        self.savedDateEndDays = self.dateBeginDays
        #Domoticz.Log("Dates : " + datetimeToSQLDateTimeString(self.dateBeginDays) + " " + datetimeToSQLDateTimeString(self.dateEndDays) + " " + datetimeToSQLDateTimeString(self.savedDateEndDays))

    # Calculate next complete grab, for tomorrow between 5 and 6 am if tomorrow is true, for next hour otherwise
    def setNextConnection(self, tomorrow):
        if tomorrow:
            self.nextConnection = datetime.now() + timedelta(days=1)
            self.nextConnection = self.nextConnection.replace(hour=5)
        else:
            self.nextConnection = datetime.now() + timedelta(hours = 1)
        # Randomize minutes to lower load on Enedis website
        #randint makes domoticz crash on RPI
        #self.nextConnection = self.nextConnection + timedelta(minutes=randint(0, 59), seconds=randint(0, 59))
        # We take microseconds to randomize
        minutesRand = round(datetime.now().microsecond / 10000) % 60
        self.nextConnection = self.nextConnection + timedelta(minutes=minutesRand)

    # Calculate next connection for device authorization
    def setNextConnectionForAuthorization(self, iInterval):
        self.nextConnection = datetime.now() + timedelta(seconds=iInterval)
        
    # Handle the connection state machine
    def handleConnection(self, Data = None):
        self.myDebug("Etape " + self.sConnectionStep)
        
        # First and last step
        if self.sConnectionStep == "idle":
            Domoticz.Log("Récupération des données...")
            # Reset failed state
            self.bHasAFail = False

            # If we have access tokens, try do grab data, otherwise ask for tokens
            if (getConfigItem("access_token", "") and getConfigItem("usage_point_id", "")) :
                self.sConnectionStep = "getdatadays"
                self.getData(API_ENDPOINT_DATA_DAILY_CONSUMPTION, self.dateBeginDays, self.dateEndDays)
            else :
                self.sConnectionStep = "parsedevicecode"
                self.getDeviceCode()

        # We should never reach this
        elif self.sConnectionStep == "connecting":
            self.showSimpleStepError("Timeout à la connexion")
            self.bHasAFail = False
                
        # We should never reach this
        elif self.sConnectionStep == "nothingtosend":
            self.showSimpleStepError("Erreur à la connexion")
            self.bHasAFail = False

        # Did we get a device code ?
        elif self.sConnectionStep == "parsedevicecode":
            if self.parseDeviceCode(Data):
                self.sConnectionStep = "parseaccesstoken"
                self.getAccessToken()
            else:
                self.sConnectionStep = "idle"
                self.bHasAFail = True
            
        # Wait for user to complete authorization process with his web browser
        elif self.sConnectionStep == "askagainaccesscode":
            # We must stay connected until completion, otherwise = error
            if not self.httpLoginConn.Connected():
                self.showSimpleStepError("Redemande du jeton d'accès")
                self.sConnectionStep = "idle"
                self.bHasAFail = True
            # Got answer, parse it
            else:
                self.sConnectionStep = "parseaccesstoken"
                self.getAccessToken()
            
        # Parse for access token
        elif self.sConnectionStep == "parseaccesstoken":
            result = self.parseAccessToken(Data)
            if result == "done":
                self.sConnectionStep = "getdatadays"
                # Ask data for days
                self.getData(API_ENDPOINT_DATA_DAILY_CONSUMPTION, self.dateBeginDays, self.dateEndDays)
            elif result == "error":
                self.isEnabled = False
                self.showSimpleStepError("Le plugin va être arrêté. Relancez le en vous rendant dans Configuration/Matériel, en cliquant sur le plugin puis sur Modifier. Surveillez les logs pour obtenir le lien afin de renouveler le consentement pour la récupération des données auprès d'Enedis")
            # Wait for user to complete authorization process with his web browser
            else:
                self.sConnectionStep = "askagainaccesscode"
                self.setNextConnectionForAuthorization(self.iInterval)
            
        # Ask data for days or peak data
        elif self.sConnectionStep == "getdatadays" or self.sConnectionStep == "getdatapeakdays":
            # Check if access token still valid
            status = getStatus(Data)
            # status 403 = token not valid, needs refresh
            if status == 403:
                self.sConnectionStep = "parseaccesstoken"
                self.refreshToken()
            elif status != 200:
                self.showStatusError(False, Data)
                self.sConnectionStep = "idle"
                self.bHasAFail = True
            else:
                # Analyse data for days
                if self.sConnectionStep == "getdatapeakdays" :
                    bPeak = True
                else:
                    bPeak = False
                if not self.exploreDataDays(Data, bPeak):
                    self.bHasAFail = True
                # Still data to get, another batch ?
                if self.iDaysLeft > 0:
                    self.calculateDaysLeft()
                    # Normal data or peak data ?
                    if bPeak:
                        self.sConnectionStep = "getdatapeakdays"
                        self.getData(API_ENDPOINT_DATA_CONSUMPTION_MAX_POWER, self.dateBeginDays, self.dateEndDays)
                    else:
                        self.sConnectionStep = "getdatadays"
                        self.getData(API_ENDPOINT_DATA_DAILY_CONSUMPTION, self.dateBeginDays, self.dateEndDays)
                else:
                    # If at end of data for days and for peaks, continue to data for hours or idle
                    if (not self.bPeakMode) or bPeak:
                        # Update data shown on dashboard
                        if not self.updateDashboard():
                            self.bHasAFail = True
                        # user set Mode1 to 0, he doesn't want to grab hours data
                        if self.iHistoryDaysForHoursView < 1:
                            self.sConnectionStep = "idle"
                            Domoticz.Log("Done")
                        # grab data for hours
                        else:
                            self.sConnectionStep = "getdatahours"
                            self.getData(API_ENDPOINT_DATA_CONSUMPTION_LOAD_CURVE, self.dateBeginHours, self.dateEndHours)
                    # Get peak data
                    else:
                        self.resetDates()
                        self.sConnectionStep = "getdatapeakdays"
                        self.getData(API_ENDPOINT_DATA_CONSUMPTION_MAX_POWER, self.dateBeginDays, self.dateEndDays)

        # Ask data for hours
        elif self.sConnectionStep == "getdatahours":
            # Check if access token still valid
            status = getStatus(Data)
            if status == 403:
                self.sConnectionStep = "parseaccesstoken"
                self.refreshToken()
            elif status == 404:
                self.showStatusError(True, Data)
                self.showStepError(True, "Avez-vous activé la courbe de charge sur le site d'Enedis ?")
                self.sConnectionStep = "idle"
                self.bHasAFail = True
            elif status != 200:
                self.showStatusError(True, Data)
                self.sConnectionStep = "idle"
                self.bHasAFail = True
            else:
                # Analyse data for hours
                if not self.exploreDataHours(Data):
                    self.bHasAFail = True
                self.sConnectionStep = "idle"
                Domoticz.Log("Fait")
                
        # Next connection time depends on success
        if self.sConnectionStep == "idle":
            if self.bHasAFail:
                self.setNextConnection(False)            
            Domoticz.Log("Prochaine connexion : " + datetimeToSQLDateTimeString(self.nextConnection))

    def dumpDictToLog(self, dictToLog):
        if self.iDebugLevel:
            if isinstance(dictToLog, dict):
                self.myDebug("Dict details ("+str(len(dictToLog))+"):")
                for x in dictToLog:
                    if isinstance(dictToLog[x], dict):
                        self.myDebug("--->'"+x+" ("+str(len(dictToLog[x]))+"):")
                        for y in dictToLog[x]:
                            if isinstance(dictToLog[x][y], dict):
                                for z in dictToLog[x][y]:
                                    self.myDebug("----------->'" + z + "':'" + str(dictToLog[x][y][z]) + "'")
                            else:
                                self.myDebug("------->'" + y + "':'" + str(dictToLog[x][y]) + "'")
                    else:
                        self.myDebug("--->'" + x + "':'" + str(dictToLog[x]) + "'")
            else:
                self.myDebug("Received no dict: " + str(dictToLog))
                        
    def onStart(self):
        self.myDebug("onStart called")
        
        Domoticz.Log("Ce plugin est compatible avec Domoticz version 3.9517 et plus récent, mais la vue par heure peut ne pas fonctionner avec la version 4.9700")
        
        # Even if not used, Username and Password may still be in database because of previous versions. We don't want them, as it triggers an unwanted HTTP basic autorization header in old Domoticz Python Framework
        Parameters.pop("Username", None)
        Parameters.pop("Password", None)
        
        self.iHistoryDaysForHoursView = Parameters["Mode1"]
        self.iHistoryDaysForDaysView = Parameters["Mode2"]
        self.sConsumptionType = Parameters["Mode5"]
        
        if self.sConsumptionType.startswith("peak_"):
            self.bPeakMode = True
        else:
            self.bPeakMode = False
            
        try:
            self.iDebugLevel = int(Parameters["Mode3"])
        except ValueError:
            self.iDebugLevel = 0
    
        if self.iDebugLevel > 1:
            Domoticz.Debugging(1)

        if self.iDebugLevel > 2:
            resetTokens()

        # History for short log is 7 days max (default to 7)
        try:
            self.iHistoryDaysForHoursView = int(self.iHistoryDaysForHoursView)
        except:
            self.iHistoryDaysForHoursView = 7
        if self.iHistoryDaysForHoursView < 0:
            self.iHistoryDaysForHoursView = 0
        elif self.iHistoryDaysForHoursView > 7:
            self.iHistoryDaysForHoursView = 7
            
        # History for short log is 1095 days max (default to 365)
        try:
            self.iHistoryDaysForDaysView = int(self.iHistoryDaysForDaysView)
        except:
            self.iHistoryDaysForDaysView = 365
        if self.iHistoryDaysForDaysView < 1:
            self.iHistoryDaysForDaysView = 1
        elif self.iHistoryDaysForDaysView > 1095:
            self.iHistoryDaysForDaysView = 1095
        self.iHistoryDaysForPeakDaysView = self.iHistoryDaysForDaysView


        if (self.sConsumptionType == "cweek") and (self.iHistoryDaysForDaysView < 7) :
            self.iHistoryDaysForDaysView = 7
            
        if (self.sConsumptionType == "lweek") and (self.iHistoryDaysForDaysView < 14) :
            self.iHistoryDaysForDaysView = 14
            
        if (self.sConsumptionType == "cmonth") and (self.iHistoryDaysForDaysView < 32) :
            self.iHistoryDaysForDaysView = 32

        if (self.sConsumptionType == "lmonth") and (self.iHistoryDaysForDaysView < 63) :
            self.iHistoryDaysForDaysView = 63

        if (self.sConsumptionType == "year") and (self.iHistoryDaysForDaysView < 366) :
            self.iHistoryDaysForDaysView = 366
            

        if (self.sConsumptionType == "peak_cweek") and (self.iHistoryDaysForPeakDaysView < 7) :
            self.iHistoryDaysForPeakDaysView = 7
            
        if (self.sConsumptionType == "peak_lweek") and (self.iHistoryDaysForPeakDaysView < 14) :
            self.iHistoryDaysForPeakDaysView = 14
            
        if (self.sConsumptionType == "peak_cmonth") and (self.iHistoryDaysForPeakDaysView < 32) :
            self.iHistoryDaysForPeakDaysView = 32

        if (self.sConsumptionType == "peak_lmonth") and (self.iHistoryDaysForPeakDaysView < 63) :
            self.iHistoryDaysForPeakDaysView = 63

        if (self.sConsumptionType == "peak_year") and (self.iHistoryDaysForPeakDaysView < 366) :
            self.iHistoryDaysForPeakDaysView = 366
            

        Domoticz.Log("Consommation à montrer sur le tableau de bord mis à " + self.sConsumptionType)
        Domoticz.Log("Accepter automatiquement les conditions d'utilisation mis à " + str(self.bAutoAcceptTerms))
        Domoticz.Log("Nombre de jours à récupérer pour la vue par heures mis à " + str(self.iHistoryDaysForHoursView))
        Domoticz.Log("Nombre de jours à récupérer pour les autres vues mis à " + str(self.iHistoryDaysForDaysView))
        if self.bPeakMode:
            Domoticz.Log("Nombre de jours à récupérer pour les autres vues (calcul du pic) mis à " + str(self.iHistoryDaysForPeakDaysView))
        Domoticz.Log("Debug mis à " + str(self.iDebugLevel))
        
        # most init
        self.__init__()

        Domoticz.Log("Si vous ne voyez pas assez de données dans la vue par heures, augmentez le paramètre Log des capteurs qui se trouve dans Réglages / Paramètres / Historique des logs")
        
        if self.createDevice():
            self.nextConnection = datetime.now()
        else:
            self.setNextConnection(False)            
        
        # Now we can enabling the plugin
        self.isStarted = True

    def onStop(self):
        Domoticz.Debug("onStop called")
        # prevent error messages during disabling plugin
        self.isStarted = False

    def onConnect(self, Connection, Status, Description):
        Domoticz.Debug("onConnect called")
        if self.isStarted and ((Connection == self.httpLoginConn) or (Connection == self.httpDataConn)):
            if self.sBuffer:
                self.sConnectionStep = self.sConnectionNextStep
                Connection.Send(self.sBuffer)
                self.sBuffer = None
            else:
                self.myDebug("Nothing to send")
                self.sConnectionStep = "nothingtosend"
                self.handleConnection()

    def onMessage(self, Connection, Data):
        Domoticz.Debug("onMessage called")
        
        # if started and not stopping
        if self.isStarted and ((Connection == self.httpLoginConn) or (Connection == self.httpDataConn)):
            self.handleConnection(Data)

    def onDisconnect(self, Connection):
        Domoticz.Debug("onDisconnect called")
        
    def onHeartbeat(self):
        Domoticz.Debug("onHeartbeat() called")
        
        if self.isEnabled and (datetime.now() > self.nextConnection):
            #self.savedDateEndDays = self.nextConnection
            self.resetDates(datetime(self.nextConnection.year, self.nextConnection.month, self.nextConnection.day))
            # We immediatly program next connection for tomorrow, if there is a problem, we will reprogram it sooner
            self.setNextConnection(True)
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
def getConfigItem(Key=None, Default={}):
    Value = Default
    try:
        Config = Domoticz.Configuration()
        if (Key != None):
            Value = Config[Key] # only return requested key if there was one
        else:
            Value = Config      # return the whole configuration if no key
    except KeyError:
        Value = Default
    except Exception as inst:
        Domoticz.Error("Domoticz.Configuration read failed: '"+str(inst)+"'")
    return Value
    
def setConfigItem(Key=None, Value=None):
    Config = {}
    try:
        Config = Domoticz.Configuration()
        if (Key != None):
            Config[Key] = Value
        else:
            Config = Value  # set whole configuration if no key specified
        Config = Domoticz.Configuration(Config)
    except Exception as inst:
        Domoticz.Error("Domoticz.Configuration operation failed: '"+str(inst)+"'")
    return Config
   
# Erase authorization tokens
def resetTokens():
    setConfigItem("usage_point_id", "")
    setConfigItem("token_type", "")
    setConfigItem("refresh_token", "")
    setConfigItem("access_token", "")

def dictToQuotedString(dParams):
    result = ""
    for sKey, sValue in dParams.items():
        if result:
            result += "&"
        result += sKey + "=" + quote(str(sValue))
    return result

# Grab error inside received JSON
def getError(Data):
    if Data and ("Data" in Data):
        try:
            dJson = json.loads(Data["Data"].decode())
        except ValueError:
            return ""
        else:
            if dJson and ("error" in dJson):
                return dJson["error"]
    return ""

# Grab status inside received JSON
def getStatus(Data):
    if Data and "Status" in Data:
        try:
            return int(Data["Status"])
        except ValueError:
            return 504
    else:
        return 504

def DumpConfigToLog():
    for x in Parameters:
        if Parameters[x] != "":
            self.myDebug( "'" + x + "':'" + str(Parameters[x]) + "'")
    self.myDebug("Device count: " + str(len(Devices)))
    for x in Devices:
        self.myDebug("Device:           " + str(x) + " - " + str(Devices[x]))
        self.myDebug("Device ID:       '" + str(Devices[x].ID) + "'")
        self.myDebug("Device Name:     '" + Devices[x].Name + "'")
        self.myDebug("Device iValue:    " + str(Devices[x].iValue))
        self.myDebug("Device sValue:   '" + Devices[x].sValue + "'")
        self.myDebug("Device LastLevel: " + str(Devices[x].LastLevel))
    return

# Convert Enedis date string to datetime object
def enedisDateToDatetime(datetimeStr):
    #Buggy
    #return datetime.strptime(datetimeStr, "%d/%m/%Y")
    #Not buggy ?
    return datetime(*(strptime(datetimeStr, "%Y-%m-%d")[0:6]))

# Convert datetime object to Enedis date string
def datetimeToEnedisDateString(datetimeObj):
    return datetimeObj.strftime("%Y-%m-%d")

# Convert datetime object to Domoticz date string
def datetimeToSQLDateString(datetimeObj):
    return datetimeObj.strftime("%Y-%m-%d")

# Convert datetime object to Domoticz date and time string
def datetimeToSQLDateTimeString(datetimeObj):
    return datetimeObj.strftime("%Y-%m-%d %H:%M:%S")
