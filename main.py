import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://www.cerkezkoytso.org.tr/firmarehberi.html"

def get_firmalar():
    session = requests.Session()
    response = session.get(BASE_URL)
    soup = BeautifulSoup(response.text, "html.parser")
    firmalar = []

    # Tablo içerisindeki firma verilerini çekiyoruz
    rows = soup.select("table tbody tr")
    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 4:
            firma_adi = cols[0].text.strip()
            adres = cols[1].text.strip()
            nace_kodu = cols[2].text.strip()
            is_konusu = cols[3].text.strip()
            firmalar.append({
                "Firma Adı": firma_adi,
                "Adres": adres,
                "NACE Kodu": nace_kodu,
                "İş Konusu": is_konusu,
                "Web Sitesi": "",
                "E-posta": "",
                "Telefon": "",
                "Instagram": "",
                "LinkedIn": "",
                "Video İçeriği": ""
            })
    return firmalar

def main():
    firmalar = get_firmalar()
    df = pd.DataFrame(firmalar)
    df.to_csv("cerkezkoy_firmalar.csv", index=False)
    print(f"{len(firmalar)} firma bilgisi kaydedildi.")

if __name__ == "__main__":
    main()