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
<plugin key="linky" name="Linky" author="Barberousse" version="2.0.0-beta-1" externallink="https://github.com/guillaumezin/DomoticzLinky">
    <params>
        <param field="Mode4" label="Heures creuses (exemple : 2h00-7h00 13h00-16h00, laisser vide si pas d'heure creuse)" width="500px" required="false" default="">
<!--        <param field="Mode4" label="Heures creuses" width="500px">
            <options>
                <option label="Désactivées" value=""  default="true" />
                <option label="21h30-5h30" value="21h30-5h30" />
                <option label="22h00-6h00" value="22h00-6h00" />
                <option label="22h30-6h30" value="22h30-6h30" />
                <option label="23h00-7h00" value="23h00-7h00" />
                <option label="23h30-7h00" value="23h30-7h00" />
                <option label="23h30-7h30" value="23h30-7h30" />
                <option label="0h00-8h00" value="0h00-8h00" />
                <option label="1h00-7h00 et 12h30-14h30" value="1h00-7h00 et 12h30-14h30" />
                <option label="1h00-7h30 et 12h30-14h00" value="1h00-7h30 et 12h30-14h00" />
                <option label="1h00-7h30 et 12h00-14h30" value="1h00-7h30 et 13h00-14h30" />
                <option label="1h30-7h30 et 12h00-14h00" value="1h30-7h30 et 12h00-14h00" />
                <option label="1h30-7h30 et 12h30-14h30" value="1h30-7h30 et 12h30-14h30" />
                <option label="2h00-7h00 et 12h30-15h30" value="2h00-7h00 et 12h30-15h30" />
                <option label="2h00-7h00 et 13h00-16h00" value="2h00-7h00 et 13h00-16h00" />
                <option label="2h00-7h00 et 14h00-17h00" value="2h00-7h00 et 14h00-17h00" />
                <option label="2h00-8h00 et 13h30-15h30" value="2h00-8h00 et 13h30-15h30" />
                <option label="3h00-8h00 et 13h30-16h30" value="3h00-8h00 et 13h30-16h30" />
                <option label="3h00-7h00 et 12h30-14h30 et 20h30-22h30" value="3h00-7h00 et 12h30-14h30 et 20h30-22h30" />
                <option label="3h30-7h00 et 13h00-16h00 et 22h30-6h30" value="3h30-7h00 et 13h00-16h00 et 22h30-6h30" />
            </options>
-->
        </param>
        <param field="Mode5" label="Consommation à montrer sur le tableau de bord (affichage principal)" width="500px">
            <options>
                <option label="Pic consommation journée dernière" value="peak_day" />
                <option label="Pic consommation semaine en cours" value="peak_cweek" />
                <option label="Pic consommation semaine dernière" value="peak_lweek" />
                <option label="Pic consommation mois en cours" value="peak_cmonth" />
                <option label="Pic consommation mois dernier" value="peak_lmonth" />
                <option label="Pic consommation année en cours" value="peak_year" />
            </options>
        </param>
        <param field="Mode6" label="Consommation à montrer sur le tableau de bord (affichage secondaire)" width="500px">
            <options>
                <option label="Consommation / production journée dernière" value="value_day"  default="true" />
                <option label="Consommation / production semaine en cours" value="value_cweek" />
                <option label="Consommation / production semaine dernière" value="value_lweek" />
                <option label="Consommation / production mois en cours" value="value_cmonth" />
                <option label="Consommation / production mois dernier" value="value_lmonth" />
                <option label="Consommation / production année en cours" value="value_year" />
                <option label="Consommation / production horaire max journée dernière" value="max_day" />
                <option label="Consommation / production horaire max semaine en cours" value="max_cweek" />
                <option label="Consommation / production horaire max semaine dernière" value="max_lweek" />
                <option label="Consommation / production horaire max mois en cours" value="max_cmonth" />
                <option label="Consommation / production horaire max mois dernier" value="max_lmonth" />
                <option label="Consommation / production horaire max année en cours" value="max_year" />
                <option label="Consommation / production horaire moyenne journée dernière" value="mean_day" />
                <option label="Consommation / production horaire moyenne semaine en cours" value="mean_cweek" />
                <option label="Consommation / production horaire moyenne semaine dernière" value="mean_lweek" />
                <option label="Consommation / production horaire moyenne mois en cours" value="mean_cmonth" />
                <option label="Consommation / production horaire moyenne mois dernier" value="mean_lmonth" />
                <option label="Consommation / production horaire moyenne année en cours" value="mean_year" />
            </options>
        </param>
        <param field="Mode1" label="Nombre de jours à récupérer pour la vue par heures (0 min, pour désactiver la récupération par heures, 7 max)" width="50px" required="false" default="7"/>
        <param field="Mode2" label="Nombre de jours à récupérer pour les autres vues (730 max)" width="50px" required="false" default="60"/>
        <param field="Mode3" label="Debug" width="170px">
            <options>
                <option label="Non" value="0"  default="true" />
                <option label="Simple" value="1"/>
                <option label="Avancé" value="2"/>
                <option label="Reset consentement" value="3"/>
                <option label="Faux client 0" value="10"/>
                <option label="Faux client 1" value="11"/>
                <option label="Faux client 2" value="12"/>
                <option label="Faux client 3" value="13"/>
                <option label="Faux client 4" value="14"/>
                <option label="Faux client 5" value="15"/>
                <option label="Faux client 6" value="16"/>
                <option label="Faux client 7" value="17"/>
                <option label="Faux client 8" value="18"/>
                <option label="Faux client 9" value="19"/>
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
# import re
from datetime import datetime
from datetime import timedelta
from time import strptime
# from random import randint
# import html
from pprint import pprint

CLIENT_ID = ["d198fd52-61c0-4b77-8725-06a1ef90da9f", "9c551777-9d1b-447c-9e68-bfe6896ee002"]

LOGIN_BASE_PORT = ["443", "443"]
LOGIN_BASE_URI = ["enedis.domoticz.russandol.pro", "opensrcdev.alwaysdata.net"]
API_ENDPOINT_DEVICE_CODE = ["/device/code", "/domoticzlinkyconnect/device/code"]
API_ENDPOINT_DEVICE_TOKEN = ["/device/token", "/domoticzlinkyconnect/device/token"]
API_ENDPOINT_PROXY = ["/device/proxy", "/domoticzlinkyconnect/device/proxy"]
VERIFY_CODE_URI = ["https://" + LOGIN_BASE_URI[0] + "/device?code=",
                   "https://" + LOGIN_BASE_URI[1] + "/domoticzlinkyconnect/device?code="]

