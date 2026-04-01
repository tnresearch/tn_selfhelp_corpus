# Cisco EPC3828

# Cisco EPC3828

[ Ominaisuudet ](https://www.dna.fi/tuki/laitteet/modeemit/kaapeli/cisco-
epc3828/ominaisuudet) [ Käyttöönotto
](https://www.dna.fi/tuki/laitteet/modeemit/kaapeli/cisco-
epc3828/kayttoonotto) [ Asetukset
](https://www.dna.fi/tuki/laitteet/modeemit/kaapeli/cisco-epc3828/asetukset) [
Päivitykset ](https://www.dna.fi/tuki/laitteet/modeemit/kaapeli/cisco-
epc3828/paivitykset)

## Asetukset

Asetussivulle kirjautuminen

Laitteen kaikkia asetuksia hallitaan nettiselaimella. Laitteen muistissa
olevat asetussivut muistuttavat tavallisten nettisivujen käyttöä, joten
asetusten muuttaminen on helppoa. DNA suosittelee Internet Explorer-,
Firefox-, Google Chrome- ja Safari-selaimia.

Avaa nettiselain (tässä vaiheessa saatat saada virheilmoituksen selaimeesi,
mutta älä huomioi sitä). Kirjoita osoiteriville osoite http://192.168.0.1.
Enteriä painamalla pääset kirjautumissivulle.

  1. Kirjaudu asetussivulle jättämällä kummatkin kentät tyhjäksi (Käyttäjänimi ja Salasana).
  2. Paina Log In.
  3. Asetussivut aukeavat.  

  
Nyt olet kirjautunut sisään modeemin asetussivuille. Asetussivuilta voit
muuttaa myös WiFi-kanavia, verkon nimeä tai suojausasetuksia. Ensimmäiseksi
sinua kehotetaan vaihtamaan laitteen salasana Administration Management
-sivulla.  

Salasanan vaihto ja unohtunut salasana

Kaikilla DNA:n langattomilla modeemeilla on tehdasasetuksiltaan sama salasana.
Tietoturvan ja modeemin ulkopuolisen haltuunoton estämiseksi salasana tulee
vaihtaa.

  1. Valitse asetussivujen ylälaidan navigointivalikosta **Administration.**
  2. Valitse alemman ylälaidan navigointivalikosta **Management**. Tämän sivun kautta voit muuttaa laitteen käyttäjätunnusta ja salasanaa. Salasanaa tarvitaan, jotta laitteen asetuksia voidaan muuttaa.
  3. Kirjoita uusi käyttäjätunnus kohtaan **Change Current User Name to** ja salasana kohtaan **Change Password to** sekä uudelleen kohtaan **Re-Enter New Password**.
  4. Paina **Save Settings.**

WiFi-taajuuden vaihtaminen

Cisco 3828 -modeemin 2.4 GHz ja 5 GHz -taajuuksiset WiFi-verkot ovat
oletuksena samannimisiä. Tämä tarkoittaa, että valinta 5 GHz tai 2.4 GHz
käyttämiselle tapahtuu täysin automaattisesti päätelaitteen asetuksien mukaan.

WiFi-taajuus vaihdetaan **Wireless** -> **Radio Settings** -> kohdasta **Radio
Band**.

Valitsemalla alasvetolaatikosta 2.4 GHz tai 5 GHz, vaihdat tämän taajuuden
WiFi-verkon nimeä ja muita asetuksia. Jos tiedät haluavasi käyttää vain
jompaakumpaa taajuutta (2.4 GHz tai 5 GHz), kannattaa taajuuksien nimet (SSID)
vaihtaa erilaisiksi.

Esimerkiksi valitsemalla Radio Band -kohdasta 2.4 GHz -taajuuden ja
vaihtamalla tämän verkon nimeksi (SSID) ”Oman verkon nimi 2G” ja tekemällä
saman 5 GHz -taajuudelle ”Oman verkon nimi 5G” on oikean taajuuden löytäminen
helpompaa.

WiFi-salasanan vaihtaminen

Mene **Wireless** -> **Wireless Security** -> **Passphrase** -kohdassa
kirjataan salasana, joka oletuksena löytyy laitteen pohjassa olevasta tarrasta
( **Pre-shared-key** ).

