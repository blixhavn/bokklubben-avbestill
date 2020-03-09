import requests
import sys
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.INFO)

try:
    from config import username, password
except (ImportError, ModuleNotFoundError):
    from config_default import username, password

log = logging.getLogger(__name__)
dt_fmt = "%Y-%m-%d %H:%M:%S"
fmt = '[%(asctime)s]: %(message)s'
log_format = logging.Formatter(fmt, dt_fmt)
f_handler = logging.FileHandler('trace.log')
f_handler.setFormatter(log_format)
log.addHandler(f_handler)

payload = f"login={username}&passord={password}&permanent=on&submit="
headers = {'Content-Type': "application/x-www-form-urlencoded"}
url = "https://www.bokklubben.no/login.do"

try:
    with requests.Session() as s:
        s.post(url, data=payload, headers=headers)
        try:
            medlemsnr = s.cookies['MedlNr']
        except KeyError:
            log.error("❌ Innlogging feilet")
            sys.exit()

        mainpage = s.get('https://www.bokklubben.no/medlem/hovedboker.do')
        main_soup = BeautifulSoup(mainpage.text, features="html.parser")

        try:
            book_link = main_soup.find(lambda elem: elem.name == 'a' and 'Les mer/avbestill' in elem.text)
            book_id = book_link['href'].split('=')[-1]

            s.get(f'https://www.bokklubben.no//medlem/hovedboker.do?avbestill={book_id}&saId=NB&meNr={medlemsnr}')
            log.info("✔️ Bok avbestilt")

        except TypeError as e:
            log.info("❌ Bok allerede avbestilt")
except Exception as e:
    log.error("Exception occurred", exc_info=True)