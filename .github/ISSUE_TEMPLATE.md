* Avant de poster un message ici, veuillez toujours vérifiez que vos données sont visibles sur le site d'Enedis, dans la vue par jours et dans la vue par heures. Si ça ne fonctionne pas avec le site d'Enedis, ça ne fonctionnera pas non plus avec le plugin. N'oubliez pas de demander la collecte des données par demi-heure, c'est un pré-requis pour que le plugin fonctionne, une fois la demande faite, il faut attendre le lendemain pour qu'elle soit effective.

* La version de Domoticz doit être 3.9517 ou plus récente, mais la vue par heures ne fonctionnera pas avec la release version 4.9700 (vous aurez besoin d'une version release ou beta plus récente si vous avez déjà installé la version 4.9700 pour que la vue par heures fonctionne). La version de Domoticz doit être 4.11774, 2020.14 ou plus récente pour pouvoir visualiser l'énergie produite et la différentiation jour / nuit.

* Pensez à donner les droits en lecture et exécution au plugin si vous êtes sous Linux, c'est expliqué dans le readme

* Si vous exécutez pour la première fois le plugin tard le soir, ou si vous redémarrez Domoticz tard, le plugin essaiera d'emblée de récupérer des données, mais n'y parviendra peut-être pas. Enedis ferme souvent l'accès aux données à partir de quelque chose comme 23h00. Vous aurez donc des messages d'erreur jusqu'à disponibilité des données. Ensuite, le plugin récupérera les données au matin puis toutes les 24 heures environ, donc les erreurs ne devraient pas persister.

* L'erreur "async read" se produit souvent à la première exécution du plugin et est liée à un bug de Domoticz. Cette erreur ne doit pas persister.

* Pour tout problème, veuillez activer le mode Debug en le mettant sur "Oui" ou "Avancé", et postez tous les messages qui concernent le plugin, y compris les lignes indiquant la version du plugin et les paramètres configurés

* Veuillez indiquer votre version de 
  * Domoticz
  * Système d'exploitation
  * Type d'ordinateur (PC/Raspberry Pi 3 B+/etc.)

----------------------------------------------------------------

* Before posting a message here, please always check that your data are visible on the Enedis website, in the days view and in the hours view. If it does not work with the Enedis website, it will not work with the plugin either. Don't forget to allow hours data collect, it's a prerequisite for the plugin to work, after allowing it, data may be available the day after only.

* Domoticz version must be at least 3.9517, but short log view (hours view) will fail on release version 4.9700 (you'll need a more recent release or beta version if you already installed the version 4.9700 to get short log view working). Domoticz version must be at least 4.11774 or 2020.1 to see energy production and day / night tariff differences.

* Consider giving the read and execute rights to the plugin if you are on Linux, it is explained in the readme

* If you are running the plugin for the first time late at night, or if you restart Domoticz late, the plugin will try to recover data immediately, but may not succeed. Enedis often closes data access starting something like 11pm. You will therefore have error messages until data availability. Then, the plugin will grab the data in the morning then every 24 hours or so, so errors should not persist.

* The "async read" error often occurs the first time the plugin is executed and is due to a Domoticz bug. This error should not persist.

* For any problem, please enable the Debug mode by putting it on "Oui" or "Avancé", and post all the messages concerning the plugin, including the lines indicating the
version of the plugin and the configured parameters

* Please indicate your version of
  * Domoticz
  * Operating system
  * Computer type (PC/Raspberry Pi 3 B+/etc.)