API_BASE_PORT = ["443", "443"]
API_BASE_URI = ["gw.prd.api.enedis.fr", "gw.hml.api.enedis.fr"]
API_ENDPOINT_DATA_CONSUMPTION_LOAD_CURVE = '/v4/metering_data/consumption_load_curve'
API_ENDPOINT_DATA_CONSUMPTION_MAX_POWER = '/v4/metering_data/daily_consumption_max_power'
API_ENDPOINT_DATA_DAILY_CONSUMPTION = '/v4/metering_data/daily_consumption'
API_ENDPOINT_DATA_PRODUCTION_LOAD_CURVE = '/v4/metering_data/production_load_curve'
API_ENDPOINT_DATA_DAILY_PRODUCTION = '/v4/metering_data/daily_production'

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
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
    # string: name of the Linky device
    sDeviceName = "Linky"
    # string: description of the Linky device
    sDescription = "Compteur Linky"
    # list of integer: type (pTypeP1Power or pTypeGeneral)
    lType = [0xfa, 0xf3]
    # list of integer: subtype (sTypeP1Power or sTypeManagedCounter)
    lSubType = [0x01, 0x21]
    # list of integer: switch type (Energy)
    lSwitchType = [0, 0]
    # list of dict: options
    lOptions = [{"DisableLogAutoUpdate": "true", "AddDBLogEntry": "true"}, {}]
    # string: step name of the state machine
    sConnectionStep = None
    # string: memory of step name of the state machine during connection
    sMemConnectionStep = None
    # string: step name of the next state machine during connection
    sConnectionNextStep = None
    # boolean: true if a step failed
    # bHasAFail = None
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
    iDaysLeftHoursView = None
    # datetime: backup end date
    savedDateEndDays = None
    savedDateEndDaysForHoursView = None
    # datetime: backup 2 end date
    savedDateEndDays2 = None
    # datetime: date for hours history view beginning
    dateBeginDaysHistoryView = None
    # boolean: is this the batch of the most recent history
    bFirstMonths = None
    # list: usage point id
    lUsagePointIndex = None
    # integer: usage point id index in list
    iUsagePointIndex = None
    # string: consumption to show = current week ("cweek"), the previous week ("lweek", the current month ("cmonth"), the previous month ("lmonth"), or year ("cyear"), prefix "max_" for max calculation
    sConsumptionType1 = None
    sConsumptionType2 = None
    # Tarif
    sTarif = None
    # integer: number of other view (peak)
    iHistoryDaysForPeakDaysView = None
    # boolean: debug mode
    iDebugLevel = None
    # previous day
    prevDay = None
    # current day
    curDay = None
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
    # count data packet Error
    iDataErrorCount = None
    # production mode
    bProdMode = None
    # send nuffer
    sBuffer = None
    # data sent
    sMemData = None
    # connect for login if true, for data if false
    bLoginConnect = True
    # timeout counter
    iTimeoutCount = 0
    # resend counter
    iResendCount = 0
    # data dict with date string as index and consumption1, consumption2, production1, production2 as float and date as DateTime
    dData = None
    # dict with time (xxhmm format) as index and a boolean to indicate tariff
    dHc = None
    # has 2 tariff
    bHasHc = None
    # dict with calculation to show on dashboard
    dCalculate = None
    # date
    dateNextConnection = None
    # integer: which device to use
    iAlternateDevice = 0
    # integer: false customoer
    iFalseCustomer = 0
    # integer: which address to use (production or sandbox)
    iAlternateAddress = 0
    # to know that we come from refresh token step
    bRefreshToken = None

    def __init__(self):
        self.isStarted = False
        self.httpLoginConn = None
        self.httpDataConn = None
        self.sConnectionStep = "idle"
        self.bHasAFail = False
        self.sBuffer = None
        self.iTimeoutCount = 0
        self.iResendCount = 0

    def myDebug(self, message):
        if self.iDebugLevel:
            Domoticz.Log(message)

    # resend same data
    def reconnectAndResend(self):
        self.sBuffer = self.sMemData
        self.sConnectionNextStep = self.sMemConnectionStep
        self.sConnectionStep = "connecting"
        self.iTimeoutCount = 0
        self.iResendCount = self.iResendCount + 1
        if self.bLoginConnect:
            self.httpLoginConn = Domoticz.Connection(Name="HTTPS connection", Transport="TCP/IP", Protocol="HTTPS",
                                                     Address=LOGIN_BASE_URI[self.iAlternateAddress],
                                                     Port=LOGIN_BASE_PORT[self.iAlternateAddress])
            self.httpLoginConn.Connect()
        else:
            self.httpDataConn = Domoticz.Connection(Name="HTTPS connection", Transport="TCP/IP", Protocol="HTTPS",
                                                    Address=API_BASE_URI[self.iAlternateAddress],
                                                    Port=API_BASE_PORT[self.iAlternateAddress])
            self.httpDataConn.Connect()

    # Prepare buffer and connect
    def connectAndSend(self, conn, data, address, port):
        self.sMemData = data
        self.sBuffer = data
        self.sConnectionNextStep = self.sConnectionStep
        self.sMemConnectionStep = self.sConnectionStep
        self.sConnectionStep = "connecting"
        self.iTimeoutCount = 0
        self.iResendCount = 0
        conn = Domoticz.Connection(Name="HTTPS connection", Transport="TCP/IP", Protocol="HTTPS", Address=address,
                                   Port=port)
        conn.Connect()
        return conn

    # Connect for login
    def connectAndSendForAuthorize(self, data):
        self.bLoginConnect = True
        self.httpLoginConn = self.connectAndSend(self.httpLoginConn, data, LOGIN_BASE_URI[self.iAlternateAddress],
                                                 LOGIN_BASE_PORT[self.iAlternateAddress])

    # Connect for metering data
    def connectAndSendForMetering(self, data):
        self.bLoginConnect = False
        self.httpDataConn = self.connectAndSend(self.httpDataConn, data, API_BASE_URI[self.iAlternateAddress],
                                                API_BASE_PORT[self.iAlternateAddress])

    # get default headers
    def initHeaders(self, uri):
        headers = dict(HEADERS)
        headers["Host"] = uri;
        return headers

    # get access token
    def getDeviceCode(self):
        headers = self.initHeaders(
            LOGIN_BASE_URI[self.iAlternateAddress] + ":" + LOGIN_BASE_PORT[self.iAlternateAddress])
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        postData = {
            "client_id": CLIENT_ID[self.iAlternateAddress]
        }

        sendData = {
            "Verb": "POST",
            "URL": API_ENDPOINT_DEVICE_CODE[self.iAlternateAddress],
            "Headers": headers,
            "Data": dictToQuotedString(postData)
        }

        self.dumpDictToLog(sendData)
        self.connectAndSendForAuthorize(sendData)

    def showStatusError(self, hours, Data):
        sErrorSentence = "Erreur status : " + str(getStatus(Data))
        if Data and ("Data" in Data):
            try:
                dJson = json.loads(Data["Data"].decode())
            except ValueError:
                pass
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
        sError, sErrorDescription, sErrorUri = getError(Data)
        if sError:
            sErrorSentence = sErrorSentence + " - code " + sError
        if sErrorDescription:
            sErrorSentence = sErrorSentence + " - description : " + sErrorDescription
        if sErrorUri:
            sErrorSentence = sErrorSentence + " - URI : " + sErrorUri
        self.showSimpleStepError(sErrorSentence)

    def parseDeviceCode(self, Data):
        self.dumpDictToLog(Data)
        iStatus = getStatus(Data)
        if iStatus == 429:
            return "retry"
        if iStatus == 200:
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
                    sUrl = VERIFY_CODE_URI[self.iAlternateAddress] + quote(sUserCode)
                    if self.iFalseCustomer:
                        sUrl = sUrl + "&state=" + str(self.iFalseCustomer)
                    Domoticz.Error(
                        "Connectez-vous à l'adresse " + sUrl + " pour lancer la demande de consentement avec le code " + sUserCode)
                    return "done"
            else:
                self.showSimpleStepError("Pas de données reçue")
        else:
            self.showSimpleStatusError(Data)
        return "error"

    # get access token
    def getAccessToken(self):
        headers = self.initHeaders(
            LOGIN_BASE_URI[self.iAlternateAddress] + ":" + LOGIN_BASE_PORT[self.iAlternateAddress])
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        postData = {
            "client_id": CLIENT_ID[self.iAlternateAddress],
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "device_code": self.sDeviceCode
        }

        sendData = {
            "Verb": "POST",
            "URL": API_ENDPOINT_DEVICE_TOKEN[self.iAlternateAddress],
            "Headers": headers,
            "Data": dictToQuotedString(postData)
        }

        self.dumpDictToLog(sendData)
        self.connectAndSendForAuthorize(sendData)

    # Refresh token
    def refreshToken(self):
        headers = self.initHeaders(
            LOGIN_BASE_URI[self.iAlternateAddress] + ":" + LOGIN_BASE_PORT[self.iAlternateAddress])
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        postData = {
            "grant_type": "refresh_token",
            "client_id": CLIENT_ID[self.iAlternateAddress],
            "refresh_token": getConfigItem("refresh_token", "")
        }

        sendData = {
            "Verb": "POST",
            "URL": API_ENDPOINT_PROXY[self.iAlternateAddress],
            "Headers": headers,
            "Data": dictToQuotedString(postData)
        }

        self.bRefreshToken = True
        self.dumpDictToLog(sendData)
        self.connectAndSendForAuthorize(sendData)

    # Parse access token
    def parseAccessToken(self, Data):
        self.dumpDictToLog(Data)
        iStatus = getStatus(Data)
        sError, sErrorDescription, sErrorUri = getError(Data)
        if iStatus == 429:
            return "retry"
        elif sError == "authorization_pending":
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
        elif (sError != "invalid_grant") and (iStatus == 200):
            if Data and ("Data" in Data):
                try:
                    dJson = json.loads(Data["Data"].decode())
                except ValueError as err:
                    self.showSimpleStepError("Les données reçues ne sont pas du JSON : " + str(err))
                    return False
                if dJson and ("usage_points_id" in dJson):
                    setConfigItem("usage_points_id", str(dJson["usage_points_id"]).split(","))
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
        headers = self.initHeaders(API_BASE_URI[self.iAlternateAddress] + ":" + API_BASE_PORT[self.iAlternateAddress])
        headers["Authorization"] = getConfigItem("token_type", "") + " " + getConfigItem("access_token", "")

        query = {
            "start": datetimeToEnedisDateString(start),
            "end": datetimeToEnedisDateString(end),
            "usage_point_id": self.sUsagePointId
        }

        sendData = {
            "Verb": "GET",
            "URL": uri + "?" + dictToQuotedString(query),
            "Headers": headers
        }

        self.dumpDictToLog(sendData)
        self.connectAndSendForMetering(sendData)

    # get and create if needed Domoticz device
    def getOrCreateDevice(self, sUsagePointCurrentId):
        for iIndexUnit, oDevice in Devices.items():
            if sUsagePointCurrentId == oDevice.DeviceID:
                return oDevice

        for iIndexUnit in range(1, 256):
            if iIndexUnit == 256:
                self.showSimpleStepError(
                    "Ne peut ajouter de dispositif Linky à la base de données. Trop de dispositifs déjà présents, faites le ménage SVP")
                return None
            if iIndexUnit not in Devices:
                Domoticz.Device(Name=self.sDeviceName + " " + sUsagePointCurrentId, DeviceID=sUsagePointCurrentId,
                                Unit=iIndexUnit, Type=self.lType[self.iAlternateDevice],
                                Subtype=self.lSubType[self.iAlternateDevice],
                                Switchtype=self.lSwitchType[self.iAlternateDevice],
                                Description=self.sDescription + " " + sUsagePointCurrentId,
                                Options=self.lOptions[self.iAlternateDevice], Used=1).Create()
                if iIndexUnit not in Devices:
                    self.showSimpleStepError(
                        "Ne peut ajouter de dispositif Linky à la base de données. Vérifiez dans les paramètres de Domoticz que l'ajout de nouveaux dispositifs est autorisé")
                    return None
                else:
                    return Devices[iIndexUnit]

    # insert usage in Domoticz DB
    def addToDevice(self, oDevice, fConsumption1, fConsumption2, fProduction1, fProduction2, sDate):
        if self.iAlternateDevice:
            sValue = "-1.0;" + str(fConsumption1 + fConsumption2) + ";" + sDate
        else:
            sValue = str(fConsumption1) + ";" + str(fConsumption2) + ";" + str(fProduction1) + ";" + str(
                fProduction2) + ";0;0;" + sDate
        self.myDebug("Mets dans la BDD la valeur " + sValue)
        oDevice.Update(nValue=0, sValue=sValue,
            Type=self.lType[self.iAlternateDevice],
            Subtype=self.lSubType[self.iAlternateDevice],
            Switchtype=self.lSwitchType[self.iAlternateDevice],
            Options=self.lOptions[self.iAlternateDevice])
        return True

    # Update value shown on Domoticz dashboard
    def updateDevice(self, oDevice, fConsoVal1, fConsoVal2, fProdVal1, fProdVal2, fSecVal1, fSecVal2):
        if self.iAlternateDevice:
            sValue = "-1.0;" + str(fSecVal1 + fSecVal2)
        else:
            sValue = str(fConsoVal1) + ";" + str(fConsoVal2) + ";" + str(fProdVal1) + ";" + str(fProdVal2) + ";" + str(
                fSecVal1) + ";" + str(fSecVal2)
        self.myDebug("Mets sur le tableau de bord la valeur " + sValue)
        oDevice.Update(nValue=0, sValue=sValue,
            Type=self.lType[self.iAlternateDevice],
            Subtype=self.lSubType[self.iAlternateDevice],
            Switchtype=self.lSwitchType[self.iAlternateDevice],
            Options=self.lOptions[self.iAlternateDevice])
        return True

    # Show error in state machine context
    def showSimpleStepError(self, logMessage):
        Domoticz.Error("durant l'étape : " + self.sConnectionStep + " - " + logMessage)

    # Show error in state machine context with dates
    def showStepError(self, hours, logMessage):
        if hours:
            Domoticz.Error("durant l'étape " + self.sConnectionStep + " de " + datetimeToEnedisDateString(
                self.dateBeginHours) + " à " + datetimeToEnedisDateString(self.dateEndHours) + " - " + logMessage)
        else:
            Domoticz.Error("durant l'étape " + self.sConnectionStep + " de " + datetimeToEnedisDateString(
                self.dateBeginDays) + " à " + datetimeToEnedisDateString(self.dateEndDays) + " - " + logMessage)

    # Check date if in cost 1 or cost 2
    def isCost2(self, dDate):
        sTimeIndex = "{:01d}h{:02d}".format(dDate.hour, dDate.minute)
        return self.dHc[sTimeIndex]

    # Write data from memory to Domoticz DB
    def saveDataToDb(self, sUsagePointCurrentId):
        if sUsagePointCurrentId not in self.dData:
            return False

        oDevice = self.getOrCreateDevice(sUsagePointCurrentId)
        if not oDevice:
            return False

        dUsagePointData = self.dData[sUsagePointCurrentId]
        iConsumption1 = 0
        iConsumption2 = 0
        iProduction1 = 0
        iProduction2 = 0

        self.resetCalculate(sUsagePointCurrentId)

        # sorting needed to accumulate
        for sDate, dOneData in sorted(dUsagePointData.items()):
            # hour
            if len(sDate) > 10:
                # We don't want the last day = today, it breaks CounterToday value and log view
                self.dayAccumulate(sUsagePointCurrentId, dOneData["date"], dOneData)
                if dOneData["date"] >= self.savedDateEndDays2:
                    # Domoticz.Error("Skip " + sDate)
                    continue
                # We want only iHistoryDaysForHoursView days
                if (self.iHistoryDaysForHoursView < 1) or (dOneData["date"] < self.dateBeginDaysHistoryView):
                    # Domoticz.Error("Skip " + sDate)
                    continue
                iConsumption1 = iConsumption1 + dOneData["consumption1"]
                iConsumption2 = iConsumption2 + dOneData["consumption2"]
                iProduction1 = iProduction1 + dOneData["production1"]
                iProduction2 = iProduction2 + dOneData["production2"]
                if self.iAlternateDevice:
                    if not self.addToDevice(oDevice, dOneData["consumption1"], dOneData["consumption2"],
                                            dOneData["production1"], dOneData["production2"], sDate):
                        return False
                else:
                    if not self.addToDevice(oDevice, iConsumption1, iConsumption2, iProduction1, iProduction2, sDate):
                        return False
            # day
            else:
                # We don't want the last day = today, it's incomplete
                if dOneData["date"] >= self.savedDateEndDays2:
                    # Domoticz.Error("Skip " + sDate)
                    continue
                if not self.addToDevice(oDevice, dOneData["consumption1"], dOneData["consumption2"], dOneData["production1"],
                                        dOneData["production2"], sDate):
                    return False
        # self.dumpDictToLog(self.dCalculate)
        return self.updateDashboard(oDevice, sUsagePointCurrentId)

    # Merge counters with only consumption with counters with only production into new virtual counters
    def mergeCounters(self):
        bResult = True
        dCalculateCopy = self.dCalculate.copy()
        for sUsagePointConsumptionId in dCalculateCopy:
            if (not dCalculateCopy[sUsagePointConsumptionId]["production1"]["value_year"]) and (not dCalculateCopy[sUsagePointConsumptionId]["production2"]["value_year"]):
                for sUsagePointProductionId in dCalculateCopy:
                    if (not dCalculateCopy[sUsagePointProductionId]["consumption1"]["value_year"]) and (not dCalculateCopy[sUsagePointProductionId]["consumption2"]["value_year"]):
                        # Do merge
                        sNewUsagePointId = sUsagePointConsumptionId + " / " + sUsagePointProductionId

                        # copy consumption data to merged device
                        self.dData[sNewUsagePointId] = self.dData[sUsagePointConsumptionId].copy()

                        # copy production data to merged device where dates coincide for consumption
                        for sDate, dMergedData in self.dData[sNewUsagePointId].items():
                            if sDate in self.dData[sUsagePointProductionId]:
                                dProdData = self.dData[sUsagePointProductionId][sDate]
                                dMergedData["production1"] = dProdData["production1"]
                                dMergedData["production2"] = dProdData["production2"]
                                dMergedData["productionpeak"] = dProdData["productionpeak"]

                        # create production data to merged device where dates don't coincide for consumption
                        for sDate, dProdData in self.dData[sUsagePointConsumptionId].items():
                            if sDate not in self.dData[sNewUsagePointId]:
                                dMergedData = initData(dProdData["date"])
                                dMergedData["production1"] = dProdData["production1"]
                                dMergedData["production2"] = dProdData["production2"]
                                dMergedData["productionpeak"] = dProdData["productionpeak"]
                                self.dData[sNewUsagePointId][sDate] = dMergedData

                        if not self.saveDataToDb(sNewUsagePointId):
                            bResult = False
        return bResult

    # Store data in memory
    def storeData(self, fData, sDate, dDate, bProduction, bCost2, bPeak):
        if self.sUsagePointId not in self.dData:
            self.dData[self.sUsagePointId] = dict()
        if sDate not in self.dData[self.sUsagePointId]:
            self.dData[self.sUsagePointId][sDate] = initData(dDate)
        if bPeak:
            if bProduction:
                self.dData[self.sUsagePointId][sDate]["productionpeak"] = fData
            else:
                self.dData[self.sUsagePointId][sDate]["consumptionpeak"] = fData
        else:
            if bProduction:
                if bCost2:
                    self.dData[self.sUsagePointId][sDate]["production2"] = self.dData[self.sUsagePointId][sDate][
                                                                               "production2"] + fData
                else:
                    self.dData[self.sUsagePointId][sDate]["production1"] = self.dData[self.sUsagePointId][sDate][
                                                                               "production1"] + fData
            else:
                if bCost2:
                    self.dData[self.sUsagePointId][sDate]["consumption2"] = self.dData[self.sUsagePointId][sDate][
                                                                                "consumption2"] + fData
                else:
                    self.dData[self.sUsagePointId][sDate]["consumption1"] = self.dData[self.sUsagePointId][sDate][
                                                                                "consumption1"] + fData

    # Manage data in memory for hours
    def manageDataHours(self, fData, dDate, bProduction=False):
        sDateTime = datetimeToSQLDateTimeString(dDate)
        bCost2 = self.isCost2(dDate)
        # Store hour
        self.storeData(fData, sDateTime, dDate, bProduction, bCost2, False)
        # Accumulate for day
        dDate = dDate - timedelta(hours=1)
        sDate = datetimeToSQLDateString(dDate)
        self.storeData(fData, sDate, dDate, bProduction, bCost2, False)

    # Manage data in memory for days
    def manageDataDays(self, fData, dDate, bPeak=False, bProduction=False):
        sDate = datetimeToSQLDateTimeString(dDate)
        self.storeData(fData, sDate, dDate, bProduction, False, bPeak)

    # Grab hours data inside received JSON data for short log
    def exploreDataHours(self, Data, bProduction=False):
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
                if dJson and ("meter_reading" in dJson):
                    try:
                        beginDate = enedisDateToDatetime(dJson["meter_reading"]["start"])
                        endDate = enedisDateToDatetime(dJson["meter_reading"]["end"])
                    except (TypeError, ValueError) as err:
                        self.showStepError(True, "Erreur dans le format de donnée de date JSON : " + str(err))
                        return False
                    except:
                        self.showStepError(True, "Erreur dans la donnée de date JSON : " + str(sys.exc_info()[0]) +
                                           dJson["graphe"]["periode"]["dateDebut"] + dJson["graphe"]["periode"][
                                               "dateFin"])
                        return False
                    # We accumulate data because Enedis sends kWh for every 30 minutes and Domoticz expects data only for every hour
                    accumulation = 0.0
                    currentDay = -1
                    steps = 1.0
                    dataSeenToTheEnd = False
                    for index, data in enumerate(dJson["meter_reading"]["interval_reading"]):
                        try:
                            val = float(data["value"])
                        except:
                            val = -1.0
                        if (val >= 0.0):
                            # Shift to +1 hour for Domoticz, because bars/hours for graph are shifted to -1 hour in Domoticz, cf. constructTime() call in WebServer.cpp
                            # Enedis and Domoticz doesn't set the same date for used energy, add offset
                            curDate = enedisDateTimeToDatetime(data["date"]) + timedelta(hours=1)
                            # Domoticz.Log("date " + datetimeToSQLDateTimeString(curDate) + " " + datetimeToSQLDateTimeString(endDate))
                            accumulation = accumulation + val
                            # Domoticz.Log("Value " + str(val) + " " + datetimeToSQLDateTimeString(curDate))
                            if curDate.minute == 0:
                                # Check that we had enough data, as expected
                                if curDate >= endDate:
                                    # Domoticz.Log("Last val")
                                    dataSeenToTheEnd = True
                                # Domoticz.Log("accumulation " + str(accumulation / steps) + " " + datetimeToSQLDateTimeString(curDate))
                                # if not self.createAndAddToDevice(accumulation / steps, datetimeToSQLDateTimeString(curDate)):
                                # return False
                                self.manageDataHours(accumulation / steps, curDate, bProduction)
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

    def resetCalculate(self, sUsagePointCurrentId):
        self.dCalculate[sUsagePointCurrentId] = {"consumption1": dict(), "consumption2": dict(), "production1": dict(),
                                                 "production2": dict(), "consumptionpeak": dict(),
                                                 "productionpeak": dict()}

    # Reset counters for power consumption
    def resetDayAccumulate(self):
        self.curDay = self.savedDateEndDays2.replace(hour=0, minute=0, second=0, microsecond=0)
        self.prevDay = self.curDay - timedelta(days=1)
        self.daysCalculate = 0.0
        self.fdmonth = self.prevDay.replace(day=1)
        ldpmonth = self.fdmonth - timedelta(days=1)
        self.fdpmonth = ldpmonth.replace(day=1)
        self.fdweek = self.prevDay - timedelta(days=self.prevDay.weekday())
        ldpweek = self.fdweek - timedelta(days=1)
        self.fdpweek = ldpweek - timedelta(days=6)
        self.fdyear = self.prevDay.replace(day=1, month=1)
        #Domoticz.Log(
        #    str(self.prevDay) + " " + str(self.curDay) + " " + str(self.fdmonth) + " " + str(self.fdpmonth) + " " + str(
        #       self.fdweek) + " " + str(self.fdpweek) + " " + str(self.fdyear))

    # Calculate and store
    def modifyCalculation(self, dCalculation, sParameter, fVal):
        sParameterComplete = "value_" + sParameter
        fCurrentVal = 0
        if sParameterComplete not in dCalculation:
            dCalculation[sParameterComplete] = 0
        fCurrentVal = dCalculation[sParameterComplete] + fVal
        dCalculation[sParameterComplete] = fCurrentVal

        sParameterComplete = "max_" + sParameter
        if sParameterComplete not in dCalculation:
            dCalculation[sParameterComplete] = 0
        if fVal > dCalculation[sParameterComplete]:
            dCalculation[sParameterComplete] = fVal

        sParameterComplete = "counter_" + sParameter
        if sParameterComplete not in dCalculation:
            dCalculation[sParameterComplete] = 0
        iCounter = dCalculation[sParameterComplete] + 1
        dCalculation[sParameterComplete] = iCounter

        sParameterComplete = "mean_" + sParameter
        dCalculation[sParameterComplete] = fCurrentVal / iCounter

    # Accumulate power consumption
    def dayAccumulate(self, sUsagePointCurrentId, dateCur, dVal):
        for sKey, dCalcType in self.dCalculate[sUsagePointCurrentId].items():
            if (dateCur >= self.fdweek):
                self.modifyCalculation(dCalcType, "cweek", dVal[sKey])
            if (self.fdpweek <= dateCur < self.fdweek):
                self.modifyCalculation(dCalcType, "lweek", dVal[sKey])
            if (dateCur >= self.fdmonth):
                self.modifyCalculation(dCalcType, "cmonth", dVal[sKey])
            if (self.fdpmonth <= dateCur < self.fdmonth):
                self.modifyCalculation(dCalcType, "lmonth", dVal[sKey])
            if (dateCur >= self.fdyear):
                self.modifyCalculation(dCalcType, "year", dVal[sKey])
            if (self.prevDay <= dateCur < self.curDay):
                self.modifyCalculation(dCalcType, "day", dVal[sKey])

    # Grab days data inside received JSON data for history
    def exploreDataDays(self, Data, bPeak, bProduction=False):
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
                if dJson and ("meter_reading" in dJson):
                    try:
                        beginDate = enedisDateToDatetime(dJson["meter_reading"]["start"])
                        endDate = enedisDateToDatetime(dJson["meter_reading"]["end"])
                    except ValueError as err:
                        self.showStepError(False, "Erreur dans le format de donnée de date JSON : " + str(err))
                        return False
                    except:
                        self.showStepError(False, "Erreur dans la donnée de date JSON : " + str(sys.exc_info()[0]))
                        return False
                    for index, data in enumerate(dJson["meter_reading"]["interval_reading"]):
                        try:
                            val = float(data["value"])
                        except:
                            val = -1.0
                        if (val >= 0.0):
                            curDate = enedisDateToDatetime(data["date"])
                            # Domoticz.Log("Value " + str(val) + " " + datetimeToSQLDateString(curDate))
                            # self.dumpDictToLog(values)
                            # self.dayAccumulate(curDate, val)
                            # if not self.createAndAddToDevice(val, datetimeToSQLDateString(curDate)):
                            # return False
                            self.manageDataDays(val, curDate, bPeak, bProduction)
                    return True
                else:
                    self.showStepError(False, "Erreur à la réception de données JSON")
        else:
            self.showStepError(False, "Aucune donnée reçue")
        return False

    # Update dashboard with accumulated value
    def updateDashboard(self, oDevice, sUsagePointCurrentId):
        if not sUsagePointCurrentId in self.dCalculate:
            return False
        self.dumpDictToLog(self.dCalculate[sUsagePointCurrentId])
        fConsoVal1 = 0
        fConsoVal2 = 0
        fProdVal1 = 0
        fProdVal2 = 0
        fSecVal1 = 0
        fSecVal2 = 0

        if self.sConsumptionType1.startswith("peak_"):
            SCalcT1 = self.sConsumptionType1.replace("peak_", "max_")
            sConso1T1 = "consumptionpeak"
            sProd1T1 = "productionpeak"
            bTwoValuesT1 = False
        else:
            SCalcT1 = self.sConsumptionType1
            sConso1T1 = "consumption1"
            sConso2T1 = "consumption2"
            sProd1T1 = "production1"
            sProd2T1 = "production2"
            bTwoValuesT1 = self.bHasHc

        if self.sConsumptionType2.startswith("peak_"):
            SCalcT2 = self.sConsumptionType2.replace("peak_", "max_")
            sConso1T2 = "consumptionpeak"
            sProd1T2 = "productionpeak"
            bTwoValuesT2 = False
        else:
            SCalcT2 = self.sConsumptionType2
            sConso1T2 = "consumption1"
            sConso2T2 = "consumption2"
            sProd1T2 = "production1"
            sProd2T2 = "production2"
            bTwoValuesT2 = self.bHasHc

        #self.myDebug(sConso1T1 + " --- " + " - " + sConso1T2 + " --- " + " - " + str(bTwoValuesT1) + " - " + str(bTwoValuesT2) + " / " + SCalcT1 + " /-/ " + SCalcT2)
        if bTwoValuesT1:
            if SCalcT1 in self.dCalculate[sUsagePointCurrentId][sConso1T1]:
                fConsoVal1 = self.dCalculate[sUsagePointCurrentId][sConso1T1][SCalcT1]
            if SCalcT1 in self.dCalculate[sUsagePointCurrentId][sConso2T1]:
                fConsoVal2 = self.dCalculate[sUsagePointCurrentId][sConso2T1][SCalcT1]
            if SCalcT1 in self.dCalculate[sUsagePointCurrentId][sProd1T1]:
                fProdVal1 = self.dCalculate[sUsagePointCurrentId][sProd1T1][SCalcT1]
            if SCalcT1 in self.dCalculate[sUsagePointCurrentId][sProd2T1]:
                fProdVal2 = self.dCalculate[sUsagePointCurrentId][sProd2T1][SCalcT1]
        else:
            if SCalcT1 in self.dCalculate[sUsagePointCurrentId][sConso1T1]:
                fConsoVal1 = self.dCalculate[sUsagePointCurrentId][sConso1T1][SCalcT1]
            if SCalcT1 in self.dCalculate[sUsagePointCurrentId][sProd1T1]:
                fProdVal1 = self.dCalculate[sUsagePointCurrentId][sProd1T1][SCalcT1]

        # for peaks, get the max
        if bTwoValuesT2:
            if SCalcT2 in self.dCalculate[sUsagePointCurrentId][sConso1T2]:
                if fSecVal1 < self.dCalculate[sUsagePointCurrentId][sConso1T2][SCalcT2]:
                    fSecVal1 = self.dCalculate[sUsagePointCurrentId][sConso1T2][SCalcT2]
            if SCalcT2 in self.dCalculate[sUsagePointCurrentId][sConso2T2]:
                if fSecVal1 < self.dCalculate[sUsagePointCurrentId][sConso2T2][SCalcT2]:
                    fSecVal1 = self.dCalculate[sUsagePointCurrentId][sConso2T2][SCalcT2]
            if SCalcT2 in self.dCalculate[sUsagePointCurrentId][sProd1T2]:
                if fSecVal2 < self.dCalculate[sUsagePointCurrentId][sProd1T2][SCalcT2]:
                    fSecVal2 = self.dCalculate[sUsagePointCurrentId][sProd1T2][SCalcT2]
            if SCalcT2 in self.dCalculate[sUsagePointCurrentId][sProd2T2]:
                if fSecVal2 < self.dCalculate[sUsagePointCurrentId][sProd2T2][SCalcT2]:
                    fSecVal2 = self.dCalculate[sUsagePointCurrentId][sProd2T2][SCalcT2]
        else:
            if SCalcT2 in self.dCalculate[sUsagePointCurrentId][sConso1T2]:
                fSecVal1 = self.dCalculate[sUsagePointCurrentId][sConso1T2][SCalcT2]
            if SCalcT2 in self.dCalculate[sUsagePointCurrentId][sProd1T2]:
                fSecVal2 = self.dCalculate[sUsagePointCurrentId][sProd1T2][SCalcT2]

        return self.updateDevice(oDevice, fConsoVal1, fConsoVal2, fProdVal1, fProdVal2, fSecVal1, fSecVal2)

    # Calculate days and date left for next batch
    def resetDates(self, dDateEnd=None):
        if dDateEnd:
            self.savedDateEndDays = dDateEnd
            self.savedDateEndDaysForHoursView = dDateEnd
            self.savedDateEndDays2 = dDateEnd
            self.dateBeginDaysHistoryView = dDateEnd - timedelta(days=self.iHistoryDaysForHoursView)
        else:
            self.savedDateEndDays = self.savedDateEndDays2
            self.savedDateEndDaysForHoursView = self.savedDateEndDays2

        self.iDaysLeft = self.iHistoryDaysForPeakDaysView
        if self.iHistoryDaysForDaysView < self.iHistoryDaysForHoursView:
            self.iDaysLeftHoursView = self.iHistoryDaysForHoursView
        else:
            self.iDaysLeftHoursView = self.iHistoryDaysForDaysView
        # self.dateBeginHours = self.savedDateEndDays - timedelta(days=self.iHistoryDaysForHoursView)
        # self.dateEndHours = self.savedDateEndDays

        self.calculateDaysLeft()

    # Calculate days and date left for next batch
    def calculateDaysLeft(self):
        # No more than 365 days at once
        self.iDaysLeft = self.iDaysLeft - 365
        if self.iDaysLeft <= 0:
            daysToGet = self.iDaysLeft + 365
        else:
            daysToGet = 365
        self.dateBeginDays = self.savedDateEndDays - timedelta(days=daysToGet)
        self.dateEndDays = self.savedDateEndDays
        self.savedDateEndDays = self.dateBeginDays

        # Domoticz.Log("Dates : " + datetimeToSQLDateTimeString(self.dateBeginDays) + " " + datetimeToSQLDateTimeString(self.dateEndDays) + " " + datetimeToSQLDateTimeString(self.savedDateEndDays))

        # No more than 7 days at once
        self.iDaysLeftHoursView = self.iDaysLeftHoursView - 7
        if self.iDaysLeftHoursView <= 0:
            daysToGet = self.iDaysLeftHoursView + 7
        else:
            daysToGet = 7
        self.dateBeginHours = self.savedDateEndDaysForHoursView - timedelta(days=daysToGet)
        self.dateEndHours = self.savedDateEndDaysForHoursView
        self.savedDateEndDaysForHoursView = self.dateBeginHours

        # Domoticz.Log("Dates : " + datetimeToSQLDateTimeString(self.dateBeginHours) + " " + datetimeToSQLDateTimeString(self.dateEndHours) + " " + datetimeToSQLDateTimeString(self.savedDateEndDaysForHoursView))

    # Still data to get
    def stillDays(self, bPeak):
        if bPeak:
            return self.iDaysLeft > 0
        else:
            return self.iDaysLeftHoursView > 0

    # Calculate next complete grab, for tomorrow between 5 and 6 am if tomorrow is true, for next hour otherwise
    def setNextConnection(self, tomorrow):
        self.iUsagePointIndex = 0
        if tomorrow:
            self.dateNextConnection = datetime.now() + timedelta(days=1)
            self.dateNextConnection = self.dateNextConnection.replace(hour=5)
        else:
            self.dateNextConnection = datetime.now() + timedelta(hours=1)
        # Randomize minutes to lower load on Enedis website
        # randint makes domoticz crash on RPI
        # self.dateNextConnection = self.dateNextConnection + timedelta(minutes=randint(0, 59), seconds=randint(0, 59))
        # We take microseconds to randomize
        minutesRand = round(datetime.now().microsecond / 10000) % 60
        self.dateNextConnection = self.dateNextConnection + timedelta(minutes=minutesRand)

    # Calculate next connection after a few seconds
    def setNextConnectionForLater(self, iInterval):
        self.dateNextConnection = datetime.now() + timedelta(seconds=iInterval)

    def clearData(self):
        self.dData = dict()
        self.dCalculate = dict()
        self.bHasAFail = False
        self.bRefreshToken = False

    # Handle the connection state machine
    def handleConnection(self, Data=None):
        self.myDebug("Etape " + self.sConnectionStep)

        # First and last step
        if self.sConnectionStep == "idle":
            Domoticz.Log("Récupération des données...")
            # Reset data
            self.clearData()

            # If we have access tokens, try do grab data, otherwise ask for tokens
            if getConfigItem("access_token", ""):
                # self.sConnectionStep = "getdatadays"
                # self.getData(self.lUsagePointIndex[self.iUsagePointIndex], API_ENDPOINT_DATA_DAILY_CONSUMPTION, self.dateBeginDays, self.dateEndDays)
                self.sConnectionStep = "start"
            else:
                self.sConnectionStep = "parsedevicecode"
                self.getDeviceCode()

        # We should never reach this
        elif self.sConnectionStep == "connecting":
            if (self.iTimeoutCount >= 3):
                self.showSimpleStepError("Timeout à la connexion")
                self.sConnectionStep = "done"
                self.bHasAFail = True
            else:
                self.iTimeoutCount = self.iTimeoutCount + 1

        # We should never reach this
        elif self.sConnectionStep == "nothingtosend":
            self.showSimpleStepError("Erreur à la connexion")
            self.sConnectionStep = "done"
            self.bHasAFail = True

        # Did we get a device code ?
        elif self.sConnectionStep == "parsedevicecode":
            result = self.parseDeviceCode(Data)
            if result == "done":
                self.sConnectionStep = "parseaccesstoken"
                self.getAccessToken()
            elif result == "retry":
                self.sConnectionStep = "retry"
                self.setNextConnectionForLater(self.iInterval)
            else:
                self.sConnectionStep = "done"
                self.bHasAFail = True

        # Wait for user to complete authorization process with his web browser
        elif self.sConnectionStep == "askagainaccesscode":
            # We must stay connected until completion, otherwise = error
            if not self.httpLoginConn.Connected():
                self.showSimpleStepError("Redemande du jeton d'accès")
                self.sConnectionStep = "done"
                self.bHasAFail = True
            else:
                self.sConnectionStep = "parseaccesstoken"
                self.getAccessToken()

        # Retry
        elif self.sConnectionStep == "retry":
            if (self.iResendCount >= 3):
                self.showSimpleStepError("Trop d'échec d'envoi, le plugin réessaiera plus tard")
                self.sConnectionStep = "done"
                self.bHasAFail = True
            else:
                self.reconnectAndResend()

        # Parse for access token
        elif self.sConnectionStep == "parseaccesstoken":
            result = self.parseAccessToken(Data)
            if result == "done":
                # Ask data for days
                # self.sConnectionStep = "getdatadays"
                # self.getData(self.lUsagePointIndex[self.iUsagePointIndex], API_ENDPOINT_DATA_DAILY_CONSUMPTION, self.dateBeginDays, self.dateEndDays)
                # Ask data for hours
                # If we have access tokens, try do grab data, otherwise ask for tokens
                self.sConnectionStep = "start"
            elif result == "retry":
                self.sConnectionStep = "retry"
                self.setNextConnectionForLater(self.iInterval)
            # Wait for user to complete authorization process with his web browser
            elif result == "pending":
                self.sConnectionStep = "askagainaccesscode"
                self.setNextConnectionForLater(self.iInterval)
            else:
                self.isEnabled = False
                resetTokens()
                self.showSimpleStepError(
                    "Le plugin va être arrêté. Relancez le en vous rendant dans Configuration/Matériel, en cliquant sur le plugin puis sur Modifier. Surveillez les logs pour obtenir le lien afin de renouveler le consentement pour la récupération des données auprès d'Enedis")

        # Ask data for hours
        elif self.sConnectionStep == "getdatahours":
            # Check if access token still valid
            iStatus = getStatus(Data)
            self.dumpDictToLog(Data)
            sError, sErrorDescription, sErrorUri = getError(Data)
            if (iStatus == 403) and (sError == "invalid_token") and (not self.bRefreshToken):
                self.sConnectionStep = "parseaccesstoken"
                self.refreshToken()
            elif iStatus == 403:
                self.isEnabled = False
                resetTokens()
                self.showSimpleStatusError(Data)
                self.showSimpleStepError(
                    "Le plugin va être arrêté. Relancez le en vous rendant dans Configuration/Matériel, en cliquant sur le plugin puis sur Modifier. Surveillez les logs pour obtenir le lien afin de renouveler le consentement pour la récupération des données auprès d'Enedis")
            elif (iStatus == 404) or self.bProdMode and (iStatus == 400):
                self.iDataErrorCount = self.iDataErrorCount + 1
                if self.iDataErrorCount > 1:
                    #self.showStatusError(True, Data)
                    self.showStepError(True, "Pas de données disponibles, avez-vous associé un compteur à votre compte et activé la courbe de charge sur le site d'Enedis ?")
                    self.bHasAFail = True
                self.sConnectionStep = "prod"
            # If status 429, retry later
            elif iStatus == 429:
                self.sConnectionStep = "retry"
                self.setNextConnectionForLater(self.iInterval)
            elif iStatus != 200:
                self.showStatusError(True, Data)
                self.sConnectionStep = "save"
                self.bHasAFail = True
            else:
                # Analyse data for hours
                if not self.exploreDataHours(Data, self.bProdMode):
                    self.bHasAFail = True
                # self.sConnectionStep = "save"

                # Still data to get, another batch ?
                if self.stillDays(False):
                    self.calculateDaysLeft()
                    self.sConnectionStep = "getdatahours"
                    self.getData(
                        API_ENDPOINT_DATA_PRODUCTION_LOAD_CURVE if self.bProdMode else API_ENDPOINT_DATA_CONSUMPTION_LOAD_CURVE,
                        self.dateBeginHours, self.dateEndHours)
                else:
                    # If at end of data for days and for peaks, continue to data for hours or save
                    # if not self.bPeakMode:
                    # No production peak available yet in Enedis API
                    if self.bProdMode or (not self.bPeakMode):
                        self.sConnectionStep = "prod"
                    # Get peak data
                    else:
                        self.resetDates()
                        self.sConnectionStep = "getdatapeakdays"
                        self.getData(
                            API_ENDPOINT_DATA_CONSUMPTION_MAX_POWER,
                            self.dateBeginDays, self.dateEndDays)

        # Ask data for peak data
        elif self.sConnectionStep == "getdatapeakdays":
            # Check if access token still valid
            iStatus = getStatus(Data)
            sError, sErrorDescription, sErrorUri = getError(Data)
            if (iStatus == 403) and (sError == "invalid_token") and (not self.bRefreshToken):
                self.sConnectionStep = "parseaccesstoken"
                self.refreshToken()
            elif iStatus == 403:
                self.isEnabled = False
                resetTokens()
                self.showSimpleStatusError(Data)
                self.showSimpleStepError(
                    "Le plugin va être arrêté. Relancez le en vous rendant dans Configuration/Matériel, en cliquant sur le plugin puis sur Modifier. Surveillez les logs pour obtenir le lien afin de renouveler le consentement pour la récupération des données auprès d'Enedis")
            elif iStatus == 404:
                self.sConnectionStep = "prod"
            # If status 429, retry later
            elif iStatus == 429:
                self.sConnectionStep = "retry"
                self.setNextConnectionForLater(self.iInterval)
            elif (iStatus != 200):
                self.showStatusError(False, Data)
                self.sConnectionStep = "save"
                self.bHasAFail = True
            else:
                if not self.exploreDataDays(Data, True, self.bProdMode):
                    self.bHasAFail = True
                # Still data to get, another batch ?
                if self.stillDays(True):
                    self.calculateDaysLeft()
                    # Normal data or peak data ?
                    self.sConnectionStep = "getdatapeakdays"
                    self.getData(
                        API_ENDPOINT_DATA_CONSUMPTION_MAX_POWER,
                        self.dateBeginDays, self.dateEndDays)
                else:
                    self.sConnectionStep = "prod"

        # first step to grab data
        if self.sConnectionStep == "start":
            self.lUsagePointIndex = getConfigItem("usage_points_id", [])
            if (len(self.lUsagePointIndex) > 0):
                self.resetDates()
                self.resetDayAccumulate()
                self.sConnectionStep = "nextcons"
            else:
                self.sConnectionStep = "done"
                self.bHasAFail = True
                self.showSimpleStepError("Erreur à la lecture des points de livraison")

        # if we didn't grab production data, do it
        if self.sConnectionStep == "prod":
            if (not self.bProdMode) and API_ENDPOINT_DATA_PRODUCTION_LOAD_CURVE:
                self.bProdMode = True
                self.sConnectionStep = "next"
            else:
                self.sConnectionStep = "save"

        # Next connection time depends on success
        if self.sConnectionStep == "save":
            if not self.saveDataToDb(self.sUsagePointId):
                self.bHasAFail = True
            # check if another usage point to grab
            self.iUsagePointIndex = self.iUsagePointIndex + 1
            if self.iUsagePointIndex < len(self.lUsagePointIndex):
                self.sConnectionStep = "nextcons"
            else:
                if not self.mergeCounters():
                    self.bHasAFail = True
                self.sConnectionStep = "done"

        # next consumption point
        if self.sConnectionStep == "nextcons":
            self.sUsagePointId = self.lUsagePointIndex[self.iUsagePointIndex]
            Domoticz.Log("Traitement pour le point de livraison " + self.sUsagePointId)
            self.bProdMode = False
            self.iDataErrorCount = 0
            self.sConnectionStep = "next"

        # next consumption or production point
        if self.sConnectionStep == "next":
            self.sConnectionStep = "getdatahours"
            self.getData(
                API_ENDPOINT_DATA_PRODUCTION_LOAD_CURVE if self.bProdMode else API_ENDPOINT_DATA_CONSUMPTION_LOAD_CURVE,
                self.dateBeginHours, self.dateEndHours)

        # Next connection time depends on success
        if self.sConnectionStep == "done":
            if self.bHasAFail:
                self.setNextConnection(False)
            self.clearData()
            self.sConnectionStep = "idle"
            Domoticz.Log("Prochaine connexion : " + datetimeToSQLDateTimeString(self.dateNextConnection))

    def dumpDictToLog(self, dictToLog):
        if self.iDebugLevel:
            if isinstance(dictToLog, dict):
                self.myDebug("Dict details (" + str(len(dictToLog)) + "):")
                for x in dictToLog:
                    if isinstance(dictToLog[x], dict):
                        self.myDebug("--->'" + x + " (" + str(len(dictToLog[x])) + "):")
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

        self.iAlternateDevice = 1
        lVersions = Parameters["DomoticzVersion"].split(".")
        if (len(lVersions) == 2):
            iVersionMaj = int(lVersions[0])
            iVersionMin = int(lVersions[1])
            iVersion = (iVersionMaj * 1000000) + iVersionMin
            if iVersion >= 4011774:
                self.iAlternateDevice = 0

        # For test purpose
        # self.iAlternateDevice = 1

        if self.iAlternateDevice:
            Domoticz.Log(
                "Ce plugin est compatible avec Domoticz version 3.9517 et plus récent, mais la vue par heure peut ne pas fonctionner avec la version 4.9700 et la visualisation d'énergie produite et de tarification horaire ne peuvent fonctionner qu'à partir de la version 4.11774")

            # Even if not used, Username and Password may still be in database because of previous versions. We don't want them, as it triggers an unwanted HTTP basic autorization header in old Domoticz Python Framework
        Parameters.pop("Username", None)
        Parameters.pop("Password", None)

        self.iHistoryDaysForHoursView = Parameters["Mode1"]
        self.iHistoryDaysForDaysView = Parameters["Mode2"]
        self.sTarif = Parameters["Mode4"]
        self.sConsumptionType1 = Parameters["Mode6"]
        self.sConsumptionType2 = Parameters["Mode5"]

        if not self.sConsumptionType1:
            self.sConsumptionType1 = "value_day"

        if not self.sConsumptionType2:
            self.sConsumptionType2 = "peak_day"

        try:
            self.iDebugLevel = int(Parameters["Mode3"])
        except ValueError:
            self.iDebugLevel = 0

        if self.iDebugLevel > 1:
            Domoticz.Debugging(1)

        if self.iDebugLevel == 3:
            resetTokens()

        if self.iDebugLevel >= 10:
            self.iAlternateAddress = 1
            self.iFalseCustomer = self.iDebugLevel - 10
        else:
            self.iAlternateAddress = 0
            self.iFalseCustomer = 0

        # History for short log is 7 days max (default to 7)
        try:
            self.iHistoryDaysForHoursView = int(self.iHistoryDaysForHoursView)
        except:
            self.iHistoryDaysForHoursView = 7
        if self.iHistoryDaysForHoursView < 0:
            self.iHistoryDaysForHoursView = 0
        elif self.iHistoryDaysForHoursView > 7:
            self.iHistoryDaysForHoursView = 7

        # History for short log is 730 days max (default to 60)
        try:
            self.iHistoryDaysForDaysView = int(self.iHistoryDaysForDaysView)
        except:
            self.iHistoryDaysForDaysView = 60
        if self.iHistoryDaysForDaysView < 1:
            self.iHistoryDaysForDaysView = 1
        elif self.iHistoryDaysForDaysView > 730:
            self.iHistoryDaysForDaysView = 730
        self.iHistoryDaysForPeakDaysView = self.iHistoryDaysForDaysView

        if self.sConsumptionType1.startswith("peak_") or self.sConsumptionType2.startswith("peak_"):
            self.bPeakMode = True
            if (self.sConsumptionType1.endswith("_cweek") or self.sConsumptionType2.endswith("_cweek")) and (
                    self.iHistoryDaysForPeakDaysView < 7):
                self.iHistoryDaysForPeakDaysView = 7

            if (self.sConsumptionType1.endswith("_lweek") or self.sConsumptionType2.endswith("_lweek")) and (
                    self.iHistoryDaysForPeakDaysView < 14):
                self.iHistoryDaysForPeakDaysView = 14

            if (self.sConsumptionType1.endswith("_cmonth") or self.sConsumptionType2.endswith("_cmonth")) and (
                    self.iHistoryDaysForPeakDaysView < 32):
                self.iHistoryDaysForPeakDaysView = 32

            if (self.sConsumptionType1.endswith("_lmonth") or self.sConsumptionType2.endswith("_lmonth")) and (
                    self.iHistoryDaysForPeakDaysView < 63):
                self.iHistoryDaysForPeakDaysView = 63

            if (self.sConsumptionType1.endswith("_year") or self.sConsumptionType2.endswith("_year")) and (
                    self.iHistoryDaysForPeakDaysView < 366):
                self.iHistoryDaysForPeakDaysView = 366
        else:
            self.bPeakMode = False
            if (self.sConsumptionType1.endswith("_cweek") or self.sConsumptionType2.endswith("_cweek")) and (
                    self.iHistoryDaysForDaysView < 7):
                self.iHistoryDaysForDaysView = 7

            if (self.sConsumptionType1.endswith("_lweek") or self.sConsumptionType2.endswith("_lweek")) and (
                    self.iHistoryDaysForDaysView < 14):
                self.iHistoryDaysForDaysView = 14

            if (self.sConsumptionType1.endswith("_cmonth") or self.sConsumptionType2.endswith("_cmonth")) and (
                    self.iHistoryDaysForDaysView < 32):
                self.iHistoryDaysForDaysView = 32

            if (self.sConsumptionType1.endswith("_lmonth") or self.sConsumptionType2.endswith("_lmonth")) and (
                    self.iHistoryDaysForDaysView < 63):
                self.iHistoryDaysForDaysView = 63

            if (self.sConsumptionType1.endswith("_year") or self.sConsumptionType2.endswith("_year")) and (
                    self.iHistoryDaysForDaysView < 366):
                self.iHistoryDaysForDaysView = 366

        Domoticz.Log(
            "Consommation à montrer sur le tableau de bord mis à " + self.sConsumptionType1 + " / " + self.sConsumptionType2)
        Domoticz.Log("Nombre de jours à récupérer pour la vue par heures mis à " + str(self.iHistoryDaysForHoursView))
        Domoticz.Log("Nombre de jours à récupérer pour les autres vues mis à " + str(self.iHistoryDaysForDaysView))
        if self.bPeakMode:
            Domoticz.Log(
                "Nombre de jours à récupérer pour le calcul du pic mis à " + str(self.iHistoryDaysForPeakDaysView))
        Domoticz.Log("Debug mis à " + str(self.iDebugLevel))

        # Parameter for tarif 1/2
        self.dHc = dict()
        self.bHasHc = parseHcParameter(self.dHc, self.sTarif)
        # self.dumpDictToLog(self.dHc)

        # most init
        self.__init__()

        Domoticz.Log(
            "Si vous ne voyez pas assez de données dans la vue par heures, augmentez le paramètre Log des capteurs qui se trouve dans Réglages / Paramètres / Historique des logs")

        self.dateNextConnection = datetime.now()

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

        if self.isEnabled and (datetime.now() > self.dateNextConnection):
            # self.savedDateEndDays = self.dateNextConnection
            self.resetDates(
                datetime(self.dateNextConnection.year, self.dateNextConnection.month, self.dateNextConnection.day))
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

