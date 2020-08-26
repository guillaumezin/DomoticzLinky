*English below*

# Plugin Linky pour Domoticz

Ceci est un plugin pour [Domoticz](https://domoticz.com), récupérant les données Linky. Les données sont collectées du compte utilisateur [Enedis](http://www.enedis.fr) et stockées dans le log d'un dispositif compteur électrique.

## Prérequis

La version de Domoticz doit être 4.11070 ou plus récente. La version de Domoticz doit être 4.11774, 2020.14 ou plus récente pour pouvoir visualiser l'énergie produite et la différentiation jour / nuit.

Vous devez avoir un compteur Linky, créer un compte utilisateur sur [Enedis](http://www.enedis.fr), accepter les conditions d'utilisation et vérifier que vous visualisez bien les courbes sur le site. En particulier, vérifiez la vue par heures (allez sur "Suivre les mesures" et passez "affiché(e)s en" sur "heures"), Enedis peut vous demander la permission la première fois pour collecter et enregistrer les données par heure, ce plugin ne fonctionnera pas pleinement si vous n'avez pas passé cette étape. Vous pouvez activer la collecte et l'enregistrement des données par heure sur votre compte Enedis sur "Gérer l'accès à mes données" dans l'encart "Collecte de la consommation horaire" et dans l'encart "Enregistrement de la consommation horaire". Les données peuvent ne pas être disponibles après l'installation ou l'activation de Linky, soyez patient et vérifiez que vous recevez les données sur le site [Enedis](http://www.enedis.fr) avant de rejetter la faute sur le plugin.

## Installation

Copiez plugin.py dans le sous-répertoire plugins/DomoticzLinky de Domoticz ou placez vous dans le sous répertoire plugins de Domoticz and tapez la commande suivante :

```
git clone https://github.com/guillaumezin/DomoticzLinky
```

Pour mettre à jour, écrasez plugin.py ou placez vous dans le sous répertoire plugins de Domoticz et tapez la commande suivante :
```
git pull
```

Donnez la permission d'exécution si vous êtes sous Linux :
```
chmod ugo+x plugin.py
```

Redémarrez Domoticz.

## Configuration

A la première installation, commencez par vérifier dans les paramètres de Domoticz que "Accepter de nouveaux dispositifs matériels" est activé au moins temporairement (Configuration / Paramètres / Système / Matériel/dispositifs).

Ajoutez le matériel Linky dans l'onglet de configuration Configuration / Matériel.

Vous pouvez choisir les plages horaires d'heures creuses, sous la forme "2h00-7h00 13h00-16h00" par exemple, laisser vide pour désactiver. Vous pouvez préciser des plages différentes pour chaque point de livraison, par exemple "12345678901234 1h00-6h00 12h00-14h00 88888888888888 13h00-16h00" indique des plages horaires "1h00-6h00 12h00-14h00" pour le point de livraison "12345678901234" et la plage horaire "13h00-16h00" pour le point de livraison "88888888888888". Vous pouvez également précéder de plages horaires par défaut, par exemple "02h00-04h00 16h00-19h00 12345678901234 1h00-6h00 12h00-14h00 88888888888888 13h00-16h00" permet, par rapport à l'exemple précédent, de mettre les plages horaires "02h00-04h00 16h00-19h00" pour tous les points de livraison autres que "12345678901234" et "88888888888888". Enfin vous pouvez désactiver les heures creuses pour un point de livraison particulier, par exemple "02h00-04h00 16h00-19h00 12345678901234 88888888888888 13h00-16h00" permet de mettre les plages horaires "02h00-04h00 16h00-19h00" pour tous les points de livraison, de désactiver les heures creuses pour le point de livraison 12345678901234 et de mettre la plage horaire "13h00-16h00" pour le point de livraison "88888888888888".

Vous pouvez également choisir le nombre à afficher tableau de bord.

Vous pouvez choisir le nombre de jours à récupérer pour la vue par heures et pour les autres vues. Vous pouvez mettre le nombre de jours à récupérer à 0 pour désactiver la récupération de données pour la vue par heures. Notez que Domoticz effacera chaque jour une partie des données de la vue par heures en se basant sur le paramètre Log des capteurs qui se trouve dans Configuration / Paramètres / Historique des logs, vous pouvez augmenter ce paramètre pour voir jusqu'à 7 jours d'historique.

Commencez par surveiller votre Configuration / Log. Aux premières connexions, le plugin doit vous donner l'adresse Web https://opensrcdev.alwaysdata.net/domoticzlinkyconnect/device à consulter et un code à y copier/coller pour obtenir le consentement du partage de données d'Enedis vers le plugin. Si vous ne répondez pas dans les minutes qui suivent, le plugin est arrêté. Pour relancer le processus, rendez-vous dans Configuration / Matériel, cliquez sur le plugin et sur Modifier.

Après avoir activé le matériel et donné le consentement, vous devriez avoir un nouveau dispositif Linky dans l'onglet Mesures, et vous devriez pouvoir visualiser les courbes de consommation via le bouton Log de ce dispositif.

## Auteurs

* **Baptiste Candellier** - *Kindle Linky plugin* - [linkindle](https://github.com/outadoc/linkindle)
* **Asdepique777** - *Jeedom Linky plugin* - [jeedom_linky](https://github.com/Asdepique777/jeedom_linky)
* **epierre** - *Linky external script for Domoticz* - [domoticz_linky](https://github.com/empierre/domoticz_linky)
* **Guillaume Zin** - *Port to Domoticz plugin framework* - [DomoticzLinky](https://github.com/guillaumezin/DomoticzLinky)

See also the list of [contributors](https://github.com/guillaumezin/DomoticzLinky/contributors) who participated in this project.

## Licence

Ce projet est sous licence GPLv3 - cf. fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

* Frédéric Caillet - son site Internet : [RUSSANDOL](https://www.russandol.pro) - pour l'hébergement et la maintenance de l'infrastructure intermédiaire d'obtention du consentement oAuth et la prise en charge contractuelle avec Enedis
* Baptiste Candellier
* Asdepique777
* empierre
* Domoticz team

----------------------------------------------------------------

# Linky plugin for Domoticz

This is a plugin for [Domoticz](https://domoticz.com), to grab data from french smartgrid meter Linky. It grabs data from [Enedis](http://www.enedis.fr) user account and store them inside a counter device log.

## Prerequisites

Domoticz version must be at least 4.11070. Domoticz version must be at least 4.11774 or 2020.1 to see energy production and day / night tariff differences.

You need to have a Linky meter, create a user account on [Enedis](http://www.enedis.fr), accept conditions on the website and check that you receive data on the website. In particular, check the hour view (go to "Suivre les mesures" and switch "affiché(e)s en" to "heures"), Enedis might ask for your permission the first time to collect hours data, this plugin won't work if you didn't fulfill this step. You can activate the recording and collection of data per hour on your Enedis account on "Gérer l'accès à mes données" in "Enregistrement de la consommation horaire" area and in "Collecte de la consommation horaire" area. Data might be not available the first weeks after Linky has be installed or enabled, be patient and check you get data on [Enedis](http://www.enedis.fr) website before blaming the plugin.

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

On first install, check that "Accept new Hardware Devices" is enabled, at least temporaly (in Setup / Settings / System / Hardware/Devices).

Add the Linky hardware in Domoticz Setup / Hardware configuration tab.

You can choose the off-peak hours, in the form "2:00-7:00 13:00-16:00" for example, leave empty to disable. You can specify different ranges for each delivery point, for example "12345678901234 1:00-6:00 12:00-14:00 88888888888888 13:00-16:00" indicates time slots "1:00-6:00 12:00-14:00" for the delivery point "12345678901234" and the time slot "13:00-16:00" for the delivery point "88888888888888". You can also begin with default time slots, for example "2:00-04:00 16:00-19:00 12345678901234 1:00-6:00 12:00-14:00 88888888888888 13:00-16:00" allows, compared to the previous example, to put the time slots "02:00-04:00 16:00-19:00" for all delivery points other than "12345678901234" and "88888888888888". Finally you can disable the off-peak hours for a particular delivery point, for example "02:00-04:00 16:00-19:00 12345678901234 88888888888888 13:00-16:00" allows to set the time slots "02:00-04:00 16:00-19:00" for all the delivery points, to disable off-peak hours for the delivery point 12345678901234 and to set the time slot "13:00-16:00" for the delivery point "88888888888888".

You can choose the number you want to see on the dashboard.

You can choose the number of days to collect data for the short log (day) and for the week/month/year log. You can set the number of days to collect data for the short log (day) to 0 to disable data grabbing for this view. Note that Domoticz will clean every day data in the short log, based on the Short Log Sensors value the in Setup / Settings / Log History, you can increase the value there to get up to 7 days of short log history.

To start, go to Setup / Log. At first connections, the plugin shall give you the web address https://opensrcdev.alwaysdata.net/domoticzlinkyconnect/device to browse and a code to copy/paste to give Enedis authorizations to share your data with the plugin. If you don't answer quickly, the plugin will stop. To relaunch the process, go to Setup / Hardware, click on the plugin then on Update.

After enabling the hardware and give authorizations, you shall have a new Linky Utility device and watch your energy consumption history with the Log button.

## Authors

* **Baptiste Candellier** - *Kindle Linky plugin* - [linkindle](https://github.com/outadoc/linkindle)
* **Asdepique777** - *Jeedom Linky plugin* - [jeedom_linky](https://github.com/Asdepique777/jeedom_linky)
* **epierre** - *Linky external script for Domoticz* - [domoticz_linky](https://github.com/empierre/domoticz_linky)
* **Guillaume Zin** - *Port to Domoticz plugin framework* - [DomoticzLinky](https://github.com/guillaumezin/DomoticzLinky)

See also the list of [contributors](https://github.com/guillaumezin/DomoticzLinky/contributors) who participated in this project.

## License

This project is licensed under the GPLv3 license - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Frédéric Caillet - his web site: [RUSSANDOL](https://www.russandol.pro) - for the web hosting and maintenance of the oAuth consent middleware infrastructure and contracting with Enedis 
* Baptiste Candellier
* Asdepique777
* empierre
* Domoticz team
