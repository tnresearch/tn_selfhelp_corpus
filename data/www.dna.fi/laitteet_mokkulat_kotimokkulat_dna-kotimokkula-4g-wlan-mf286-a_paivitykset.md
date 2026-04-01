# DNA Kotimokkula 4G+ WLAN MF286(A)

# DNA Kotimokkula 4G+ WLAN MF286(A)

[ Ominaisuudet ](https://www.dna.fi/tuki/laitteet/mokkulat/kotimokkulat/dna-
kotimokkula-4g-wlan-mf286-a/ominaisuudet) [ Käyttöönotto
](https://www.dna.fi/tuki/laitteet/mokkulat/kotimokkulat/dna-
kotimokkula-4g-wlan-mf286-a/kayttoonotto) [ Asetukset
](https://www.dna.fi/tuki/laitteet/mokkulat/kotimokkulat/dna-
kotimokkula-4g-wlan-mf286-a/asetukset) [ Päivitykset
](https://www.dna.fi/tuki/laitteet/mokkulat/kotimokkulat/dna-
kotimokkula-4g-wlan-mf286-a/paivitykset) [ Vianmääritys
](https://www.dna.fi/tuki/laitteet/mokkulat/kotimokkulat/dna-
kotimokkula-4g-wlan-mf286-a/vianmaaritys)

## Päivitykset

Laitteen ohjelmistoa ei enää päivitetä aktiivisesti. Suosittelemme vaihtamaan
uuteen laitteeseen, jotta tietoturva ja suorituskyky ovat varmasti ajan
tasalla.

### Ohjeet päivitykseen:

  1. Avaa nettiselain, kun olet kytkeytynyt DNA Kotimokkulan WiFi-verkkoon tai yhdistänyt laitteen Ethernet-johdolla.
  2. Kirjoita osoiteriville <http://192.168.1.1> tai http://dna.mokkula 
    * Oletuskäyttäjänimi on **admin**
    * Oletussalasana on **1234**
  3. Mikäli kirjautuminen ei onnistu, pidä DNA Kotimokkulan reset-painiketta pohjassa 30 sekunnin ajan ja yritä kirjautumista uudelleen.
  4. Valitse aloitussivun alareunasta **lisäasetukset.**
  5. Valitse ylävalikosta **päivitä.**
  6. Valitse **tarkista.**
  7. Seuraa käyttöliittymän ohjeita. Älä sammuta tai irrota virtajohtoa laitteesta päivityksen aikana. Päivitys voi kestää 5-30 minuuttia.

  
Jos päivitystä ei löydy tai se keskeytyy yllättäen, kokeile resetoida laite ja
tyhjentää selaimen välimuisti ja kokeile uudestaan.

**MF286 saa uuden päivityksen 15.8.2018 alkaen**

Muutoksina edelliseen versioon:

  * GDPR tiedote
  * Korjaus 2100 (B1) taajuuden aiheuttamaan pätkintään tai uudelleenkäynnistelyyn
  * Hienosäätöä lepotilaan

**Uusi versio: ZTE_DNA_MF286_B16**

  
DNA suosittelee päivityksen jälkeen tyhjentämään selaimen välimuistin
(evästeet, offline-tiedostot jne) sekä mahdollisuuksien mukaan resetoimaan
laitteen yläosan reset-painikkeesta (30 sek).

Päivitys tapahtuu portaittain eli kaikki eivät saa päivitystä samaan aikaan.
Jos käyttäjä päivittää laitteen vanhasta versiosta (vanhempi kuin B13),
päivitys voi tapahtua kahdessa osassa eli käyttäjän pitää päivittää laite
kahteen kertaan peräkkäin.

**MF286 saa uuden päivityksen 21.12.2017 alkaen**

Muutoksina edelliseen versioon:

  * Korjattu vika, missä asetukset häviävät uudelleenkäynnistyksessä joillakin laitteilla
  * Lisätty prosessi, missä päivitys tarkastaa ja korjaa mahdollisen flash-muistin korruptoinnin (korjausprosessi tapahtuu myös resetissä)
  * Lisätty yhdistelmätaajuuksien (CA) valinta/priorisointi
  * Lisätty valinta back-up yhteydelle Ethernetin yli
  * Telnet disabloitu
  * KRACK ja muita haavoittuvuuskorjauksia
  * Muutoksia käyttöliittymään
  * RSRQ, APN ja eNB tiedot lisätty lisätietoja-kenttään
  * Ajoitettu uudelleenkäynnistys-ominaisuus lisätty
  * Korjaus IPv6-allokointiin LAN-laitteelle
  * 5 GHz Wi-Fin katkaisu joissakin harvinaisissa tilanteissa korjattu
  * Huonon CA-yhteyden vaikutus mobiiliverkon stabiilisuuteen korjattu
  * CLAT toimintaa parannettu, otathan käyttöön MTU 1400 ja MSS 1360
  * Muita pienempiä korjauksia

**Uusi versio on: ZTE_DNA_MF286_B13**

**MF286 saa uuden päivityksen 30.8.2017 alkaen**

**Muutoksina edelliseen versioon:**

  * Mobiilikäyttöliittymä DNA:n väreihin
  * Päivitysilmoituksiin muutoksia
  * Tekstiviesti ei pakota lukua
  * "Pakkopäivitys" korjattu (toimii vasta seuraavan päivityksen yhteydessä)
  * 700Mhz lukko lisätty
  * CLAT tuki kokeilussa (IPv4 > IPv6 konversio, löytyy APN-asetuksista)
  * USB-tuki (FTP-server) korjattu
  * 802.11ac DFS-kanavat lisätty. Toimii ainoastaan automaattisessa kanavavalinnassa
  * RJ11-portit toimivat, ääni CSFB:n kautta. Huom. kokeiluasteella, SIM-kortti pitää olla puheellinen
  * Virtual server -toiminto lisätty
  * CPU ja RAM tiedot löytyvät system valikosta
  * Korjaus ongelmaan, missä LAN1-porttiin kytketyt jotkin käyttölaitteet aiheuttivat häiriötä mobiiliyhteyteen
  * Muita käyttöliittymä, tietoturva ja käytettävyyskorjauksia

**Uusi versio on: ZTE_DNA_MF286_B10**

**MF286:lle on julkaistu päivitys 10.11.2016.**

Muutoksina edelliseen versioon:

  * Korjattu DHCP-käyttäytyminen siltaavassa tilassa (helpottaa kolmannen osapuolen reitittimen käyttämistä)
  * Rautakiihdytys toimii nyt kaikissa tilanteissa
  * SSH-yhteys IPv6:lla korjattu
  * DNA APN:t lisätty valikkoon
  * Oletus-APN muutettu tulevan tuotteistuksen muotoon
  * Lisätietoja -valikkoon lisätty tieto tukiasemasta, mihin laite on yhdistänyt
  * Käännöskorjauksia

**Uusi versio on: ZTE_DNA_MF286_B04**

