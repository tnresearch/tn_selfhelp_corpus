# DNA Mesh WiFi WA8021V5 -modeemi

# DNA Mesh WiFi WA8021V5 -modeemi

[ Ominaisuudet ](https://www.dna.fi/tuki/laitteet/modeemit/ethernet/dna-mesh-
wifi-wa8021v5/ominaisuudet) [ Käyttöönotto
](https://www.dna.fi/tuki/laitteet/modeemit/ethernet/dna-mesh-wifi-
wa8021v5/kayttoonotto) [ Asetukset
](https://www.dna.fi/tuki/laitteet/modeemit/ethernet/dna-mesh-wifi-
wa8021v5/wa8021v5/asetukset) [ Vianmääritys
](https://www.dna.fi/tuki/laitteet/modeemit/ethernet/dna-mesh-wifi-
wa8021v5/vianmaaritys) [ Päivitykset
](https://www.dna.fi/tuki/laitteet/modeemit/ethernet/dna-mesh-wifi-
wa8021v5/paivitykset)

##  Asetukset

Asetussivulle kirjautuminen

Kun tietokone tai muu päätelaite on kytketty langallisesti tai langattomasti
modeemiin, sen kaikkia asetuksia voidaan hallita nettiselaimella.
Suosittelemme käyttämään Google Chrome- ja Safari-selaimia.

  1. Avaa nettiselain ja kirjoita osoiteriville 192.168.101.1 tai dna.wifi/ ja paina **Enter**.
  2. User Name on **admin** ja password on **1234**
  3. Paina **Login** ja modeemin asetussivut aukeavat 

Nyt olet kirjautunut sisään modeemin asetussivuille. Voit vaihtaa salasanan
**More** -> **System Management** -> **Account Management** -valikosta.
Asetussivuilta voit muuttaa myös WiFi-asetuksia, verkon nimeä tai vaikkapa
suojausasetuksia sekä päivittää laitteen uusimpaan ohjelmistoversioon.

Salasanan vaihto ja unohtunut salasana

Kaikilla DNA:n langattomilla modeemeilla on tehdasasetuksiltaan sama salasana,
1234. Salasanaa tarvitaan, jotta laitteen asetuksia voidaan muuttaa. Salasana
tulee vaihtaa tietoturvasyistä, jotta ulkopuoliset eivät voi hallinnoida
modeemia. Kun olet kirjautunut asetussivuille, saat vaihdettua salasanan
seuraavasti:

  1. Valitse etusivulta **More**.
  2. Valitse **System Management** -valikon alta **Account Management**.   

  3. Kirjoita nykyinen salasanasi **Old Password** -kenttään. Tämän jälkeen kirjoita haluamasi uusi salasana **New Password** -kenttään sekä uudelleen **Confirm Password** -kenttään. Lopuksi paina **Apply**.

Bandsteering / yhdistelmäverkon pois päältä kytkeminen

Kirjaudu laitteen asetussivulle ja valitse **My Wi-Fi**.

My Wi-Fi -välilehdellä voit valita onko yhdistelmäverkko (2.4 GHz & 5 GHz)
käytössä. Jos haluat poistaa yhdistelmäverkon käytöstä, valitse **Dual-band
Combination** -valinnassa **OFF**. Muutos tallennetaan painamalla **Apply**.

Valinnan jälkeen sinulla on erilliset 2,4GHz ja 5GHz verkot, joiden asetuksia
voit muuttaa itsenäisesti.

DynDNS

Kirjaudu laitteen asetussivulle ja valitse **More**. Siirry sivun välilehdelle
**Network Configuration** -> **DDNS Function**.

Valitse **New**. Valitse **Enable DDNS** ja täytä vaadittavat tiedot kenttiin.
Lopuksi tallenna muutokset painamalla sivun alalaidasta **Apply**.

DynDNS-palvelun käyttö edellyttää, että käyttäjä on luonut valmiiksi tilin
DynDNS-palveluntarjoajalle.

Porttiohjaus

Kirjaudu laitteen asetussivulle ja valitse More. Siirry Security Configuration
-välilehden kautta IPv4 Port Mapping / IPv6 Port Mapping -välilehdelle.

Modeemissa on päällä oletuksena UnPn-työkalu portinohjaukseen. Esimerkiksi
pelattaessa tai käytettäessä latausohjelmia, käyttäjä voi avata portteja myös
manuaalisesti.

#### Manuaalisen ohjauksen tekeminen:

Valitse New ja täytä IP-osoitetiedot. Paina sitten Add ja lisää tarvittavat
porttitiedot. Add-painikkeesta saa avattua useampia portteja laitteelle.
Lopuksi paina Apply hyväksyäksesi muutokset.