# Parse HP/HC parameter string and store result in dHc
def parseHcParameter(dHc, sHcParameter):
    bHasHc = False
    bHcState = False
    iIndexParam = 0
    lHcParameter = sHcParameter.strip().replace(" ", "-").replace(" et ", "-").replace(":", "h").split("-")
    for iTimeIndex in range(0, 1440, 30):
        iTimeIndexMin = int(iTimeIndex % 60)
        iTimeIndexHour = int(iTimeIndex / 60)
        sTimeIndex = "{:01d}h{:02d}".format(iTimeIndexHour, iTimeIndexMin)
        if (iIndexParam < len(lHcParameter)) and (lHcParameter[iIndexParam] == sTimeIndex):
            bHcState = not bHcState
            iIndexParam = iIndexParam + 1
            hasHc = True
        # shift 1 hour
        iTimeIndexHour = (iTimeIndexHour + 1) % 24
        sTimeIndex = "{:01d}h{:02d}".format(iTimeIndexHour, iTimeIndexMin)
        dHc[sTimeIndex] = bHcState

    if bHcState:
        for iTimeIndex in range(0, 1440, 30):
            iTimeIndexMin = int(iTimeIndex % 60)
            iTimeIndexHour = int(iTimeIndex / 60)
            sTimeIndex = "{:01d}h{:02d}".format(iTimeIndexHour, iTimeIndexMin)
            if (iIndexParam < len(lHcParameter)) and (lHcParameter[iIndexParam] == sTimeIndex):
                break
            # shift 1 hour
            iTimeIndexHour = (iTimeIndexHour + 1) % 24
            sTimeIndex = "{:01d}h{:02d}".format(iTimeIndexHour, iTimeIndexMin)
            dHc[sTimeIndex] = True
    return bHasHc


