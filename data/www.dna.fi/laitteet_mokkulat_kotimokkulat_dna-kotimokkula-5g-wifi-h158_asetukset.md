# DNA Kotimokkula 5G WiFi H158

[ Ominaisuudet ](https://www.dna.fi/tuki/laitteet/mokkulat/kotimokkulat/dna-
kotimokkula-5g-wifi-h158/ominaisuudet) [ Käyttöönotto
](https://www.dna.fi/tuki/laitteet/mokkulat/kotimokkulat/dna-
kotimokkula-5g-wifi-h158/kayttoonotto) [ Asetukset
](https://www.dna.fi/tuki/laitteet/mokkulat/kotimokkulat/dna-
kotimokkula-5g-wifi-h158/asetukset) [ Päivitykset
](https://www.dna.fi/tuki/laitteet/mokkulat/kotimokkulat/dna-
kotimokkula-5g-wifi-h158/paivitykset) [ Vianmääritys
](https://www.dna.fi/tuki/laitteet/mokkulat/kotimokkulat/dna-
kotimokkula-5g-wifi-h158/vianmaaritys)

##  Asetukset

Asetussivulle kirjautuminen

Kun tietokone tai muu päätelaite on kytketty langallisesti tai langattomasti
mokkulaan, sen kaikkia asetuksia voidaan hallita nettiselaimella.
Suosittelemme käyttämään Google Chrome- ja Safari-selaimia.

  1. Avaa nettiselain ja kirjoita osoiteriville 192.168.1.1 tai dna.wifi/ ja paina **Enter**. 
  2. User Name on **admin** ja password on **1234**
  3. Paina **Log In** ja mokkulan asetussivut aukeavat 

Salasanan vaihto ja unohtunut salasana

Kaikilla DNA:n langattomilla modeemeilla on tehdasasetuksiltaan sama salasana,
1234. Salasanaa tarvitaan, jotta laitteen asetuksia voidaan muuttaa. Salasana
tulee vaihtaa tietoturvasyistä, jotta ulkopuoliset eivät voi hallinnoida
modeemia. Kun olet kirjautunut asetussivuille, saat vaihdettua salasanan
seuraavasti:

  1. Valitse etusivulta **Advanced**
  2. Valitse System -valikon alta **Modify Password**

Kirjoita nykyinen salasanasi **Current Password** -kenttään. Tämän jälkeen
kirjoita haluamasi uusi salasana **New Password** -kenttään sekä uudelleen
**Confirm Password** -kenttään. Lopuksi paina **Confirm**.

Jos olet unohtanut asettamasi salasanan, voit palauttaa laitteen
tehdasasetuksille painamalla mokkulan pohjasta löytyvää reset-painiketta
muutaman sekunnin ajan. Laite uudelleenkäynnistyy ja salasanaksi palautuu
oletussalasana **1234**.

Bandsteering / yhdistelmäverkon pois päältä kytkeminen

  1. Kirjaudu laitteen asetussivulle ja valitse **Wi-Fi Settings**. 
  2. Poista valinta kohdasta **5 GHz preferred**. 

Kytkettyäsi yhdistelmäverkon pois päältä, ylempi osio **Wi-Fi Basic Settings**
-sivun näkymästä hallinnoi 2,4 GHz WiFi-verkkoa ja alempi 5 GHz -verkkoa.

Modeemien merkkivalojen asettaminen pimeään tilaan

  1. Kirjaudu laitteen asetussivulle ja valitse **Advanced**
  2. Valitse System -valikon alta **System Settings**
  3. Aktivoi sivulta kohta **Indicator**
  4. Valitse ajanjakso jolloin haluat mokkulan valojen olevan pois päältä. Mikäli haluat kytkeä laitteen valot kokonaan pois, valitse ajanjaksoksi 00:00 – 23:59 
  5. Vahvista valinta valitsemalla lopuksi **Save**

Siltatilan asettaminen

  1. Kirjaudu laitteen asetussivulle ja valitse **Advanced**
  2. valitse **Router** -valikon alta **Bridge Mode**
  3. valitse **Enable bridge mode**
  4. valitse **Confirm**

Siltatilan voit poistaa käytöstä kirjautumalla asetussivuille ( **huom**.
siltatilassa pääset asetussivuille vain IP-osoitteella 192.168.1.1) ja
poistamalla valinnan **Enable bridge mode** -kohdasta tai tekemällä
tehdasasetusten palautuksen painamalla mokkulan pohjasta löytyvää reset-
painiketta muutaman sekunnin ajan.

Vierailijaverkon asettaminen

  1. Kirjaudu laitteen asetussivulle ja valitse **Wi-Fi Settings**
  2. valitse **Guest Wi-Fi** -valikon alta **Guest Wi-Fi**
  3. Syötä esiin tuleviin kenttiin tiedot seuraavasti 
    1. Määritä Duration -kohtaan vierasverkon voimassaoloaika 
    2. Määritä Wi-Fi name -kohtaan vierasverkon nimi 
    3. Määritä Security-kohtaan verkon suojaustaso (avoin/suojattu) 
  4. Valitse lopuksi **Save** vahvistaaksesi asetukset 

DynDNS

  1. Kirjaudu laitteen asetussivulle ja valitse **Advanced**
  2. Valitse **Router** -valikon alta **DDNS**
  3. Valitse + -merkki DDNS List -osion oikeasta reunasta 
  4. Täytä vaadittavat tiedot Add DDNS -ponnahdusikkunan kenttiin 
  5. Tallenna muutokset painamalla **Save**