Laitetiedot

#### Sarjanumeron tarkistus

Kirjaudu laitteen asetussivulle ja valitse **More**. Siirry **System Info**
-välilehdelle ja sitten **Device Information** -välilehdelle. Sarjanumero
näkyy kohdassa **SN**. Löydät sarjanumeron myös laitteeseen liimatusta
tarrasta.

#### Laiteversion tarkistus

Kirjaudu laitteen asetussivulle ja valitse **More**. Siirry **System Info**
-välilehdelle ja sitten **Device Information** -välilehdelle. Laiteversio
näkyy kohdassa **Software Version**.

#### WAN MAC -osoitteen tarkistus

Kirjaudu laitteen asetussivulle ja valitse **More**. Siirry **System Info**
-välilehdelle ja sitten **Device Information** -välilehdelle. WAN MAC -osoite
näkyy kohdassa **MAC**.

IP-osoitteen varaaminen sisäverkon laitteelle

#### IPv4

Kirjaudu laitteen asetussivulle ja valitse **More**. Siirry **Network
Configuration** -välilehden kautta **Lan Settings** -välilehdelle. Valitse
**Static IP address list** kohdasta **New**. Laita **MAC Address** -kohtaan
laitteen MAC-osoite, jolle haluat jakaa kiinteän osoitteen. **Laita IP
Address** -kohtaan IP-osoite, jonka haluat laitteelle. Osoitteen pitää olla
**IP Address Allocation Range** n sisällä oleva osoite.

#### IPv6

Kirjaudu laitteen asetussivulle ja valitse **More**. Siirry **Network
Configuration** -välilehden kautta **DHCPv6 Static IP Configuration**
-välilehdelle. Valitse **New**. Laita **MAC Address** -kohtaan laitteen MAC-
osoite, jolle haluat jakaa kiinteän osoitteen. **Laita IP Address** -kohtaan
IP-osoite, jonka haluat laitteelle esimerkin mukaisessa muodossa.

Verkon topologian katsominen

Kun sinulla on kaksi tai useampi DNA Mesh WiFi -modeemi käytössäsi, voit
katsoa topologia-näkymästä, että modeemit ovat optimaalisesti yhdistetty
toisiinsa. Voit myös tarkistaa minkä modeemin taakse laitteesi ovat
yhdistyneet.

Kirjaudu laitteen asetussivulle ja valitse **Terminal**. Terminal-sivulta näet
laitelistauksen. Oletuksena valittuna on laitteet, jotka ovat verkossa (Online
devices). Valitsemalla vetovalikosta **Offline devices** näet aiemmin verkossa
olleet laitteet.

Paina **Currently in list mode, click to switch to Topo chart mode**
-kuvaketta siirtyäksesi topologia-näkymään. Painamalla uudestaan samaa
kuvaketta pääset takaisin laitelistaukseen.

Virhelogin kerääminen laitteesta

Kirjaudu laitteen asetussivulle ja valitse **More**. Siirry **Maintenance
Diagnosis** -välilehden kautta **Fault Info Collect** -välilehdelle.

Paina **Start** aloittaaksesi login kerääminen. Kun logi on kerätty paina
**Download** -painiketta, logi latautuu laitteellesi collectFaultFinish.txt-
tiedostoon.

Lapsilukon asettaminen

Kirjaudu laitteen asetussivulle ja valitse **More**. Siirry **Security
Configuration** -välilehdelle ja sitten **Parental Control Configuration**
-välilehdelle.

  * Ensimmäiseksi valitse Template-välilehti ja luo sääntö lapsilukolle

  1. Valitse **New** ja määritä Templatelle nimi sekä aikajakso jolloin se on voimassa. Paina **Next**.
  2. Määritä onko lapsilukko voimassa koko päivän vai osan päivästä ja viikonpäivät jolloin se on voimassa. Paina **Apply** hyväksyäksesi asetukset. Paina **Next**.
  3. Seuraavassa kohdassa voi määrittää tietyt verkko-osoitteet, joita esto koskee. Paina **New** ja aseta osoite. Paina **Apply** hyväksyäksesi muutokset. Paina **Finish**.

  * Seuraavaksi valitaan laitteet, joiden halutaan olevan lapsilukon alaisuudessa.

  1. Siirry Overview-välilehdelle ja valitse **New**.
  2. Valitse laite, anna kuvaus laitteelle ja valitse käytettävä Template. Paina **Apply** hyväksyäksesi muutokset.

