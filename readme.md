*English below*

# Plugin Linky pour Domoticz

Ceci est un plugin pour [Domoticz](https://domoticz.com), récupérant les données Linky. Les données sont collectées du compte utilisateur [Enedis](http://www.enedis.fr) et stockées dans le log d'un dispositif compteur électrique.


## Prérequis

La version de Domoticz doit être 3.9517 ou plus récente, mais la vue par heures ne fonctionnera pas avec la release version 4.9700 (vous aurez besoin d'une version release ou beta plus récente si vous avez déjà installé la version 4.9700 pour que la vue par heures fonctionne).

Vous devez avoir un compteur Linky, créer un compte utilisateur sur [Enedis](http://www.enedis.fr), accepter les conditions d'utilisation et vérifier que vous visualisez bien les courbes sur le site. En particulier, vérifiez la vue par heures (Consommation / Suivre ma consommation / Par heure), Enedis peut vous demander la permission la première fois pour collecter les données par heure, ce plugin ne fonctionnera pas pleinement si vous n'avez pas passé cette étape. Les données peuvent ne pas être disponibles après l'installation ou l'activation de Linky, soyez patient et vérifiez que vous recevez les données sur le site [Enedis](http://www.enedis.fr) avant de rejetter la faute sur le plugin.

## Installation

Copiez plugin.py dans le sous-répertoire plugins/DomoticzLinky de Domoticz ou placez vous dans le sous répertoire plugins de Domoticz and tapez la commande suivante :

```
git clone https://github.com/guillaumezin/DomoticzLinky
```

Pour mettre à jour, écrasez plugin.py placez vous dans le sous répertoire plugins de Domoticz and tapez la commande suivante :
```
git pull
```

Donnez la permission d'exécution si vous êtes sous Linux :
```
chmod ugo+x plugin.py
```

Redémarrez Domoticz.

## Configuration

A la première installation, commencez par vérifier dans les paramètres de Domoticz que "Accepter de nouveaux dispositifs matériels" est activé au moins temporairement (Réglages / Paramètres / Système / Matériel/dispositifs).

Ajoutez le matériel Linky dans l'onglet de configuration Réglages / Matériel, en mettant l'adresse e-mail et le mot de passe de votre compte Enedis. Vous pouvez choisir le nombre de jours à récupérer pour la vue par heures et pour les autres vues. Vous pouvez mettre le nombre de jours à récupérer à 0 pour désactiver la récupération de données pour la vue par heures. Notez que Domoticz effacera chaque jour une partie des données de la vue par heures en se basant sur le paramètre Log des capteurs qui se trouve dans Réglages / Paramètres / Historique des logs, vous pouvez augmenter ce paramètre pour voir jusqu'à 7 jours d'historique.

Après avoir activé le matériel, vous devriez avoir un nouveau dispositif Linky dans l'onglet Mesures, et vous devriez pouvoir visualiser les courbes de consommation via le bouton Log de ce dispositif.

A partir de la version 1.0.9, le plugin a une option permettant de choisir si vous voulez afficher sur le tableau de bord la consommation de la veille, de la semaine en cours, de la semaine dernière, du mois en cours, du mois dernier, ou de l'année.

## Auteurs

* **Baptiste Candellier** - *Kindle Linky plugin* - [linkindle](https://github.com/outadoc/linkindle)
* **Asdepique777** - *Jeedom Linky plugin* - [jeedom_linky](https://github.com/Asdepique777/jeedom_linky)
* **epierre** - *Linky external script for Domoticz* - [domoticz_linky](https://github.com/empierre/domoticz_linky)
* **Guillaume Zin** - *Port to Domoticz plugin framework* - [DomoticzLinky](https://github.com/guillaumezin/DomoticzLinky)

See also the list of [contributors](https://github.com/guillaumezin/DomoticzLinky/contributors) who participated in this project.

## Licence

Ce projet est sous licence GPLv3 - cf. fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

* Baptiste Candellier
* Asdepique777
* empierre
* Domoticz team

----------------------------------------------------------------

# Linky plugin for Domoticz

This is a plugin for [Domoticz](https://domoticz.com), to grab data from french smartgrid meter Linky. It grabs data from [Enedis](http://www.enedis.fr) user account and store them inside a counter device log.

## Prerequisites

Domoticz version must be at least 3.9517, but short log view (hours view) will fail on release version 4.9700 (you'll need a more recent release or beta version if you already installed the version 4.9700 to get short log view working).

You need to have a Linky meter, create a user account on [Enedis](http://www.enedis.fr), accept conditions on the website and check that you receive data on the website. In particular, check the hour view (Consommation / Suivre ma consommation / Par heure), Enedis might ask for your permission the first time to collect hours data, this plugin won't work if you didn't fulfill this step. Data might be not available the first weeks after Linky has be installed or enabled, be patient and check you get data on [Enedis](http://www.enedis.fr) website before blaming the plugin.

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

Add the Linky hardware in Domoticz Settings / Hardware configuration tab, giving the e-mail address and password of your Enedis account. You can choose the number of days to collect data for the short log (day) and for the week/month/year log. You can set the number of days to collect data for the short log (day) to 0 to disable data grabbing for this view. Note that Domoticz will clean every day data in the short log, based on the Short Log Sensors value the in Setup / Settings / Log History, you can increase the value there to get up to 7 days of short log history.

After enabling the hardware, you shall have a new Linky Utility device and watch your energy consumption history with the Log button.

Starting version 1.0.9, the plugin has an option to choose if you want to see on the dashboard the consumption of the day before, the current week, the previous week, the current month, the previous month, or the year.

## Authors

* **Baptiste Candellier** - *Kindle Linky plugin* - [linkindle](https://github.com/outadoc/linkindle)
* **Asdepique777** - *Jeedom Linky plugin* - [jeedom_linky](https://github.com/Asdepique777/jeedom_linky)
* **epierre** - *Linky external script for Domoticz* - [domoticz_linky](https://github.com/empierre/domoticz_linky)
* **Guillaume Zin** - *Port to Domoticz plugin framework* - [DomoticzLinky](https://github.com/guillaumezin/DomoticzLinky)

See also the list of [contributors](https://github.com/guillaumezin/DomoticzLinky/contributors) who participated in this project.

## License

This project is licensed under the GPLv3 license - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

* Baptiste Candellier
* Asdepique777
* empierre
* Domoticz team
