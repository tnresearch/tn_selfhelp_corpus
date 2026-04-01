# Modeemien tuki

# Modeemien tuki

## Modeemien käyttöohjeet

#### Modeemit kaapeliliittymään

[ DNA Kaapelimodeemi WiFi 6 F-3896
](https://www.dna.fi/tuki/laitteet/modeemit/kaapeli/dna-kaapelimodeemi-
wifi-6-f-3896) [ DNA Kaapelimodeemi F-3890v3
](https://www.dna.fi/tuki/laitteet/modeemit/kaapeli/dna-valokuitu-
plus-f-3890v3) [ DNA Kaapelimodeemi F-3686ACv2
](https://www.dna.fi/tuki/laitteet/modeemit/kaapeli/dna-valokuitu-
plus-f-3686acv2) [ DNA Kaapelimodeemi F-3686AC
](https://www.dna.fi/tuki/laitteet/modeemit/kaapeli/dna-valokuitu-
plus-f-3686ac) [ Sagemcom F-3284DC
](https://www.dna.fi/tuki/laitteet/modeemit/kaapeli/sagemcom-f-3284dc)

[ Näytä kaikki ](https://www.dna.fi/tuki/laitteet/modeemit/kaapeli)

#### Modeemit Ethernet-liittymään

[ DNA Ethernet WiFi 6 K562
](https://www.dna.fi/tuki/laitteet/modeemit/ethernet/dna-ethernet-wifi-6-k562)
[ DNA Ethernet WiFi 6 Plus F-5670
](https://www.dna.fi/tuki/laitteet/modeemit/ethernet/dna-ethernet-
wifi6-plus-f5670) [ DNA WiFi 6 F-266 Ethernet- ja Mesh-modeemi
](https://www.dna.fi/tuki/laitteet/modeemit/ethernet/dna-mesh-f-266) [ DNA
Ethernet EX400 ](https://www.dna.fi/tuki/laitteet/modeemit/ethernet/dna-
valokuitu-plus-ethernet-ex400) [ DNA Ethernet DG200AC
](https://www.dna.fi/tuki/laitteet/modeemit/ethernet/dna-valokuitu-plus-
ethernet-dg200ac)

[ Näytä kaikki ](https://www.dna.fi/tuki/laitteet/modeemit/ethernet)

#### Modeemit FTTH-liittymään

[ DNA Kuitumodeemi EG400AC
](https://www.dna.fi/tuki/laitteet/modeemit/ftth/dna-valokuitu-plus-modeemi-
eg400ac) [ DNA Kuitumodeemi EG300AC
](https://www.dna.fi/tuki/laitteet/modeemit/ftth/dna-valokuitu-plus-modeemi-
eg300ac)

[ Näytä kaikki ](https://www.dna.fi/tuki/laitteet/modeemit/ftth)

#### Modeemit xDSL-liittymään

[ DNA xDSL-modeemi ED500A
](https://www.dna.fi/tuki/laitteet/modeemit/xdsl/dna-xdsl-modeemi-ed500a) [
DNA DSL -modeemi DG200AC ](https://www.dna.fi/tuki/laitteet/modeemit/xdsl/dna-
dsl-modeemi-dg200ac) [ DNA xDSL -modeemi DG301AC
](https://www.dna.fi/tuki/laitteet/modeemit/xdsl/dna-xdsl-modeemi-dg301ac)

[ Näytä kaikki ](https://www.dna.fi/tuki/laitteet/modeemit/xdsl)

#### Mesh WiFi -modeemit

[ Näytä kaikki ](https://www.dna.fi/tuki/laitteet/modeemit/mesh-wifi)

## Modeemien asetus siltaavaksi

NAT (routed, reitittävä) ja BRIDGE (siltaava) -asetukset

Päätelaitteet tai modeemit ovat oletuksena joko NAT- tai Bridge-tilassa. NAT-
tilassa päätelaite jakaa kotiverkon IP-osoitteet laitteille ja liikennöinti
internetiin tapahtuu yhden julkisen IP-osoitteen avulla.

NAT-tilassa liittymään on mahdollista kytkeä useampia laitteita
samanaikaisesti. Bridge-tilassa (siltaava) kotiverkon IP-osoitteet jaetaan
suoraan DNA:lta, ja jokainen modeemin kytketty laite (max. 5 kpl) liikennöi
internetiin omalla julkisella IP-osoitteella. Esimerkiksi 100/350/1000 Mbit/s
-liittymissä saavutetaan paremmat yhteysnopeudet sillattuna.

Siltaavassa tilassa voidaan päästä reitittävää suurempiin huippunopeuksiin,
koska modeemi ei suodata liikennettä. Modeemit voi vaihtaa tarvittaessa
siltaavaan tilaan, jolloin laajakaistaan voi liittää 5 kpl verkkolaitteita.
Siltaavaksi vaihtaminen tarkoittaa että modeemissasi ei ole enää DHCP- ja NAT-
ominaisuudet käytössä eikä tiedostoja tai printtereitä pysty jakamaan
lähiverkossa. Myös yhdistettävien laitteiden tietoturva voi huonontua.
Verkkolaitteesi saa IP-osoitteen suoraan DNA:lta.

IP Flood -asetuksesta yleisesti

IP Flood Detection on netistä tulevan IP-pakettihyökkäyksen
tunnistusmenetelmä. Mikäli internet-yhteys pätkii surffatessa, skypettäessä,
ladatessa tiedostoja jne., tulee IP Flood detection -asetus ottaa pois päältä.
Asetus otetaan päälle ja pois päältä modeemikohtaisesti.

## Liikennerajoitukset

Kiinteiden laajakaistaliittymien osalta rajoitetaan julkisesta verkosta
liittymään suuntautuvaa IP-liikennettä. Rajoitukset vastaavat mm.
Viestintäviraston määräyksiä. Rajoitukset eivät poista tietoturvapalveluiden
tarvetta, kuten esimerkiksi palomuuri- ja virustorjuntaohjelmistoja.
Liikennöintiä rajoitetaan seuraavasti:

Estetyt portit (IPv4 ja IPv6)

  * 25 UL (TCP) 
  * 53 DL (UDP) 
  * 7547 UL/DL (TCP)
  * 1900 DL (UDP)

Yllä UL tarkoittaa päätelaitteelta Internetiin suuntautuvaa liikennettä ja DL
Internetistä päätelaitteelle suuntautuvaa liikennettä.

Lähtevä sähköpostiliikenne (SMTP)-liikenne liittymästä porttiin 25 on sallittu
vain DNA:n omille SMTP-palvelimille Viestintäviraston määräyksen mukaan.

Palvelinosoitteet

  * DNA:n SMTP-sähköpostipalvelimen osoite on smtp.dnainternet.fi
  * DNA:n NTP-aikapalvelimen osoite on ntp.dnainternet.fi
  * DNA:n DNS-nimipalvelimien IPv4-osoitteet: 62.241.198.245 ja 62.241.198.246
  * DNA:n DNS-nimipalvelimien IPv6-osoitteet: 2001:14b8:1000::1 ja 2001:14b8:1000::2

####

## Oman modeemin käyttäminen

Jotta saat täydet tehot netistä irti, suosittelemme käyttämään DNA:n testaamia
modeemeja.

Jos kuitenkin haluat käyttää muualta kuin DNA:lta hankittua modeemia, sinun
tulee huolehtia muutamasta seikasta.

[Siirry ohjeisiin](https://www.dna.fi/tuki/laitteet/modeemit/omamodeemi)

## Ohjevideot

#### Video: WiFin ja modeemin hienosäädöt

Katso, kuinka saat Wifistä ja modeemista parhaat mahdolliset tehot irti.

Katso video

#### Video: Sijoita modeemisi oikein

Modeemin sijainnilla on suuri merkitys netin kuuluvuuteen kodissasi. Katso
videolta vinkit modeemin sijoitteluun.

Katso video

## Netin vianrajaus

Ohjeet netin vianrajaukseen löydät netin tukisivuilta

[Siirry vianrajaukseen](https://www.dna.fi/tuki/netti/vianrajaus)

### Hidas netti?

Nopeustesti auttaa selvittämään laajakaistan nopeuden alle minuutissa.

[Tee nopeustesti](https://www.dna.fi/liittymat-ja-palvelut/netti/nopeustesti)

Huomioithan, että kodin nettiä käyttävien laitteiden (esim. tietokone,
televisio, puhelin) sekä modeemin tai [Mesh
Wifi](https://www.dna.fi/laitteet/modeemit-ja-mokkulat/mesh) -järjestelmän
suorituskyky ja yhteensopivuus vaikuttavat netin nopeuteen.

Netin nopeustesti on hyvä tehdä kytkemällä tietokone suoraan modeemiin
ethernet-kaapelilla. Langattoman WiFi-yhteyden kautta mitattuna nopeus voi
olla jopa puolet alhaisempi.

