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
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License # along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
#
"""
<plugin key="linky" name="Linky" author="Barberousse" version="2.3.2" externallink="https://github.com/guillaumezin/DomoticzLinky">
    <params>
        <param field="Mode4" label="Heures creuses (vide pour désactiver, cf. readme pour la syntaxe)" width="500px" required="false" default="">
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
                <!-- <option label="Pic consommation semaine dernière" value="peak_lweek" />
                <option label="Pic consommation mois en cours" value="peak_cmonth" />
                <option label="Pic consommation mois dernier" value="peak_lmonth" />
                <option label="Pic consommation année en cours" value="peak_year" /> -->
            </options>
        </param>
        <param field="Mode6" label="Consommation à montrer sur le tableau de bord (affichage secondaire)" width="500px">
            <options>
                <option label="Consommation / production journée dernière" value="value_day"  default="true" />
                <option label="Consommation / production semaine en cours" value="value_cweek" />
                <option label="Consommation / production semaine dernière" value="value_lweek" />
                <option label="Consommation / production mois en cours" value="value_cmonth" />
                <!-- <option label="Consommation / production mois dernier" value="value_lmonth" />
                <option label="Consommation / production année en cours" value="value_year" /> -->
                <option label="Consommation / production horaire max journée dernière" value="max_day" />
                <option label="Consommation / production horaire max semaine en cours" value="max_cweek" />
                <option label="Consommation / production horaire max semaine dernière" value="max_lweek" />
                <option label="Consommation / production horaire max mois en cours" value="max_cmonth" />
                <!-- <option label="Consommation / production horaire max mois dernier" value="max_lmonth" />
                <option label="Consommation / production horaire max année en cours" value="max_year" /> -->
                <option label="Consommation / production horaire moyenne journée dernière" value="mean_day" />
                <option label="Consommation / production horaire moyenne semaine en cours" value="mean_cweek" />
                <option label="Consommation / production horaire moyenne semaine dernière" value="mean_lweek" />
                <option label="Consommation / production horaire moyenne mois en cours" value="mean_cmonth" />
                <!-- <option label="Consommation / production horaire moyenne mois dernier" value="mean_lmonth" />
                <option label="Consommation / production horaire moyenne année en cours" value="mean_year" /> -->
            </options>
        </param>
        <param field="Mode1" label="Nombre de jours à récupérer pour la vue par heures (0 min, pour désactiver la récupération par heures, 7 max)" width="50px" required="false" default="7"/>
        <param field="Mode2" label="Nombre de jours à récupérer pour les autres vues (730 max)" width="50px" required="false" default="7"/>
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
import json
from urllib.parse import quote
# import re
from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta
from time import strptime
# from random import randint
# import html
import re
import tempfile

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

USAGE_POINT_SEPARATOR = " / "
NB_WEEKS_LONG_HISTORY = 5

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
    bHasAFail = None
    bGlobalHasAFail = None
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
    iSavedHistoryDaysForDaysView = None
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
    # string: current usage point
    sUsagePointId = None
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
    # interval to retry
    iInterval = 5
    # no consumption data
    bNoConsumption = None
    # no production data
    bNoProduction = None
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
    # data dict with date string as index and consumption1, consumption2, production1, production2, consumptionpeak, productionpeak as float, peak as boolean and date as DateTime
    dData = None
    # dict with time (xxhmm format) as index and a boolean to indicate tariff
    dHc = None
    # dict with calculation to show on dashboard
    dCalculate = None
    # datetime
    dateNextConnection = None
    # integer: which device to use
    iAlternateDevice = 0
    # integer: false customoer
    iFalseCustomer = 0
    # integer: which address to use (production or sandbox)
    iAlternateAddress = 0
    # to know that we come from refresh token step
    bRefreshToken = None
    # dict of timeout
    dUsagePointTimeout = None
    # global timeout
    dtGlobalTimeout = None
    # last refresh
    dtNextRefresh = None
    # debug file
    fDebug = None
    # datetime: last data sent
    dtLastSend = None
    # has iHistoryDaysForDaysView changed?
    bHistoryDaysForDaysViewChanged = False
    # should we grab all days for day view?
    bHistoryDaysForDaysViewGrabAll = False
    
    def __init__(self):
        """
        Initialize the device

        Args:
            self: (todo): write your description
        """
        self.isStarted = False
        self.httpLoginConn = None
        self.httpDataConn = None
        self.sConnectionStep = "idle"
        self.bHasAFail = False
        self.bGlobalHasAFail = False
        self.sBuffer = None
        self.iTimeoutCount = 0
        self.iResendCount = 0
        self.iUsagePointIndex = 0
        self.lUsagePointIndex = []
        self.dUsagePointTimeout = {}
        self.dtLastSend = datetime(2000, 1, 1)

    def myDebug(self, message, bNoLog=False):
        """
        Logs a message to log.

        Args:
            self: (todo): write your description
            message: (str): write your description
            bNoLog: (todo): write your description
        """
        if (not bNoLog) and (self.iDebugLevel > 1):
            Domoticz.Log(message)
        if self.fDebug:
            try:
                self.fDebug.writelines(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3] + " " + message + "\n")
            except:
                pass

    def myLog(self, message):
        """
        Logs a message

        Args:
            self: (todo): write your description
            message: (str): write your description
        """
        Domoticz.Log(message)
        self.myDebug(message, True)

    def myStatus(self, message):
        """
        Acknowledge the status message

        Args:
            self: (todo): write your description
            message: (str): write your description
        """
        Domoticz.Status(message)
        self.myDebug("Status : " + message, True)

    def myError(self, message):
        """
        Called bytest message toDebug.

        Args:
            self: (todo): write your description
            message: (str): write your description
        """
        Domoticz.Error(message)
        self.myDebug("Erreur : " + message, True)

    # resend same data
    def reconnectAndResend(self):
        """
        Reconnect the connection.

        Args:
            self: (todo): write your description
        """
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
        """
        Send a connection to the device.

        Args:
            self: (todo): write your description
            conn: (todo): write your description
            data: (array): write your description
            address: (str): write your description
            port: (int): write your description
        """
        self.sMemData = data
        self.sBuffer = data
        self.sConnectionNextStep = self.sConnectionStep
        self.sMemConnectionStep = self.sConnectionStep
        self.iTimeoutCount = 0
        self.iResendCount = 0
        dtNow = datetime.now()
        # Prevent too quick connections, to not trigger protection mechanism
        if dtNow > (self.dtLastSend + timedelta(seconds=5)):
            self.dtLastSend = dtNow
            self.sConnectionStep = "connecting"
            conn = Domoticz.Connection(Name="HTTPS connection", Transport="TCP/IP", Protocol="HTTPS", Address=address,
                                Port=port)
            conn.Connect()
            return conn
        else:
            self.sConnectionStep = "retry"
            self.setNextConnectionForLater(self.iInterval)
            return None

    # Connect for login
    def connectAndSendForAuthorize(self, data):
        """
        Sends a message to the device.

        Args:
            self: (todo): write your description
            data: (array): write your description
        """
        self.bLoginConnect = True
        self.httpLoginConn = self.connectAndSend(self.httpLoginConn, data, LOGIN_BASE_URI[self.iAlternateAddress],
                                                 LOGIN_BASE_PORT[self.iAlternateAddress])

    # Connect for metering data
    def connectAndSendForMetering(self, data):
        """
        Sends a connection.

        Args:
            self: (todo): write your description
            data: (array): write your description
        """
        self.bLoginConnect = False
        self.httpDataConn = self.connectAndSend(self.httpDataConn, data, API_BASE_URI[self.iAlternateAddress],
                                                API_BASE_PORT[self.iAlternateAddress])

    # get default headers
    def initHeaders(self, uri):
        """
        Initialize the http headers.

        Args:
            self: (todo): write your description
            uri: (str): write your description
        """
        headers = dict(HEADERS)
        headers["User-Agent"] = "DomoticzLinkyPlugin/" + Parameters["Version"]
        headers["Host"] = uri
        return headers

    # get access token
    def getDeviceCode(self):
        """
        Get device information.

        Args:
            self: (todo): write your description
        """
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

    def showStatusError(self, hours, Data, bDebug=False):
        """
        Displays the status.

        Args:
            self: (todo): write your description
            hours: (todo): write your description
            Data: (array): write your description
            bDebug: (bool): write your description
        """
        sErrorSentence = "Erreur"
        iStatus = getStatus(Data)
        if iStatus != 504:
            sErrorSentence = sErrorSentence + " status : " + str(getStatus(Data))
        sError, sErrorDescription, sErrorUri = getError(Data)
        if sError:
            sErrorSentence = sErrorSentence + " - code " + sError
        if sErrorDescription:
            sErrorSentence = sErrorSentence + " - description : " + sErrorDescription
        if sErrorUri:
            sErrorSentence = sErrorSentence + " - URI : " + sErrorUri
        self.showStepError(hours, sErrorSentence, bDebug)

    def showSimpleStatusError(self, Data):
        """
        Shows the status of the status.

        Args:
            self: (todo): write your description
            Data: (array): write your description
        """
        sErrorSentence = "Erreur"
        iStatus = getStatus(Data)
        if iStatus != 504:
            sErrorSentence = sErrorSentence + " status : " + str(getStatus(Data))
        sError, sErrorDescription, sErrorUri = getError(Data)
        if sError:
            sErrorSentence = sErrorSentence + " - code " + sError
        if sErrorDescription:
            sErrorSentence = sErrorSentence + " - description : " + sErrorDescription
        if sErrorUri:
            sErrorSentence = sErrorSentence + " - URI : " + sErrorUri
        self.showSimpleStepError(sErrorSentence)

    def parseDeviceCode(self, Data):
        """
        Dump a data object

        Args:
            self: (todo): write your description
            Data: (todo): write your description
        """
        self.dumpDictToLog(Data)
        iStatus = getStatus(Data)
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
                    self.myError(
                        "Connectez-vous à l'adresse " + sUrl + " pour lancer la demande de consentement avec le code " + sUserCode)
                    return "done"
                else:
                    self.showSimpleStepError("Données incomplètes")
            else:
                self.showSimpleStepError("Pas de données reçue")
        else:
            self.showSimpleStatusError(Data)
        return "retry"

    # get access token
    def getAccessToken(self):
        """
        Get the access token.

        Args:
            self: (todo): write your description
        """
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
        """
        Refresh the token

        Args:
            self: (todo): write your description
        """
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
        """
        Parses an access token.

        Args:
            self: (todo): write your description
            Data: (todo): write your description
        """
        self.dumpDictToLog(Data)
        iStatus = getStatus(Data)
        sError, sErrorDescription, sErrorUri = getError(Data)
        sError = sError.lower()
        if (sError == "unauthorized") or (sError == "invalid_grant"):
            self.showSimpleStatusError(Data)
            return "error"
        if sError == "authorization_pending":
            self.myDebug("pending")
            if Data and ("Data" in Data):
                try:
                    dJson = json.loads(Data["Data"].decode())
                except ValueError as err:
                    self.showSimpleStepError("Les données reçues ne sont pas du JSON : " + str(err))
                    return "retry"
                if dJson and ("interval" in dJson):
                    try:
                        self.iInterval = int(dJson["interval"])
                    except:
                        self.iInterval = 5
            return "pending"
        elif iStatus == 200:
            if Data and ("Data" in Data):
                try:
                    dJson = json.loads(Data["Data"].decode())
                except ValueError as err:
                    self.showSimpleStepError("Les données reçues ne sont pas du JSON : " + str(err))
                    return "retry"
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
        return "retry"

    # Get data
    def getData(self, uri, start, end):
        """
        Make a get a get request

        Args:
            self: (todo): write your description
            uri: (str): write your description
            start: (int): write your description
            end: (todo): write your description
        """
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
        """
        Returns a device name for a specific device.

        Args:
            self: (todo): write your description
            sUsagePointCurrentId: (str): write your description
        """
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
        """
        This method adds to add tomodels todo.

        Args:
            self: (todo): write your description
            oDevice: (todo): write your description
            fConsumption1: (todo): write your description
            fConsumption2: (todo): write your description
            fProduction1: (todo): write your description
            fProduction2: (todo): write your description
            sDate: (todo): write your description
        """
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
        """
        Updates a device.

        Args:
            self: (todo): write your description
            oDevice: (todo): write your description
            fConsoVal1: (todo): write your description
            fConsoVal2: (todo): write your description
            fProdVal1: (str): write your description
            fProdVal2: (str): write your description
            fSecVal1: (todo): write your description
            fSecVal2: (todo): write your description
        """
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
            Options=self.lOptions[self.iAlternateDevice],
            TimedOut=0)
        return True

    # Show error in state machine context
    def showSimpleStepError(self, logMessage, bDebug=False):
        """
        Show the log message

        Args:
            self: (todo): write your description
            logMessage: (str): write your description
            bDebug: (bool): write your description
        """
        sMessage = "durant l'étape : " + self.sConnectionStep + " - " + logMessage
        if bDebug:
            self.myDebug(sMessage)
        else:
            self.myError(sMessage)

    # Show error in state machine context with dates
    def showStepError(self, hours, logMessage, bDebug=False):
        """
        Show the log

        Args:
            self: (todo): write your description
            hours: (todo): write your description
            logMessage: (str): write your description
            bDebug: (bool): write your description
        """
        if hours:
            sMessage = "durant l'étape " + self.sConnectionStep + " de " + datetimeToEnedisDateString(
                self.dateBeginHours) + " à " + datetimeToEnedisDateString(self.dateEndHours) + " - " + logMessage
        else:
            sMessage = "durant l'étape " + self.sConnectionStep + " de " + datetimeToEnedisDateString(
                self.dateBeginDays) + " à " + datetimeToEnedisDateString(self.dateEndDays) + " - " + logMessage
        if bDebug:
            self.myDebug(sMessage)
        else:
            self.myError(sMessage)

    # Parse HP/HC parameter string and store result in dHc
    def parseHcParameter(self, sHcParameter):
        """
        Parse a string representing the device object.

        Args:
            self: (todo): write your description
            sHcParameter: (str): write your description
        """
        self.dHc = {}
        sLocalUsagePointId = "all"
        iWeekday = 7
        sProd = "all"
        
        sHcParameter = sHcParameter.lower().strip()

        # Exemple 963222123213 12h30-14h00
        # https://regex101.com/r/cMWfqj/11
        for matchHc in re.finditer(r"(?:(\d+)(?:$|\s))?(?:([a-zéè]+)(?:$|\s))?(?:([a-zéè]+)(?:$|\s))?(?:(\d+)\s*[h:]\s*(\d+)?\s*(?:[-_aà]|to)+\s*(\d+)\s*[h:]\s*(\d+)?)?", sHcParameter):
            #Domoticz.Log("match " + matchHc.group(1) + " "  + matchHc.group(2) + " "  + matchHc.group(3) + " " + matchHc.group(4) + " " + matchHc.group(5) + " " + matchHc.group(6) + " " + matchHc.group(7))
            if matchHc.group(1):
                sLocalUsagePointId = matchHc.group(1).upper().strip()
                sProd = "all"
                iWeekday = 7
                #Domoticz.Log(sLocalUsagePointId)
            sMG2 = matchHc.group(2)
            if sMG2:
                sMG2 = sMG2.lower().strip()
                sMG3 = matchHc.group(3)
                if sMG3:
                    sMG3 = sMG3.lower().strip()
                    sDay = sMG3
                else:
                    sDay = sMG2
                if sMG2.startswith("p"):
                    sProd = "prod"
                    iWeekday = 7
                #Domoticz.Log(sDay)
                if sDay.startswith("lu") or sDay.startswith("mo"):
                    iWeekday = 0
                elif sDay.startswith("ma") or sDay.startswith("tu"):
                    iWeekday = 1
                elif sDay.startswith("me") or sDay.startswith("we"):
                    iWeekday = 2
                elif sDay.startswith("je") or sDay.startswith("th"):
                    iWeekday = 3
                elif sDay.startswith("ve") or sDay.startswith("fr"):
                    iWeekday = 4
                elif sDay.startswith("sa") or sDay.startswith("sa"):
                    iWeekday = 5
                elif sDay.startswith("di") or sDay.startswith("su"):
                    iWeekday = 6
                elif sDay.startswith("fe") or sDay.startswith("fé") or sDay.startswith("fè") or sDay.startswith("jo") or sDay.startswith("pu")  or sDay.startswith("ba") or sDay.startswith("ho"):
                    iWeekday = 8
                else:
                    iWeekday = 7
                #Domoticz.Log(sLocalUsagePointId)
            if not sLocalUsagePointId in self.dHc:
                self.dHc[sLocalUsagePointId] = {}
            if not sProd in self.dHc[sLocalUsagePointId]:
                self.dHc[sLocalUsagePointId][sProd] = {}
            if not iWeekday in self.dHc[sLocalUsagePointId][sProd]:
                self.dHc[sLocalUsagePointId][sProd][iWeekday] = []
            if matchHc.group(4):
                iHoursBegin = int(matchHc.group(4))
                iHoursEnd = int(matchHc.group(6))

                if matchHc.group(5):
                    iMinutesBegin = int(matchHc.group(5))
                else:
                    iMinutesBegin = 0
                if matchHc.group(7):
                    iMinutesEnd = int(matchHc.group(7))
                else:
                    iMinutesEnd = 0

                if iHoursBegin > 23:
                    iHoursBegin = 23
                    iMinutesBegin = 59
                elif iHoursBegin < 0:
                    iHoursBegin = 0

                if iHoursEnd > 23:
                    iHoursEnd = 23
                    iMinutesEnd = 59
                elif iHoursEnd < 0:
                    iHoursEnd = 0

                if iMinutesBegin > 59:
                    iMinutesBegin = 59
                elif iMinutesBegin < 0:
                    iMinutesBegin = 0

                if iMinutesEnd > 59:
                    iMinutesEnd = 59
                elif iMinutesEnd < 0:
                    iMinutesEnd = 0
                    
                datetimeBegin = datetime(2010, 1, 1, iHoursBegin, iMinutesBegin)
                datetimeEnd = datetime(2010, 1, 1, iHoursEnd, iMinutesEnd)
                timeBegin = datetimeBegin.time()
                timeEnd = datetimeEnd.time()
                if datetimeEnd <  datetimeBegin:
                    self.dHc[sLocalUsagePointId][sProd][iWeekday].append([timeBegin, time(23,59,59,999999)])
                    self.dHc[sLocalUsagePointId][sProd][iWeekday].append([time(), timeEnd])
                else:
                    self.dHc[sLocalUsagePointId][sProd][iWeekday].append([timeBegin, timeEnd])
        #self.dumpDictToLog(self.dHc)

    # Check date if in cost 1 or cost 2
    def isCost2(self, dtDate, bProduction=False):
        """
        Returns true if dt is a date isCost

        Args:
            self: (todo): write your description
            dtDate: (todo): write your description
            bProduction: (todo): write your description
        """
        dtDate = dtDate - timedelta(minutes=30)
        tDate = dtDate.time()
        dDate = dtDate.date()
        iWeekday = dtDate.weekday()
        lUsagePointCurrentId = self.sUsagePointId.split(USAGE_POINT_SEPARATOR)
        if bProduction and (len(lUsagePointCurrentId) > 1):
            sLocalUsagePointId = lUsagePointCurrentId[1]
        else:
            sLocalUsagePointId = lUsagePointCurrentId[0]
        if sLocalUsagePointId in self.dHc:
            dHc = self.dHc[sLocalUsagePointId]
        elif "all" in self.dHc:
            dHc = self.dHc["all"]
        else:
            return False

        if bProduction:
            if "prod" in dHc:
                dPHc = dHc["prod"]
            elif "all" in dHc:
                dPHc = dHc["all"]
            else:
                return False
        else:
            if "all" in dHc:
                dPHc = dHc["all"]
            else:
                return False
            
        if JoursFeries.is_bank_holiday(dDate) and (8 in dPHc):
            lHc = dPHc[8]
        elif iWeekday in dPHc:
            lHc = dPHc[iWeekday]
        elif 7 in dPHc:
            lHc = dPHc[7]
        else:
            return False            

        for lDateInterval in lHc:
            if (tDate >= lDateInterval[0]) and (tDate < lDateInterval[1]):
                return True
        return False

    # Check current usage point has 2 costs
    def has2Costs(self, sUsagePointCurrentId):
        """
        Return true if the given lcid has a } has the given point

        Args:
            self: (todo): write your description
            sUsagePointCurrentId: (str): write your description
        """
        lUsagePointCurrentId = sUsagePointCurrentId.split(USAGE_POINT_SEPARATOR)
        if len(lUsagePointCurrentId) > 1:
            return ("all" in self.dHc) or (lUsagePointCurrentId[0] in self.dHc) or (lUsagePointCurrentId[1] in self.dHc)
        else:
            return ("all" in self.dHc) or (lUsagePointCurrentId[0] in self.dHc)
    
    # Write data from memory to Domoticz DB
    def saveDataToDb(self, sUsagePointCurrentId):
        """
        Save the data of the specified target

        Args:
            self: (todo): write your description
            sUsagePointCurrentId: (todo): write your description
        """
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
            # transform hour data in day data
            dOneData["consumption1"] = 0
            for iHour, fValue in dOneData["consumption1_hours"].items():
                dOneData["consumption1"] = dOneData["consumption1"] + fValue
            dOneData["consumption2"] = 0
            for iHour, fValue in dOneData["consumption2_hours"].items():
                dOneData["consumption2"] = dOneData["consumption2"] + fValue
            dOneData["production1"] = 0
            for iHour, fValue in dOneData["production1_hours"].items():
                dOneData["production1"] = dOneData["production1"] + fValue
            dOneData["production2"] = 0
            for iHour, fValue in dOneData["production2_hours"].items():
                dOneData["production2"] = dOneData["production2"] + fValue
            # hour
            if len(sDate) > 10:
                # We don't want the last day = today, it breaks CounterToday value and log view
                self.dayAccumulate(sUsagePointCurrentId, dOneData["date"], dOneData)
                if not dOneData["data"]:
                    continue
                if dOneData["date"] >= self.savedDateEndDays2:
                    # self.myError("Skip " + sDate)
                    continue
                # We want only iHistoryDaysForHoursView days
                if (self.iHistoryDaysForHoursView < 1) or (dOneData["date"] < self.dateBeginDaysHistoryView):
                    # self.myError("Skip " + sDate)
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
                if not dOneData["data"]:
                    continue
                # We don't want the last day = today, it's incomplete
                if dOneData["date"] >= self.savedDateEndDays2:
                    # self.myError("Skip " + sDate)
                    continue
                if not self.addToDevice(oDevice, dOneData["consumption1"], dOneData["consumption2"], dOneData["production1"],
                                        dOneData["production2"], sDate):
                    return False
        # self.dumpDictToLog(self.dCalculate)
        # Do not return an error if dashboard update is not possible, to prevent retries all day long
        self.updateDashboard(oDevice, sUsagePointCurrentId)
        return True

    # Merge counters with only consumption with counters with only production into new virtual counters
    def mergeCounters(self):
        """
        Merge all the stats to the current disk

        Args:
            self: (todo): write your description
        """
        bResult = True
        dCalculateCopy = self.dCalculate.copy()
        for sUsagePointConsumptionId in dCalculateCopy:
            # Check if consumption only
            if (
                not dCalculateCopy[sUsagePointConsumptionId]["production1"]["value_year"]
                and not dCalculateCopy[sUsagePointConsumptionId]["production2"]["value_year"]
                and (dCalculateCopy[sUsagePointConsumptionId]["consumption1"]["value_year"]
                    or dCalculateCopy[sUsagePointConsumptionId]["consumption2"]["value_year"])
            ):
                for sUsagePointProductionId in dCalculateCopy:
                    # Merge with production only
                    if (
                        not dCalculateCopy[sUsagePointProductionId]["consumption1"]["value_year"]
                        and not dCalculateCopy[sUsagePointProductionId]["consumption2"]["value_year"]
                        and (dCalculateCopy[sUsagePointProductionId]["production1"]["value_year"]
                            or dCalculateCopy[sUsagePointProductionId]["production2"]["value_year"])
                    ):
                        # Do merge
                        sNewUsagePointId = sUsagePointConsumptionId + USAGE_POINT_SEPARATOR + sUsagePointProductionId

                        # copy consumption data to merged device
                        self.dData[sNewUsagePointId] = self.dData[sUsagePointConsumptionId].copy()

                        # copy production data to merged device where dates coincide for consumption
                        for sDate, dMergedData in self.dData[sNewUsagePointId].items():
                            if sDate in self.dData[sUsagePointProductionId]:
                                dProdData = self.dData[sUsagePointProductionId][sDate]
                                dMergedData["production1"] = dProdData["production1"]
                                for iHour, fValue in dProdData["production1_hours"].items():
                                    dMergedData["production1_hours"][iHour] = fValue
                                dMergedData["production2"] = dProdData["production2"]
                                for iHour, fValue in dProdData["production2_hours"].items():
                                    dMergedData["production2_hours"][iHour] = fValue
                                dMergedData["productionpeak"] = dProdData["productionpeak"]
                                dMergedData["data"] = dMergedData["data"] or dProdData["data"]
                                dMergedData["peak"] = dMergedData["peak"] or dProdData["peak"]

                        # create production data to merged device where dates don't coincide for consumption
                        for sDate, dProdData in self.dData[sUsagePointConsumptionId].items():
                            if sDate not in self.dData[sNewUsagePointId]:
                                dMergedData = initData(dProdData["date"])
                                dMergedData["production1"] = dProdData["production1"]
                                for iHour, fValue in dProdData["production1_hours"].items():
                                    dMergedData["production1_hours"][iHour] = fValue
                                dMergedData["production2"] = dProdData["production2"]
                                for iHour, fValue in dProdData["production2_hours"].items():
                                    dMergedData["production2_hours"][iHour] = fValue
                                dMergedData["productionpeak"] = dProdData["productionpeak"]
                                dMergedData["data"] = dProdData["data"]
                                dMergedData["peak"] = dProdData["peak"]
                                self.dData[sNewUsagePointId][sDate] = dMergedData

                        self.bNoConsumption = False
                        self.bNoProduction = False
                        if not self.saveDataToDb(sNewUsagePointId):
                            bResult = False
        return bResult

    # Store data in memory
    def storeData(self, fData, sDate, dDate, bProduction, bCost2, bPeak):
        """
        Stores the data of the instance.

        Args:
            self: (todo): write your description
            fData: (array): write your description
            sDate: (todo): write your description
            dDate: (todo): write your description
            bProduction: (str): write your description
            bCost2: (todo): write your description
            bPeak: (todo): write your description
        """
        if self.sUsagePointId not in self.dData:
            self.dData[self.sUsagePointId] = dict()
        if sDate not in self.dData[self.sUsagePointId]:
            self.dData[self.sUsagePointId][sDate] = initData(dDate)
        if bPeak:
            self.dData[self.sUsagePointId][sDate]["peak"] = True
            if bProduction:
                self.dData[self.sUsagePointId][sDate]["productionpeak"] = fData
            else:
                pfData = self.dData[self.sUsagePointId][sDate]["consumptionpeak"] = fData
        else:
            self.dData[self.sUsagePointId][sDate]["data"] = True
            if bProduction:
                if bCost2:
                    pfData = self.dData[self.sUsagePointId][sDate]["production2_hours"]
                else:
                    pfData = self.dData[self.sUsagePointId][sDate]["production1_hours"]
            else:
                if bCost2:
                    pfData = self.dData[self.sUsagePointId][sDate]["consumption2_hours"]
                else:
                    pfData = self.dData[self.sUsagePointId][sDate]["consumption1_hours"]
            pfData[dDate.hour] = fData

    # Manage data in memory for hours
    def manageDataHours(self, fData, dDate, bProduction=False):
        """
        Manage the data for the database

        Args:
            self: (todo): write your description
            fData: (todo): write your description
            dDate: (todo): write your description
            bProduction: (todo): write your description
        """
        sDateTime = datetimeToSQLDateTimeString(dDate)
        bCost2 = self.isCost2(dDate, bProduction)
        # Store hour
        self.storeData(fData, sDateTime, dDate, bProduction, bCost2, False)
        # Accumulate for day
        dDate = dDate - timedelta(hours=1)
        sDate = datetimeToSQLDateString(dDate)
        self.storeData(fData, sDate, dDate, bProduction, bCost2, False)

    # Manage data in memory for days
    def manageDataDays(self, fData, dDate, bPeak=False, bProduction=False):
        """
        Updates the datetime object

        Args:
            self: (todo): write your description
            fData: (todo): write your description
            dDate: (todo): write your description
            bPeak: (todo): write your description
            bProduction: (str): write your description
        """
        sDate = datetimeToSQLDateTimeString(dDate)
        self.storeData(fData, sDate, dDate, bProduction, False, bPeak)

    # Grab hours data inside received JSON data for short log
    def exploreDataHours(self, Data, bProduction=False):
        """
        Determine if data was received

        Args:
            self: (todo): write your description
            Data: (array): write your description
            bProduction: (str): write your description
        """
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
                        sReceivedUsagePointId = dJson["meter_reading"]["usage_point_id"]
                    except:
                        self.showStepError(True, "Données reçues sans numéro de point de livraison")
                        return False
                    if sReceivedUsagePointId != self.sUsagePointId:
                        self.showStepError(True, "Données reçues pour un autre point de livraison")
                        return False
                    # We accumulate data because Enedis sends kWh for every 30 minutes and Domoticz expects data only for every hour
                    accumulation = 0.0
                    currentDay = -1
                    steps = 1.0
                    dataSeen = False
                    for index, data in enumerate(dJson["meter_reading"]["interval_reading"]):
                        try:
                            val = float(data["value"])
                        except:
                            val = -1.0
                        if (val >= 0.0) and ("date" in data):
                            dataSeen = True
                            # cf. constructTime() call in WebServer.cpp to see if time shift needed
                            #curDate = enedisDateTimeToDatetime(data["date"]) + timedelta(hours=1)
                            curDate = enedisDateTimeToDatetime(data["date"])
                            accumulation = accumulation + val
                            # self.myLog("Value " + str(val) + " " + datetimeToSQLDateTimeString(curDate))
                            if curDate.minute == 0:
                                # Check that we had enough data, as expected
                                # self.myLog("accumulation " + str(accumulation / steps) + " " + datetimeToSQLDateTimeString(curDate))
                                # if not self.createAndAddToDevice(accumulation / steps, datetimeToSQLDateTimeString(curDate)):
                                # return False
                                self.manageDataHours(accumulation / steps, curDate, bProduction)
                                accumulation = 0.0
                                steps = 0.0
                            steps = steps + 1.0
                    if not dataSeen:
                        self.showStepError(True, "Données manquantes")
                    return dataSeen
                else:
                    self.showStepError(True, "Erreur à la réception de données JSON")
        else:
            self.showStepError(True, "Aucune donnée reçue")
        return False

    def resetCalculate(self, sUsagePointCurrentId):
        """
        Reset the progress bar.

        Args:
            self: (todo): write your description
            sUsagePointCurrentId: (todo): write your description
        """
        self.dCalculate[sUsagePointCurrentId] = {"consumption1": dict(), "consumption2": dict(), "production1": dict(),
                                                 "production2": dict(), "consumptionpeak": dict(),
                                                 "productionpeak": dict()}

    # Reset counters for power consumption
    def resetDayAccumulate(self):
        """
        Reset the day.

        Args:
            self: (todo): write your description
        """
        self.curDay = self.savedDateEndDays2.replace(hour=0, minute=0, second=0, microsecond=0)
        self.prevDay = self.curDay - timedelta(days=1)
        self.fdmonth = self.prevDay.replace(day=1)
        ldpmonth = self.fdmonth - timedelta(days=1)
        self.fdpmonth = ldpmonth.replace(day=1)
        self.fdweek = self.prevDay - timedelta(days=self.prevDay.weekday())
        ldpweek = self.fdweek - timedelta(days=1)
        self.fdpweek = ldpweek - timedelta(days=6)
        self.fdyear = self.prevDay.replace(day=1, month=1)
        #self.myLog(
        #    str(self.prevDay) + " " + str(self.curDay) + " " + str(self.fdmonth) + " " + str(self.fdpmonth) + " " + str(
        #       self.fdweek) + " " + str(self.fdpweek) + " " + str(self.fdyear))

    # Calculate and store
    def modifyCalculation(self, dCalculation, sParameter, fVal):
        """
        Modifies a parameter values of a parameter.

        Args:
            self: (todo): write your description
            dCalculation: (str): write your description
            sParameter: (todo): write your description
            fVal: (todo): write your description
        """
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

    def doCalculation(self, dateCur, dCalculation, fVal):
        """
        \ writesculation of the given date.

        Args:
            self: (todo): write your description
            dateCur: (todo): write your description
            dCalculation: (str): write your description
            fVal: (str): write your description
        """
        if (dateCur > self.fdweek):
            self.modifyCalculation(dCalculation, "cweek", fVal)
        if (self.fdpweek < dateCur <= self.fdweek):
            self.modifyCalculation(dCalculation, "lweek", fVal)
        if (dateCur > self.fdmonth):
            self.modifyCalculation(dCalculation, "cmonth", fVal)
        if (self.fdpmonth < dateCur <= self.fdmonth):
            self.modifyCalculation(dCalculation, "lmonth", fVal)
        if (dateCur > self.fdyear):
            self.modifyCalculation(dCalculation, "year", fVal)
        if (self.prevDay < dateCur <= self.curDay):
            self.modifyCalculation(dCalculation, "day", fVal)

    # Accumulate power consumption
    def dayAccumulate(self, sUsagePointCurrentId, dateCur, dVal):
        """
        This method is the day of the day.

        Args:
            self: (todo): write your description
            sUsagePointCurrentId: (todo): write your description
            dateCur: (todo): write your description
            dVal: (todo): write your description
        """
        if dVal["peak"]:
            self.doCalculation(dateCur, self.dCalculate[sUsagePointCurrentId]["consumptionpeak"], dVal["consumptionpeak"])
            self.doCalculation(dateCur, self.dCalculate[sUsagePointCurrentId]["productionpeak"], dVal["productionpeak"])
        if dVal["data"]:
            self.doCalculation(dateCur, self.dCalculate[sUsagePointCurrentId]["consumption1"], dVal["consumption1"])
            self.doCalculation(dateCur, self.dCalculate[sUsagePointCurrentId]["production1"], dVal["production1"])
            self.doCalculation(dateCur, self.dCalculate[sUsagePointCurrentId]["consumption2"], dVal["consumption2"])
            self.doCalculation(dateCur, self.dCalculate[sUsagePointCurrentId]["production2"], dVal["production2"])

    # Grab days data inside received JSON data for history
    def exploreDataDays(self, Data, bPeak, bProduction=False):
        """
        Returns the data from the data returned from the data

        Args:
            self: (todo): write your description
            Data: (array): write your description
            bPeak: (todo): write your description
            bProduction: (str): write your description
        """
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
                        sReceivedUsagePointId = str(dJson["meter_reading"]["usage_point_id"])
                    except:
                        self.showStepError(True, "Données reçues sans numéro de point de livraison")
                        return False
                    if sReceivedUsagePointId != self.sUsagePointId:
                        self.showStepError(True, "Données reçues pour un autre point de livraison")
                        return False
                    dataSeen = False
                    for index, data in enumerate(dJson["meter_reading"]["interval_reading"]):
                        try:
                            val = float(data["value"])
                        except:
                            val = -1.0
                        if (val >= 0.0) and ("date" in data):
                            dataSeen = True
                            if bPeak:
                                curDate = enedisDateTimeToDatetime(data["date"])
                            else:
                                curDate = enedisDateToDatetime(data["date"])
                            #self.myLog("Value " + str(val) + " " + datetimeToSQLDateString(curDate))
                            # self.dumpDictToLog(values)
                            # self.dayAccumulate(curDate, val)
                            # if not self.createAndAddToDevice(val, datetimeToSQLDateString(curDate)):
                            # return False
                            self.manageDataDays(val, curDate, bPeak, bProduction)
                    if not dataSeen:
                        self.showStepError(False, "Données manquantes")
                    return dataSeen
                else:
                    self.showStepError(False, "Erreur à la réception de données JSON")
        else:
            self.showStepError(False, "Aucune donnée reçue")
        return False

    # Update dashboard with accumulated value
    def updateDashboard(self, oDevice, sUsagePointCurrentId):
        """
        Update the oid

        Args:
            self: (todo): write your description
            oDevice: (todo): write your description
            sUsagePointCurrentId: (todo): write your description
        """
        if not sUsagePointCurrentId in self.dCalculate:
            return False
        self.dumpDictToLog(self.dCalculate[sUsagePointCurrentId])

        fConsoVal1 = -1
        fConsoVal2 = -1
        fProdVal1 = -1
        fProdVal2 = -1
        # silently ignore missing peak values, it happens too often
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
            bTwoValuesT1 = self.has2Costs(sUsagePointCurrentId)

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
            bTwoValuesT2 = self.has2Costs(sUsagePointCurrentId)

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
            fConsoVal2 = 0
            fProdVal2 = 0

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

        # Set value to 0 when no production only or no consumption only, to not trigger error
        if self.bNoConsumption and (not self.bNoProduction):
            fConsoVal1 = 0
            fConsoVal2 = 0
            fSecVal1 = 0
            fSecVal2 = 0
        elif self.bNoProduction and (not self.bNoConsumption):
            fProdVal1 =0
            fProdVal2 =0

        if (fConsoVal1 < 0) or (fConsoVal2 < 0) or (fProdVal1 < 0) or (fProdVal2 < 0) or (fSecVal1 < 0) or (fSecVal2 < 0):
            self.showStepError(False, "Données manquantes pour mettre à jour le tableau de bord")
            return False
        else:
            dtTimeout = setTimeout()
            self.dtGlobalTimeout = dtTimeout
            self.dUsagePointTimeout[sUsagePointCurrentId] = dtTimeout
            return self.updateDevice(oDevice, fConsoVal1, fConsoVal2, fProdVal1, fProdVal2, fSecVal1, fSecVal2)

    # Calculate days and date left for next batch
    def resetDates(self, dDateEnd=None):
        """
        Reset the modification.

        Args:
            self: (todo): write your description
            dDateEnd: (str): write your description
        """
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
        self.bFirstBatch = True

    # Calculate days and date left for next batch
    def calculateDaysLeft(self):
        """
        Calculate the current min and max number of the screen.

        Args:
            self: (todo): write your description
        """
        # No more than 365 days at once
        self.iDaysLeft = self.iDaysLeft - 365
        if self.iDaysLeft <= 0:
            daysToGet = self.iDaysLeft + 365
        else:
            daysToGet = 365
        self.dateBeginDays = self.savedDateEndDays - timedelta(days=daysToGet)
        self.dateEndDays = self.savedDateEndDays
        self.savedDateEndDays = self.dateBeginDays

        # self.myLog("Dates : " + datetimeToSQLDateTimeString(self.dateBeginDays) + " " + datetimeToSQLDateTimeString(self.dateEndDays) + " " + datetimeToSQLDateTimeString(self.savedDateEndDays))

        # No more than 7 days at once
        self.iDaysLeftHoursView = self.iDaysLeftHoursView - 7
        if self.iDaysLeftHoursView <= 0:
            daysToGet = self.iDaysLeftHoursView + 7
        else:
            daysToGet = 7
        self.dateBeginHours = self.savedDateEndDaysForHoursView - timedelta(days=daysToGet)
        self.dateEndHours = self.savedDateEndDaysForHoursView
        self.savedDateEndDaysForHoursView = self.dateBeginHours

        self.bFirstBatch = False

        # self.myLog("Dates : " + datetimeToSQLDateTimeString(self.dateBeginHours) + " " + datetimeToSQLDateTimeString(self.dateEndHours) + " " + datetimeToSQLDateTimeString(self.savedDateEndDaysForHoursView))

    # Still data to get
    def stillDays(self, bPeak):
        """
        Return the number of rows of the viewable.

        Args:
            self: (todo): write your description
            bPeak: (todo): write your description
        """
        if bPeak:
            return self.iDaysLeft > 0
        else:
            return self.iDaysLeftHoursView > 0

    # limit history days to prevent Enedis servers overload
    def setHistoryDays(self):
        """
        Sets the current history for this item.

        Args:
            self: (todo): write your description
        """
        iNbDaysLongHistory = NB_WEEKS_LONG_HISTORY * 7
        bGrabAll = False
        if self.bHistoryDaysForDaysViewChanged:
            bGrabAll = True
        else:
            dtNow = datetime.now()
            dtLastConnection = datetime.fromtimestamp(getConfigItem("previous_successful_connection_date", datetime(2000, 1, 1)))
            dtGrab = datetime.fromtimestamp(getConfigItem("next_history_grab_date", datetime(2000, 1, 1)))
            if (dtGrab <= dtNow) or ((dtLastConnection + timedelta(days = self.iSavedHistoryDaysForDaysView)) <= dtNow):
                bGrabAll = True
        if bGrabAll and (self.iSavedHistoryDaysForDaysView > iNbDaysLongHistory):
            self.myStatus("Récupération des données avec l'historique complet")
            self.bHistoryDaysForDaysViewGrabAll = True
        else:
            self.myStatus("Récupération des données avec l'historique court")
            if self.iHistoryDaysForDaysView > iNbDaysLongHistory:
                self.iHistoryDaysForDaysView = iNbDaysLongHistory
            self.bHistoryDaysForDaysViewGrabAll = False

    # Save date of connection if successful
    def savePreviousSuccessfulConnectionDate(self, bError):
        """
        Creates the current working copy of the current working copy.

        Args:
            self: (todo): write your description
            bError: (todo): write your description
        """
        iNbDaysLongHistory = NB_WEEKS_LONG_HISTORY * 7
        dtNow = datetime.now()
        if not bError:
            setConfigItem("previous_successful_connection_date", dtNow)
            if self.bHistoryDaysForDaysViewGrabAll:
                dtGrab = dtNow + timedelta(days = self.iSavedHistoryDaysForDaysView / 2)
                setConfigItem("next_history_grab_date", dtGrab)
        elif self.bHistoryDaysForDaysViewGrabAll:
            iDaysRand = (round(dtNow.microsecond / 10000) % 7) + 1
            dtGrab = dtNow + timedelta(days = iDaysRand)
            setConfigItem("next_history_grab_date", dtGrab)
        if self.iSavedHistoryDaysForDaysView > iNbDaysLongHistory:
            dtGrab = datetime.fromtimestamp(getConfigItem("next_history_grab_date", datetime(2000, 1, 1)))
            self.myStatus("Prochaine récupération complète de l'historique : " + datetimeToSQLDateString(dtGrab))

    # Calculate next complete grab, for tomorrow between 8 and 9 am if tomorrow is true, for next hour otherwise, prevent connection between 10 pm and 8 am
    def setNextConnection(self, bTomorrow):
        """
        Sets the next redis.

        Args:
            self: (todo): write your description
            bTomorrow: (todo): write your description
        """
        bForceTomorrow = False
        dtNow = datetime.now()
        if not bTomorrow:
            self.dateNextConnection = dtNow + timedelta(hours=1)
            if self.dateNextConnection.hour >= 22:
                bForceTomorrow = True
        if bTomorrow or bForceTomorrow:
            self.dateNextConnection = dtNow.replace(hour=8, minute=0)
            self.dateNextConnection = self.dateNextConnection + timedelta(days=1)
            iMinutesRand = round(dtNow.microsecond / 10000) % 60
            self.dateNextConnection = self.dateNextConnection + timedelta(minutes=iMinutesRand)
            if bForceTomorrow:
                self.myError("Serveurs inaccessibles à cette heure, prochaine connexion : " + datetimeToSQLDateTimeString(self.dateNextConnection))
        # Randomize minutes to lower load on Enedis website
        # randint makes domoticz crash on RPI
        # self.dateNextConnection = self.dateNextConnection + timedelta(minutes=randint(0, 59), seconds=randint(0, 59))
        # We take microseconds to randomize
        return bTomorrow or bForceTomorrow

    # Calculate next connection after a few seconds, prevent connection between 10 pm and 8 am
    def setNextConnectionForLater(self, iInterval):
        """
        Sets the next connection to the inputted value.

        Args:
            self: (todo): write your description
            iInterval: (int): write your description
        """
        bTomorrow = False
        dtNow = datetime.now()
        self.dateNextConnection = dtNow + timedelta(seconds=iInterval)
        if self.dateNextConnection.hour >= 22: 
            self.dateNextConnection = dtNow.replace(hour=8, minute=0)
            self.dateNextConnection = self.dateNextConnection + timedelta(days=1)
            bTomorrow = True
        elif self.dateNextConnection.hour < 8: 
            self.dateNextConnection = dtNow.replace(hour=8, minute=0)
            bTomorrow = True
        if bTomorrow:
            minutesRand = round(dtNow.microsecond / 10000) % 60
            self.dateNextConnection = self.dateNextConnection + timedelta(minutes=minutesRand)
            self.sConnectionStep = "idle"
            self.myError("Serveurs inaccessibles à cette heure, prochaine connexion : " + datetimeToSQLDateTimeString(self.dateNextConnection))
        return bTomorrow

    def clearData(self):
        """
        Clears the data

        Args:
            self: (todo): write your description
        """
        self.iUsagePointIndex = 0
        self.dData = dict()
        self.dCalculate = dict()
        self.bHasAFail = False
        self.bGlobalHasAFail = False
        self.bRefreshToken = False

    def disablePlugin(self):
        """
        Disables the usb devices.

        Args:
            self: (todo): write your description
        """
        self.isEnabled = False
        resetTokens()
        for oDevice in Devices.values():
            oDevice.Update(nValue=oDevice.nValue, sValue=oDevice.sValue, TimedOut=1)
        self.showSimpleStepError(
            "Le plugin va être arrêté. Relancez le en vous rendant dans Configuration/Matériel, en cliquant sur le plugin puis sur Modifier. Surveillez les logs pour obtenir le lien afin de renouveler le consentement pour la récupération des données auprès d'Enedis")

    # Handle the connection state machine
    def handleConnection(self, Data=None):
        """
        Called when a connection is received.

        Args:
            self: (todo): write your description
            Data: (todo): write your description
        """
        self.myDebug("Etape " + self.sConnectionStep)

        # First and last step
        if self.sConnectionStep == "idle":
            self.setHistoryDays()
            # Reset data
            self.clearData()
            self.resetDates(datetime(self.dateNextConnection.year, self.dateNextConnection.month, self.dateNextConnection.day) - timedelta(days=1))

            # If we have access tokens, try do grab data, otherwise ask for tokens
            if getConfigItem("access_token", ""):
                # self.sConnectionStep = "getdatadays"
                # self.getData(self.lUsagePointIndex[self.iUsagePointIndex], API_ENDPOINT_DATA_DAILY_CONSUMPTION, self.dateBeginDays, self.dateEndDays)
                self.sConnectionStep = "start"
            else:
                self.sConnectionStep = "parsedevicecode"
                self.getDeviceCode()

        # We should never reach this
        elif (self.sConnectionStep == "connecting") or (self.sConnectionStep == "sending"):
            if (self.iTimeoutCount >= 3):
                self.sConnectionStep = "retry"
                self.setNextConnectionForLater(self.iInterval)
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
            else:
                self.sConnectionStep = "retry"
                self.setNextConnectionForLater(self.iInterval)

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
                self.showSimpleStepError("Trop d'échecs de communication, le plugin réessaiera plus tard")
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
                self.disablePlugin()

        # Ask data for hours
        elif self.sConnectionStep == "getdatahours":
            # Check if access token still valid
            iStatus = getStatus(Data)
            #self.dumpDictToLog(Data)
            sError, sErrorDescription, sErrorUri = getError(Data)
            if (sError.lower() == "invalid_token") and (not self.bRefreshToken):
                self.sConnectionStep = "parseaccesstoken"
                self.refreshToken()
            elif iStatus == 403:
                self.showSimpleStatusError(Data)
                self.disablePlugin()
            elif (iStatus == 404) or self.bProdMode and (iStatus == 400):
                #self.showStatusError(True, Data, True)
                if self.bFirstBatch:
                    if (self.bProdMode):
                        self.bNoProduction = True
                    else:
                        self.bNoConsumption = True
                    if self.bNoConsumption and self.bNoProduction:
                        #self.showStatusError(True, Data)
                        self.showStepError(True, "Pas de données disponibles, avez-vous associé un compteur à votre compte et demandé l'enregistrement et la collecte des données horaire sur le site d'Enedis (dans \"Gérer l'accès à mes données\") ?")
                        self.bHasAFail = True
                self.sConnectionStep = "prod"
            # If status 429 or 500, retry later
            elif (iStatus == 429) or (iStatus == 500):
                self.sConnectionStep = "retry"
                self.setNextConnectionForLater(self.iInterval)
            elif iStatus != 200:
                self.showStatusError(True, Data)
                self.sConnectionStep = "prod"
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
                    # No production peak available yet in Enedis API
                    if self.bProdMode:
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
            if sError.lower() == "invalid_token" and (not self.bRefreshToken):
                self.sConnectionStep = "parseaccesstoken"
                self.refreshToken()
            elif iStatus == 403:
                self.showSimpleStatusError(Data)
                self.disablePlugin()
            # No peak available, it happens, ignore error silently
            elif iStatus == 404:
                self.showStatusError(True, Data, True)
                self.sConnectionStep = "prod"
            # If status 429 or 500, retry later
            elif (iStatus == 429) or (iStatus == 500):
                self.sConnectionStep = "retry"
                self.setNextConnectionForLater(self.iInterval)
            elif (iStatus != 200):
                self.showStatusError(False, Data)
                self.sConnectionStep = "prod"
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
            self.sUsagePointId = self.lUsagePointIndex[self.iUsagePointIndex].upper().strip()
            self.myStatus("Traitement pour le point de livraison " + self.sUsagePointId)
            if self.bHasAFail:
                self.bGlobalHasAFail = True
                self.bHasAFail = False
            self.bProdMode = False
            self.bNoConsumption = False
            self.bNoProduction = False
            self.sConnectionStep = "next"

        # next consumption or production point
        if self.sConnectionStep == "next":
            self.resetDates()
            self.sConnectionStep = "getdatahours"
            self.getData(
                API_ENDPOINT_DATA_PRODUCTION_LOAD_CURVE if self.bProdMode else API_ENDPOINT_DATA_CONSUMPTION_LOAD_CURVE,
                self.dateBeginHours, self.dateEndHours)

        # Next connection time depends on success
        if self.sConnectionStep == "done":
            if self.bHasAFail:
                self.bGlobalHasAFail = True
            if self.bGlobalHasAFail:
                self.setNextConnection(False)
            self.savePreviousSuccessfulConnectionDate(self.bGlobalHasAFail)
            self.clearData()
            self.sConnectionStep = "idle"
            self.myStatus("Prochaine connexion : " + datetimeToSQLDateTimeString(self.dateNextConnection))

    def dumpDictToLog(self, dictToLog):
        """
        Dump a dictionary to a dictionary.

        Args:
            self: (todo): write your description
            dictToLog: (dict): write your description
        """
        if self.iDebugLevel:
            if isinstance(dictToLog, dict):
                self.myDebug("Dict details (" + str(len(dictToLog)) + "):")
                for x in dictToLog:
                    if isinstance(dictToLog[x], dict):
                        self.myDebug("--->'" + str(x) + " (" + str(len(dictToLog[x])) + "):")
                        for y in dictToLog[x]:
                            if isinstance(dictToLog[x][y], dict):
                                for z in dictToLog[x][y]:
                                    self.myDebug("----------->'" + str(z) + "':'" + str(dictToLog[x][y][z]) + "'")
                            else:
                                self.myDebug("------->'" + str(y) + "':'" + str(dictToLog[x][y]) + "'")
                    else:
                        self.myDebug("--->'" + str(x) + "':'" + str(dictToLog[x]) + "'")
            else:
                self.myDebug("Received no dict: " + str(dictToLog))

    def onStart(self):
        """
        Initialize the device.

        Args:
            self: (todo): write your description
        """
        try:
            self.iDebugLevel = int(Parameters["Mode3"])
        except ValueError:
            self.iDebugLevel = 0
            
        if self.iDebugLevel > 0:
            self.fDebug = tempfile.NamedTemporaryFile(mode='w+t', delete=False, prefix="DomoticzLinky" + datetime.now().strftime("_%Y_%m_%d_%H_%M_%S_"), suffix=".log")

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

        self.myDebug("onStart called")

        self.iAlternateDevice = 1
        matchVersions = re.search(r"(\d+)\.(\d+)", Parameters["DomoticzVersion"])
        if (matchVersions):
            iVersionMaj = int(matchVersions.group(1))
            iVersionMin = int(matchVersions.group(2))
            iVersion = (iVersionMaj * 1000000) + iVersionMin
            if iVersion >= 4011774:
                self.iAlternateDevice = 0

        # For test purpose
        # self.iAlternateDevice = 1

        if self.iAlternateDevice:
            self.myLog(
                "Ce plugin est compatible avec Domoticz version 4.11070 mais la visualisation d'énergie produite et de tarification horaire ne peuvent fonctionner qu'à partir de la version 4.11774")

        if iVersion < 4011070:
            self.myError(
                "Votre version de Domoticz est trop ancienne")
            self.isEnabled = False
            return

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

        # History for short log is 7 days max (default to 7)
        try:
            self.iHistoryDaysForHoursView = int(self.iHistoryDaysForHoursView)
        except:
            self.iHistoryDaysForHoursView = 7
        if self.iHistoryDaysForHoursView < 0:
            self.iHistoryDaysForHoursView = 0
        elif self.iHistoryDaysForHoursView > 7:
            self.iHistoryDaysForHoursView = 7

        # History for short log is 730 days max (default to 7)
        try:
            self.iHistoryDaysForDaysView = int(self.iHistoryDaysForDaysView)
        except:
            self.iHistoryDaysForDaysView = 7
        if self.iHistoryDaysForDaysView < 1:
            self.iHistoryDaysForDaysView = 1
        elif self.iHistoryDaysForDaysView > 730:
            self.iHistoryDaysForDaysView = 730

        if self.sConsumptionType1.endswith("_cweek") and (self.iHistoryDaysForDaysView < 7):
            self.iHistoryDaysForDaysView = 7
        elif self.sConsumptionType1.endswith("_lweek")  and (self.iHistoryDaysForDaysView < 14):
            self.iHistoryDaysForDaysView = 14
        elif self.sConsumptionType1.endswith("_cmonth") and (self.iHistoryDaysForDaysView < 32):
            self.iHistoryDaysForDaysView = 32
        elif self.sConsumptionType1.endswith("_lmonth") and (self.iHistoryDaysForDaysView < 63):
            self.iHistoryDaysForDaysView = 63
        elif self.sConsumptionType1.endswith("_year") and (self.iHistoryDaysForDaysView < 366):
            self.iHistoryDaysForDaysView = 366

        self.iHistoryDaysForPeakDaysView = 1
        if self.sConsumptionType2.endswith("_cweek"):
            self.iHistoryDaysForPeakDaysView = 7
        elif self.sConsumptionType2.endswith("_lweek"):
            self.iHistoryDaysForPeakDaysView = 14
        elif self.sConsumptionType2.endswith("_cmonth"):
            self.iHistoryDaysForPeakDaysView = 32
        elif self.sConsumptionType2.endswith("_lmonth"):
            self.iHistoryDaysForPeakDaysView = 63
        elif self.sConsumptionType2.endswith("_year"):
            self.iHistoryDaysForPeakDaysView = 366

        if self.sTarif:
            self.myLog("Heures creuses mises à " + self.sTarif)
        else:
            self.myLog("Heures creuses désactivées")
        self.myLog(
            "Consommation à montrer sur le tableau de bord mis à " + self.sConsumptionType1 + " / " + self.sConsumptionType2)
        self.myLog("Nombre de jours à récupérer pour la vue par heures mis à " + str(self.iHistoryDaysForHoursView))
        self.myLog("Nombre de jours à récupérer pour les autres vues mis à " + str(self.iHistoryDaysForDaysView))
        self.myLog(
            "Nombre de jours à récupérer pour le calcul du pic mis à " + str(self.iHistoryDaysForPeakDaysView))
        self.myLog("Debug mis à " + str(self.iDebugLevel))
        if self.fDebug:
            self.myStatus("Log dans le fichier " + self.fDebug.name + " pour la version " + str(Parameters["Version"]) + " du plugin")

        # Parameter for tarif 1/2
        self.parseHcParameter(self.sTarif)

        # most init
        self.__init__()

        self.myLog(
            "Si vous ne voyez pas assez de données dans la vue par heures, augmentez le paramètre Log des capteurs qui se trouve dans Réglages / Paramètres / Historique des logs")

        iPreviousHistoryDaysForDaysView = getConfigItem("history_days", 0)
        if self.iHistoryDaysForDaysView != iPreviousHistoryDaysForDaysView:
            self.bHistoryDaysForDaysViewChanged = True
            setConfigItem("history_days", self.iHistoryDaysForDaysView)
        else:
            self.bHistoryDaysForDaysViewChanged = False
        self.iSavedHistoryDaysForDaysView = self.iHistoryDaysForDaysView

        # For test purpose
        #setConfigItem("next_history_grab_date", datetime(2020, 10, 26, 7, 34, 12))

        dtNow = datetime.now()
        self.dtNextRefresh = setRefreshTime(dtNow)
        self.dtGlobalTimeout = setTimeout(dtNow)
        self.setNextConnectionForLater(0)

        # Now we can enabling the plugin
        self.isStarted = True

    def onStop(self):
        """
        Called when the handler.

        Args:
            self: (todo): write your description
        """
        Domoticz.Debug("onStop called")
        # prevent error messages during disabling plugin
        self.isStarted = False
        if self.fDebug:
            self.fDebug.flush()

    def onConnect(self, Connection, Status, Description):
        """
        Called when the connection is established.

        Args:
            self: (todo): write your description
            Connection: (todo): write your description
            Status: (str): write your description
            Description: (str): write your description
        """
        Domoticz.Debug("onConnect called")
        if self.isStarted and ((Connection == self.httpLoginConn) or (Connection == self.httpDataConn)):
            if self.sBuffer:
                self.iTimeoutCount = 0
                self.sConnectionStep = "sending"
                Connection.Send(self.sBuffer)
                self.sBuffer = None
            else:
                self.myDebug("Nothing to send")
                self.sConnectionStep = "nothingtosend"
                self.handleConnection()

    def onMessage(self, Connection, Data):
        """
        Called when a message is received.

        Args:
            self: (todo): write your description
            Connection: (todo): write your description
            Data: (array): write your description
        """
        Domoticz.Debug("onMessage called")

        # if started and not stopping
        if self.isStarted and ((Connection == self.httpLoginConn) or (Connection == self.httpDataConn)) and (self.sConnectionStep == "sending"):
            self.sConnectionStep = self.sConnectionNextStep
            self.handleConnection(Data)

    def onDisconnect(self, Connection):
        """
        Called when the connection has been established.

        Args:
            self: (todo): write your description
            Connection: (todo): write your description
        """
        Domoticz.Debug("onDisconnect called")

    def onHeartbeat(self):
        """
        Called when a device has been received.

        Args:
            self: (todo): write your description
        """
        Domoticz.Debug("onHeartbeat() called")

        if self.fDebug:
            self.fDebug.flush()

        if self.isEnabled:
            dtNow = datetime.now()

            if dtNow > self.dtNextRefresh:
                self.dtNextRefresh = setRefreshTime(dtNow)
                if dtNow > self.dtGlobalTimeout:
                    bHasGlobalTimeout = True
                else:
                    bHasGlobalTimeout = False
                    
                for oDevice in Devices.values():
                    bHasLocalTimeout = False
                    if oDevice.DeviceID in self.dUsagePointTimeout:
                        #self.myLog(str(bHasGlobalTimeout) + " " + str(bHasLocalTimeout) + " " + str(self.dUsagePointTimeout[oDevice.DeviceID]) + " " + str(self.dtGlobalTimeout) + " " + str(self.dtNextRefresh))
                        if dtNow > self.dUsagePointTimeout[oDevice.DeviceID]:
                            bHasLocalTimeout = True
                    # Update the device at a regular basis to prevent usage to be shown at 0
                    if bHasGlobalTimeout or bHasLocalTimeout:
                        oDevice.Update(nValue=oDevice.nValue, sValue=oDevice.sValue, TimedOut=1)
                    else:
                        oDevice.Touch()

            if dtNow > self.dateNextConnection:
                # We immediatly program next connection for tomorrow, if there is a problem, we will reprogram it sooner
                self.setNextConnection(True)
                self.handleConnection()
            elif (self.sConnectionStep == "connecting") or (self.sConnectionStep == "sending"):
                self.handleConnection()


global _plugin
_plugin = BasePlugin()


def onStart():
    """
    Called when the plugin.

    Args:
    """
    global _plugin
    _plugin.onStart()


def onStop():
    """
    Called when plugin is closed

    Args:
    """
    global _plugin
    _plugin.onStop()


def onConnect(Connection, Status, Description):
    """
    Called when the connection is closed.

    Args:
        Connection: (todo): write your description
        Status: (str): write your description
        Description: (str): write your description
    """
    global _plugin
    _plugin.onConnect(Connection, Status, Description)


def onMessage(Connection, Data):
    """
    The callback.

    Args:
        Connection: (todo): write your description
        Data: (array): write your description
    """
    global _plugin
    _plugin.onMessage(Connection, Data)


def onCommand(Unit, Command, Level, Hue):
    """
    Called when the command.

    Args:
        Unit: (str): write your description
        Command: (str): write your description
        Level: (int): write your description
        Hue: (todo): write your description
    """
    global _plugin
    _plugin.onCommand(Unit, Command, Level, Hue)


def onDeviceAdded(Unit):
    """
    OnDevice on the given unit.

    Args:
        Unit: (str): write your description
    """
    global _plugin


def onDeviceModified(Unit):
    """
    Sets function toDevice.

    Args:
        Unit: (str): write your description
    """
    global _plugin


def onDeviceRemoved(Unit):
    """
    Sets the device to the given unit.

    Args:
        Unit: (str): write your description
    """
    global _plugin


def onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile):
    """
    Called when a notification is received.

    Args:
        Name: (str): write your description
        Subject: (todo): write your description
        Text: (str): write your description
        Status: (str): write your description
        Priority: (int): write your description
        Sound: (str): write your description
        ImageFile: (str): write your description
    """
    global _plugin
    _plugin.onNotification(Name, Subject, Text, Status, Priority, Sound, ImageFile)


def onDisconnect(Connection):
    """
    Initialize connection.

    Args:
        Connection: (todo): write your description
    """
    global _plugin
    _plugin.onDisconnect(Connection)


def onHeartbeat():
    """
    Called when the global callback.

    Args:
    """
    global _plugin
    _plugin.onHeartbeat()


# Generic helper functions
def setTimeout(dtDate=None):
    """
    Returns a datetime to the current day.

    Args:
        dtDate: (todo): write your description
    """
    if dtDate is None:
        dtDate = datetime.now()
    return dtDate + timedelta(days=1, hours=12)


def setRefreshTime(dtDate=None):
    """
    Sets the current date to the current instance.

    Args:
        dtDate: (todo): write your description
    """
#    return dtDate + timedelta(minutes=10)
    if dtDate is None:
        dtDate = datetime.now()
    return dtDate + timedelta(seconds=50)

# Get config item from Domoticz DB, convert DateTime to timestamp to circumvent a Domoticz bug
def getConfigItem(Key=None, Default={}):
    """
    Returns a configuration item from the item

    Args:
        Key: (str): write your description
        Default: (todo): write your description
    """
    Value = Default
    try:
        Config = Domoticz.Configuration()
        if (Key != None):
            Value = Config[Key]  # only return requested key if there was one
        else:
            Value = Config  # return the whole configuration if no key
    except KeyError:
        try:
            Value = Default.timestamp()
        except:
            Value = Default
    except Exception as inst:
        self.myError("Domoticz.Configuration read failed: '" + str(inst) + "'")
    return Value


# Set config item from Domoticz DB, convert DateTime to timestamp to circumvent a Domoticz bug
def setConfigItem(Key=None, Value=None):
    """
    Sets a configuration item.

    Args:
        Key: (str): write your description
        Value: (todo): write your description
    """
    Config = {}
    try:
        Config = Domoticz.Configuration()
        try:
            Value = Value.timestamp()
        except:
            pass
        if (Key != None):
            Config[Key] = Value
        else:
            Config = Value  # set whole configuration if no key specified
        Config = Domoticz.Configuration(Config)
    except Exception as inst:
        self.myError("Domoticz.Configuration operation failed: '" + str(inst) + "'")
    return Config


# Erase authorization tokens
def resetTokens():
    """
    Reset the currently running item.

    Args:
    """
    setConfigItem("usage_points_id", [])
    setConfigItem("token_type", "")
    setConfigItem("refresh_token", "")
    setConfigItem("access_token", "")


def initData(dDate):
    """
    Initialize data.

    Args:
        dDate: (todo): write your description
    """
    return {"consumption1": 0, "consumption2": 0, "production1": 0, "production2": 0, "consumption1_hours": {}, "consumption2_hours": {}, "production1_hours": {}, "production2_hours": {}, "consumptionpeak": 0, "productionpeak": 0, "data": False, "peak": False, "date": dDate}


def dictToQuotedString(dParams):
    """
    Convert a dictionary of dict.

    Args:
        dParams: (dict): write your description
    """
    result = ""
    for sKey, sValue in dParams.items():
        if result:
            result += "&"
        result += sKey + "=" + quote(str(sValue))
    return result


# Grab error inside received JSON
def getError(Data):
    """
    Parses a data dictionary

    Args:
        Data: (str): write your description
    """
    sError = ""
    sErrorDescription = ""
    sErrorUri = ""
    if Data and ("Data" in Data):
        try:
            dJson = json.loads(Data["Data"].decode())
        except ValueError:
            pass
        else:
            if dJson:
                if "error" in dJson:
                    sError = str(dJson["error"])
                if "error_description" in dJson:
                    sErrorDescription = str(dJson["error_description"])
                if "error_uri" in dJson:
                    sErrorUri = str(dJson["error_uri"])
    if not sError:
        if Data and ("Headers" in Data) and ("WWW-Authenticate" in Data["Headers"]):
            sAuthenticate = Data["Headers"]["WWW-Authenticate"]
            if "," in sAuthenticate:
                dError = dict(item.split("=", 1) for item in sAuthenticate.split(","))
                if "error" in dError:
                    sError = str(dError["error"]).strip("\"")
                if "error_description" in dError:
                    sErrorDescription = str(dError["error_description"]).strip("\"")
                if "error_uri" in dError:
                    sErrorUri = str(dError["error_uri"].strip("\""))
    return sError, sErrorDescription, sErrorUri


# Grab status inside received JSON
def getStatus(Data):
    """
    Returns the status of rows.

    Args:
        Data: (todo): write your description
    """
    if Data and "Status" in Data:
        try:
            return int(Data["Status"])
        except ValueError:
            return 504
    else:
        return 504


# Convert Enedis datetime string to datetime object
def enedisDateTimeToDatetime(datetimeStr):
    """
    Convert a datetime object to a datetime object.

    Args:
        datetimeStr: (todo): write your description
    """
    # Buggy
    # return datetime.strptime(datetimeStr, "%d/%m/%Y")
    # Not buggy ?
    return datetime(*(strptime(datetimeStr[:19], "%Y-%m-%d %H:%M:%S")[0:6]))


# Convert Enedis date string to datetime object
def enedisDateToDatetime(datetimeStr):
    """
    Convert datetime to a datetime.

    Args:
        datetimeStr: (todo): write your description
    """
    # Buggy
    # return datetime.strptime(datetimeStr, "%d/%m/%Y")
    # Not buggy ?
    return datetime(*(strptime(datetimeStr[:10], "%Y-%m-%d")[0:6]))


# Convert datetime object to Enedis date string
def datetimeToEnedisDateString(datetimeObj):
    """
    Convert datetime object from the string representation.

    Args:
        datetimeObj: (todo): write your description
    """
    return datetimeObj.strftime("%Y-%m-%d")


# Convert datetime object to Domoticz date string
def datetimeToSQLDateString(datetimeObj):
    """
    Returns a datetime object to a datetime object.

    Args:
        datetimeObj: (todo): write your description
    """
    return datetimeObj.strftime("%Y-%m-%d")


# Convert datetime object to Domoticz date and time string
def datetimeToSQLDateTimeString(datetimeObj):
    """
    Returns a datetime.

    Args:
        datetimeObj: (todo): write your description
    """
    return datetimeObj.strftime("%Y-%m-%d %H:%M:%S")


# The JoursFeries class code after that comes from https://github.com/etalab/jours-feries-france and here is its original license:

#MIT License

#Copyright (c) 2020 Etalab

#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

class JoursFeries(object):
    ZONES = [
        "Métropole",
        "Alsace-Moselle",
        "Guadeloupe",
        "Guyane",
        "Martinique",
        "Mayotte",
        "Nouvelle-Calédonie",
        "La Réunion",
        "Polynésie Française",
        "Saint-Barthélémy",
        "Saint-Martin",
        "Wallis-et-Futuna",
        "Saint-Pierre-et-Miquelon",
    ]

    def __init__(self):
        """
        Initialize the jours.

        Args:
            self: (todo): write your description
        """
        super(JoursFeries, self).__init__()

    @staticmethod
    def check_zone(zone):
        """
        Check if the zone exists

        Args:
            zone: (str): write your description
        """
        zone = zone or "Métropole"

        if zone not in JoursFeries.ZONES:
            valid_values = ", ".join(JoursFeries.ZONES)
            raise ValueError(
                "%s is invalid. Supported values: %s" % (zone, valid_values)
            )

        return zone

    @staticmethod
    def is_bank_holiday(date, zone=None):
        """
        Returns true if the given date is in the given bytestring is in the given date.

        Args:
            date: (todo): write your description
            zone: (str): write your description
        """
        return date in JoursFeries.for_year(date.year, zone).values()

    @staticmethod
    def next_bank_holiday(date, zone=None):
        """
        Returns the next day in the given date.

        Args:
            date: (todo): write your description
            zone: (str): write your description
        """
        while not JoursFeries.is_bank_holiday(date, zone):
            date = date + timedelta(days=1)

        return [
            (k, v)
            for k, v in JoursFeries.for_year(date.year, zone).items()
            if v == date
        ][0]

    @staticmethod
    def for_year(year, zone=None):
        """
        Return the year for each year.

        Args:
            year: (int): write your description
            zone: (str): write your description
        """
        JoursFeries.check_zone(zone)

        bank_holidays = {
            "1er janvier": JoursFeries.premier_janvier(year),
            "1er mai": JoursFeries.premier_mai(year),
            "8 mai": JoursFeries.huit_mai(year),
            "14 juillet": JoursFeries.quatorze_juillet(year),
            "Assomption": JoursFeries.assomption(year),
            "Toussaint": JoursFeries.toussaint(year),
            "11 novembre": JoursFeries.onze_novembre(year),
            "Jour de Noël": JoursFeries.jour_noel(year),
            "Lundi de Pâques": JoursFeries.lundi_paques(year),
            "Ascension": JoursFeries.ascension(year),
            "Lundi de Pentecôte": JoursFeries.lundi_pentecote(year),
            "Vendredi saint": JoursFeries.vendredi_saint(year, zone),
            "2ème jour de Noël": JoursFeries.deuxieme_jour_noel(year, zone),
            "Abolition de l'esclavage": JoursFeries.abolition_esclavage(year, zone),
        }

        bank_holidays = {k: v for k, v in bank_holidays.items() if v}

        return {
            k: v for k, v in sorted(bank_holidays.items(), key=lambda item: item[1])
        }

    @staticmethod
    def paques(year):
        """
        Paques date.

        Args:
            year: (todo): write your description
        """
        if year < 1886:
            return None
        a = year % 19
        b = year // 100
        c = year % 100
        d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1
        return date(year, month, day)

    @staticmethod
    def lundi_paques(year):
        """
        Return a year.

        Args:
            year: (todo): write your description
        """
        if year >= 1886:
            return JoursFeries.paques(year) + timedelta(days=1)
        return None

    @staticmethod
    def vendredi_saint(year, zone):
        """
        Vendredi zone.

        Args:
            year: (todo): write your description
            zone: (str): write your description
        """
        if zone == JoursFeries.check_zone("Alsace-Moselle"):
            return JoursFeries.paques(year) - timedelta(days=2)
        return None

    @staticmethod
    def ascension(year):
        """
        Return the year of the year.

        Args:
            year: (todo): write your description
        """
        if year >= 1802:
            return JoursFeries.paques(year) + timedelta(days=39)
        return None

    @staticmethod
    def lundi_pentecote(year):
        """
        Returns the year.

        Args:
            year: (todo): write your description
        """
        if year >= 1886:
            return JoursFeries.paques(year) + timedelta(days=50)
        return None

    @staticmethod
    def premier_janvier(year):
        """
        Return a year.

        Args:
            year: (todo): write your description
        """
        if year > 1810:
            return date(year, 1, 1)
        return None

    @staticmethod
    def premier_mai(year):
        """
        Return the date object for the year.

        Args:
            year: (todo): write your description
        """
        if year > 1919:
            return date(year, 5, 1)
        return None

    @staticmethod
    def huit_mai(year):
        """
        Return the year of the year.

        Args:
            year: (str): write your description
        """
        if (1953 <= year <= 1959) or year > 1981:
            return date(year, 5, 8)
        return None

    @staticmethod
    def quatorze_juillet(year):
        """
        Return the number of the year

        Args:
            year: (todo): write your description
        """
        if year >= 1880:
            return date(year, 7, 14)
        return None

    @staticmethod
    def toussaint(year):
        """
        Return a year of the given year.

        Args:
            year: (str): write your description
        """
        if year >= 1802:
            return date(year, 11, 1)
        return None

    @staticmethod
    def assomption(year):
        """
        Assomposes a year.

        Args:
            year: (todo): write your description
        """
        if year >= 1802:
            return date(year, 8, 15)
        return None

    @staticmethod
    def onze_novembre(year):
        """
        Return the number of months.

        Args:
            year: (int): write your description
        """
        if year >= 1918:
            return date(year, 11, 11)
        return None

    @staticmethod
    def jour_noel(year):
        """
        Return the number of months.

        Args:
            year: (todo): write your description
        """
        if year >= 1802:
            return date(year, 12, 25)
        return None

    @staticmethod
    def deuxieme_jour_noel(year, zone):
        """
        Deuxiemieme date object.

        Args:
            year: (todo): write your description
            zone: (str): write your description
        """
        if zone == JoursFeries.check_zone("Alsace-Moselle"):
            return date(year, 12, 26)
        return None

    @staticmethod
    def abolition_esclavage(year, zone):
        """
        Determine date for the given year.

        Args:
            year: (int): write your description
            zone: (todo): write your description
        """
        if zone == JoursFeries.check_zone("Mayotte"):
            return date(year, 4, 27)

        if zone == JoursFeries.check_zone("Martinique"):
            return date(year, 5, 22)

        if zone == JoursFeries.check_zone("Guadeloupe"):
            return date(year, 5, 27)

        if zone == JoursFeries.check_zone("Saint-Martin"):
            if year >= 2018:
                return date(year, 5, 28)
            else:
                return date(year, 5, 27)

        if zone == JoursFeries.check_zone("Guyane"):
            return date(year, 6, 10)

        if zone == JoursFeries.check_zone("Saint-Barthélémy"):
            return date(year, 10, 9)

        if zone == JoursFeries.check_zone("La Réunion") and year >= 1981:
            return date(year, 12, 20)

        return None
