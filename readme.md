# Linky plugin for Domoticz

This is a plugin for [Domoticz](https://domoticz.com), to grab data from french smartgrid meter Linky. It grabs data from [Enedis](http://www.enedis.fr) user account and store them inside a counter device log.

## Prerequisites

Domoticz version must be at least 3.9517, and short log view may fail on version 4.9700.

You need to have a Linky meter, create a user account on [Enedis](http://www.enedis.fr), accept conditions on the website and check that you receive data on the website. In particular, check the hour view (Consommation/Suivre ma consommation/Par heure), Enedis might ask for your permission the first time to collect hours data, this plugin won't work if you didn't fulfill this step. Data might be not available the first weeks after Linky has be installed or enabled, be patient and check you get data on [Enedis](http://www.enedis.fr) website before blaming the plugin.

## Installing

Copy the plugin.py to domoticz directory/plugins/DomoticzLinky or change directory to domoticz directory/plugins and issue the following command:

```
git clone https://github.com/guillaumezin/DomoticzLinky
```

To update, overwrite plugin.py or change directory to domoticz directory/plugins/DomoticzLinky and issue the following command:
```
git pull
```

Give the execution permission, for Linux:
```
chmod ugo+x plugin.py
```

Restart Domoticz.

## Configuration

Add the Linky hardware in Domoticz hardware configuration tab, giving the user name (e-mail address) and password of your Enedis account. You can choose the number of days to collect data for the short log (day) and for the week/month/year log. Note that Domoticz will clean every day data in the short log, based on the Short Log Sensors value the in Setup/Settings/Log History, you can increase the value there to get up to 7 days of short log history.

After enabling the hardware, you shall have a new Linky Utility device and watch your energy consumption history with the Log button.

## Authors

* **Baptiste Candellier** - *Kindle Linky plugin* - [linkindle](https://github.com/outadoc/linkindle)
* **Asdepique777** - *Jeedom Linky plugin* - [jeedom_linky](https://github.com/Asdepique777/jeedom_linky)
* **epierre** - *Linky external script for Domoticz* - [domoticz_linky](https://github.com/empierre/domoticz_linky)
* **Guillaume Zin** - *Port to Domoticz plugin framework* - [DomoticzLinky](https://github.com/guillaumezin/DomoticzLinky)

See also the list of [contributors](https://github.com/guillaumezin/DomoticzLinky/contributors) who participated in this project.

## License

This project is licensed under the GPLv3 license - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Baptiste Candellier
* Asdepique777
* epierre
* Domoticz team