Lähetyskanavan valinta ja vaihto

Valikkopuussa **Setup** -> **Quick Setup** voidaan vaihtaa salasana. Täällä
voit määrittää myös WiFi-radioiden asetuksia määrittämällä **Wireless
Interface enable/disable**. Radioiden taajuudet ovat 2,4 GHz ja 5 GHz. Voit
myös asettaa SSID:n ja salaustavan / kryptauksen.

Valitse asetussivujen ylälaidan navigointivalikosta **Wireless** ja vasemman
reunan navigointivalikosta **Basic Settings.**

  1. Valitse **Standard Channel** -alasvetovalikosta kanava väliltä 1-13.
  2. Paina **Save Settings.**

802.11n-tilan hallinta

Laitteiston tukiessa 802.11n -määritystä voi käyttää 40MHz-Wide Channel
toimintoa. Tällä parannetaan WiFi-verkon yhteysnopeutta.

  1. Valitse **Channel Width** -alasvetovalikosta **Wide 40 MHz Channel.**
  2. Paina **Save Settings.**

Langattoman yhteyden ja modeemin liikenteen salaaminen

Langattoman lähiverkon verkkoyhteyden suojaukseen on syytä kiinnittää
erityistä huomiota. Koska langaton lähiverkko toimii myös seinien läpi, on
verkon kattavuutta käytännössä mahdotonta rajata toimimaan vain halutulle
alueelle. Yhteyden salaaminen on tehokas tapa estää ulkopuolisilta
laajakaistaliittymän luvaton käyttö tai yhteyden haltuunotto. Salaus koskee
vain kaapelimodeemin ja tietokoneen välistä langatonta liikennettä.

Kaapelimodeemin ja tietokoneen välinen suojaus ei kuitenkaan estä internetistä
tulevia uhkia, kuten verkkohyökkäyksiä, viruksia ja tietomurtoja, joille
suojaamaton tietokone on aina alttiina, kun ollaan yhteydessä internettiin.
Siksi DNA suosittelee DNA Nettiturvan hankkimista. Se on helppo ja vaivaton
tapa huolehtia tietokoneen tietoturvasta. Langattomassa lähiverkossa
suosittelemme käytettäväksi niin kutsuttua WPA2 (Wi-Fi Protected Access)
-salausta. Se on käytettävissä olevista vaihtoehdoista tällä hetkellä
turvallisin. Oletusarvoisesti modeemi tukee sekä WPA2- PSK, TKIP ja WPA-PSK
salaustapoja.

Modeemin asettaminen siltaavaksi

Valitse asetussivujen ylälaidan navigaatiovalikosta **Administration** ja
vasemman reunan navigointivalikosta **Management** -> **Gateway Setup (WAN).**

  1. Valitse **Working Mode** -alasvetovalikosta **Bridged Only**
  2. Paina **Save Settings**

Huom! Hallintaosoite on sillattuna 192.168.100.1

IP Flood detection ja palomuuri

Mikäli nettiyhteys pätkii esim. surffatessa, konsolipelejä pelatessa, IP-
puheluita soittaessa, ladatessa tiedostoja, kannattaa kokeilla ottaa IP Flood
detection -asetus pois päältä (IP Flood detection = netistä tulevan IP-
pakettihyökkäyksen tunnistus).

Yhdistä tietokone modeemiin joko langattomasti tai Ethernetin kautta.

Kirjoita selaimeen osoite http://192.168.0.1 tai 192.168.0.1 riippuen onko
modeemi reitittävässä tai siltaavassa tilassa. Kirjaudu sisään tunnuksilla
(oletuksena käyttäjätunnus ja salasana jätetään tyhjäksi).

  1. Valitse ylhäältä **Security** -> **Firewall** -> näkymästä **Filters**
  2. Ota ruksi pois kohdasta **IP Flood Detection.**
  3. Paina **Save settings.**

**Huom.** Langattoman verkon käyttöön liittyviä asetuksia kannattaa muuttaa
vain sellaiselta tietokoneelta, joka on liitetty laitteeseen verkkokaapelilla
(Ethernet-kaapeli).