def getConfigItem(Key=None, Default={}):
    Value = Default
    try:
        Config = Domoticz.Configuration()
        if (Key != None):
            Value = Config[Key]  # only return requested key if there was one
        else:
            Value = Config  # return the whole configuration if no key
    except KeyError:
        Value = Default
    except Exception as inst:
        Domoticz.Error("Domoticz.Configuration read failed: '" + str(inst) + "'")
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
        Domoticz.Error("Domoticz.Configuration operation failed: '" + str(inst) + "'")
    return Config


# Erase authorization tokens
def resetTokens():
    setConfigItem("usage_points_id", [])
    setConfigItem("token_type", "")
    setConfigItem("refresh_token", "")
    setConfigItem("access_token", "")


def initData(dDate):
    return {"consumption1": 0, "consumption2": 0, "production1": 0, "production2": 0, "consumptionpeak": 0, "productionpeak": 0, "date": dDate}


def dictToQuotedString(dParams):
    result = ""
    for sKey, sValue in dParams.items():
        if result:
            result += "&"
        result += sKey + "=" + quote(str(sValue))
    return result


# Grab error inside received JSON
def getError(Data):
    sError = ""
    sErrorDescription = ""
    sErrorUri = ""
    if Data and ("Data" in Data):
        try:
            dJson = json.loads(Data["Data"].decode())
        except ValueError:
            return ""
        else:
            if dJson:
                if "error" in dJson:
                    sError = dJson["error"]
                if "error_description" in dJson:
                    sErrorDescription = dJson["error_description"]
                if "error_uri" in dJson:
                    sErrorUri = dJson["error_uri"]
    if not sError:
        if Data and ("Headers" in Data) and ("WWW-Authenticate" in Data["Headers"]):
            sAuthenticate = Data["Headers"]["WWW-Authenticate"]
            if "," in sAuthenticate:
                dError = dict(item.split("=", 1) for item in sAuthenticate.split(","))
                if "error" in dError:
                    sError = dError["error"].strip("\"")
                if "error_description" in dError:
                    sErrorDescription = dError["error_description"].strip("\"")
                if "error_uri" in dError:
                    sErrorUri = dError["error_uri"].strip("\"")
    return sError, sErrorDescription, sErrorUri


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
            self.myDebug("'" + x + "':'" + str(Parameters[x]) + "'")
    self.myDebug("Device count: " + str(len(Devices)))
    for x in Devices:
        self.myDebug("Device:           " + str(x) + " - " + str(Devices[x]))
        self.myDebug("Device ID:       '" + str(Devices[x].ID) + "'")
        self.myDebug("Device Name:     '" + Devices[x].Name + "'")
        self.myDebug("Device iValue:    " + str(Devices[x].iValue))
        self.myDebug("Device sValue:   '" + Devices[x].sValue + "'")
        self.myDebug("Device LastLevel: " + str(Devices[x].LastLevel))
    return


# Convert Enedis datetime string to datetime object
def enedisDateTimeToDatetime(datetimeStr):
    # Buggy
    # return datetime.strptime(datetimeStr, "%d/%m/%Y")
    # Not buggy ?
    return datetime(*(strptime(datetimeStr[:19], "%Y-%m-%d %H:%M:%S")[0:6]))


# Convert Enedis date string to datetime object
def enedisDateToDatetime(datetimeStr):
    # Buggy
    # return datetime.strptime(datetimeStr, "%d/%m/%Y")
    # Not buggy ?
    return datetime(*(strptime(datetimeStr[:10], "%Y-%m-%d")[0:6]))


# Convert datetime object to Enedis date string
def datetimeToEnedisDateString(datetimeObj):
    return datetimeObj.strftime("%Y-%m-%d")


# Convert datetime object to Domoticz date string
def datetimeToSQLDateString(datetimeObj):
    return datetimeObj.strftime("%Y-%m-%d")


# Convert datetime object to Domoticz date and time string
def datetimeToSQLDateTimeString(datetimeObj):
    return datetimeObj.strftime("%Y-%m-%d %H:%M:%S")
