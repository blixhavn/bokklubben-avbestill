# bokklubben-avbestill
Et pythonscript for å automatisk logge seg på bokklubben.no og avbestille neste hovedbok. Endre brukernavn og passord i `config_default.py`, eller lag en ny fil `config.py` for å overstyre.

Kan kjøres jevnlig med et CRON-script:

```0 0 * * * /usr/bin/python3 /home/user/repos/bokklubben-avbestill/cancelOrder.py``` 

Scriptet logger alle kjøringer i `trace.log`, både suksess og feilkjøringer.
