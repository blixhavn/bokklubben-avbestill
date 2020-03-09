# bokklubben-avbestill

Et pythonscript for å automatisk logge seg på bokklubben.no og avbestille neste hovedbok. Endre brukernavn og passord i `config_default.py`, eller lag en ny fil `config.py` for å overstyre.

### Installasjon

* Installer pythonpakkene i `requirements.txt` enten globalt (`sudo pip install -r requirements.txt`) eller i et [virtualenvironment](https://linuxhint.com/create_manage_python_virtual_environment/). 
* Kjør pythonscriptet

For å slippe å følge med, kan scriptet med fordel kjøres med Crontab (unix) eller Task Scheduler (Windows). Scriptet logger alle kjøringer i `trace.log`, både suksess og feilkjøringer.