DynDNS-palvelun käyttö edellyttää, että käyttäjä on luonut valmiiksi tilin
DynDNS-palveluntarjoajalle.

Porttiohjaus

Kirjaudu laitteen asetussivulle ja valitse **Advanced**. Siirry **Security**
-valikon kautta **port forwading** -välilehdelle.

Modeemissa on päällä oletuksena UnPn-työkalu portinohjaukseen. Esimerkiksi
pelattaessa tai käytettäessä latausohjelmia, käyttäjä voi avata portteja myös
manuaalisesti.

Manuaalisen ohjauksen tekeminen:

Valitse Virtual Servers List -osion oikeasta reunasta + -merkki ja lisää
tarvittavat tiedot. Lopuksi paina **Confirm** hyväksyäksesi muutokset.

Lapsilukko

Kirjaudu laitteen asetussivulle ja valitse Tools. Siirry Parental Control
-valikkoon.

Valitse Internet Access Time Control -osion reunasta + -merkki ja luo sääntö
lapsilukolle

  1. Määritä Time -kohtaan aikajakso jolloin lapsilukko on voimassa 
  2. Määritä Repeats-kohtaan viikonpäivät jolloin lapsilukko on voimassa 
  3. Valitse Enable on selected devices -kohdasta laitteet, joiden halutaan olevan lapsilukon alaisuudessa 
  4. Valitse lopuksi Confirm vahvistaaksesi asetukset

##  WiFi-asetusten muuttaminen

Mokkulan asetussivustolla voit helposti muuttaa langattoman verkon asetuksia.
Näitä ovat mm. langattoman verkon, eli WiFi-verkon, nimi, salasana sekä
suojausasetukset.

Kirjaudu laitteen asetussivulle ja valitse etusivulta **Wi-Fi Settings**.

[Katso WiFi-verkon nimen ja salasanan vaihtamisen
ohjevideo](https://youtu.be/9qHe1xDrTCs?si=bYQE-McLC_iiAqF6)

Yhdistelmäverkon asetusten muuttaminen

**WiFi Basic Settings** -valikon alta voit muuttaa yleisimpiä langattoman
verkon asetuksia. DNA Kotimokkula tukee 2,4 GHz ja 5 GHz –taajuuksisia
langattomia WiFi-verkkoja. Oletuksena laitteessa on päällä 5 GHz -verkko sekä
2,4 GHz ja 5 GHz yhdistelmäverkko, jolloin käyttölaitteesi valitsee mitä
taajuutta käyttää. Suosittelemme yhdistelmäverkon (DNA-WIFI-XXXX) käyttöä.

WiFi -verkon nimen muuttaminen

Yhdistelmäverkon nimi vaihdetaan kirjoittamalla uusi haluttu WiFi-verkon nimi
kohtaan **2.4/5 GHz Wi-Fi name** ja tallennettaan muutos valitsemalla Save
sivuston alaosasta. 5 GHz -verkon nimen voi vastaavasti vaihtaa kirjoittamalla
uusi haluttu verkon nimi kohtaan **5 GHz Wi-Fi name** ja tallentamalla muutos
valitsemalla **Save**.

WiFi-verkon salasanan vaihtaminen

WiFi-verkon salasana vaihdetaan kirjoittamalla haluttu WiFi-verkon salasana
kohtaan **Wi-Fi Password** ja tallennettaan muutos valitsemalla **Save**
sivuston alaosasta. Yhdistelmäverkon ja 5 GHz -verkon salasanat voi asettaa
erikseen, kunkin verkon **Wi-Fi Password** -kenttää muokkaamalla ja
valitsemalla **Save**.

##  Laitetiedot

Sarjanumeron tarkistus

Kirjaudu laitteen asetussivulle ja valitse **Advanced**. Siirry **System**
-valikon **Device Information** -välilehdelle. Sarjanumero näkyy kohdassa
**Serial number**. Löydät sarjanumeron myös laitteeseen liimatusta tarrasta.

Laitteen ohjelmistoversion tarkistus

Kirjaudu laitteen asetussivulle ja valitse **Advanced**. Siirry **System**
-valikon **Device Information** -välilehdelle. Laitteen ohjelmistoversio näkyy
kohdassa **Software version**.

## Mokkulan merkkivalot

LED | Toiminne | Kuvaus  
---|---|---  
5G | Palaa sinisenä: | Yhteys 5G-verkkoon hyvä  
Palaa keltaisena: | Yhteys 5G-verkkoon kohtalainen  
Palaa punaisena: | Yhteys 5G-verkkoon heikko  
Pois päältä: | Ei yhteydessä 5G-verkkoon  
4G | Palaa sinisenä: | Yhteys 4G-verkkoon hyvä  
Palaa keltaisena: | Yhteys 4G-verkkoon kohtalainen  
Palaa punaisena: | Yhteys 4G-verkkoon heikko  
Pois päältä: | Ei yhteydessä 4G-verkkoon  
STATUS | Palaa sinisenä: | Yhdistetty mobiiliverkkoon  
Vilkkuu sinisenä: | Etsii WPS-pariliitosta  
Palaa punaisena: | Ei yhteydessä mobiiliverkkoon  