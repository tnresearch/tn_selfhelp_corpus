# Modeemit FTTH-liittymään

# Modeemit FTTH-liittymään

Laajakaistayhteys optisella kuituyhteydellä (FTTH). Yleinen uusissa
asunnoissa, etenkin omakotitaloissa.

##### DNA Kuitumodeemi EG400AC

[](/tuki/laitteet/modeemit/ftth/dna-valokuitu-plus-modeemi-eg400ac)

##### DNA Kuitumodeemi EG300AC

[](/tuki/laitteet/modeemit/ftth/dna-valokuitu-plus-modeemi-eg300ac)

###  Vanhemmat modeemit

Laitteiden ohjelmistoja ei enää päivitetä aktiivisesti. Suosittelemme
vaihtamaan uuteen laitteeseen, jotta tietoturva ja suorituskyky ovat varmasti
ajan tasalla.

Inteno XG6846

  * [Pikaopas (PDF)](/documents/753910/853489/4430238_LOW_20150415_Kuitu_XG6846_Pikaopas_150x150.pdf/769002fb-29d9-a44d-00e6-5eb5c54af2ce)
  * [Asennus- ja käyttöohje (PDF)](/documents/753910/853489/DNA_Kuitulaajakaista_asennusjak%C3%A4ytt%C3%B6_WEB.pdf/8f8e820a-52ca-2ea7-cc03-1efb75dddeeb)
  * [Laaja englanninkielinen opas (PDF)](/documents/753910/853489/XG6846+Configuration+Manual++RevE.pdf/bc4ab8b7-b2f6-463c-08a6-d0ff6ec05e00)
  * [Miten tarkistat tietokoneesi verkkokorttiasetukset (PDF)](/documents/753910/853489/Miten-tarkistat-tietokoneesi-verkkokorttiasetukset_ohje.pdf/54a48b6c-753e-5b2b-72dd-f40153ac70ee)

Inteno EG500

###

### Oppaat

  * [Pikaopas (PDF)](/documents/753910/853489/Kuitu_EG500_Pikaopas.pdf/3f3e48af-947f-236e-4340-1fced064c504)
  * [Asennus- ja käyttöohje (PDF)](/documents/753910/853489/DNA_Kuitulaajakaista-laaja-opas.pdf/54ee3f5c-91e0-14e1-48ec-dcb467debb16)
  * [Miten tarkistat tietokoneesi verkkokorttiasetukset (PDF)](/documents/753910/853489/Miten-tarkistat-tietokoneesi-verkkokorttiasetukset_ohje.pdf/54a48b6c-753e-5b2b-72dd-f40153ac70ee)

### Muut ohjeet

  * [Päätelaitteen muuttaminen sillasta reitittavaksi sekä SSID:n ja salauksen muuttaminen (PDF)](/documents/753910/853489/EG500_SSID%2Bsek%C3%A4%2Bsalaus%2Bmuuttaminen.pdf/309f9e98-7d68-cf37-a31d-ea7a116cc335)
  * [Kuitupäätteen yhdistäminen (PDF)](/documents/753910/853489/EG500_kuitup%C3%A4%C3%A4tteen%2Byhdist%C3%A4minen.pdf/fd95b6d2-5ddd-2fe3-ca07-0920017334b2)
  * [Päivitysohjeet (PDF)](/documents/753910/853489/Inteno_DNA_DG201+ja+EG500_modeemin_paivitys.pdf/092ab7da-aeaf-f880-955c-ef6b5a73d75f)

### Päivitystiedostot

  * [EG500 v271.2](/documents/753910/853450/EG500_paivitystiedosto.2_20171218/c047f6e7-16e5-7d21-a8b3-16b9d926c8ec)

**Ominaisuudet**

  * FTTH kuitumuunnin SFP liittimellä
  * Langaton yhteys: Wi-Fi 802.11b/g 2,4GHz
  * 4kpl LAN-portteja (esim. digiboksille tai tietokoneelle)
  * IPv6 -tuki
  * Palomuuri ja NAT
  * DNA:n kustomoidut asetukset
  * Oletuksena siltaavassa tilassa, DNA suosittelee reitittävää tilaa

**Modeemin siltaus**

Oletuksena siltaavana, tässä ohje reitittäväksi muuttamiseen.

  1. Vaihda verkkokortin asetuksista ip-osoitteeksi 192.168.1.0 /24 esim 192.168.1.100 / 255.255.255.0
  2. Avaa selain ja syötä osoiteriville 192.168.1.1 ja paina ”Enter” . Kirjaudu sisään tunnuksilla admin/admin
  3. Mene Advanced setup -> WAN service
  4. Laita rasti eth4.2 kohdassa ruutuun ”Remove” ja paina ”Remove”
  5. Valitse jäljelle jääneen yhteyden kohdalla valitaruutu ”Edit”
  6. ”Edit”-painikkeella pääset Network Address Translation settings -valikkoon: Rasti ruutuun ”Enable NAT” (tämä enabloi reitityksen) Fulcone NAT ei tarvitse enabloida Palomuuri saadaan päälle ”Enable Firewall” Paina ”Next”-painiketta.
  7. Yhteenvetosivulla on yhteenveto asetuksista. Paina ”Apply/Save”.
  8. Mene vielä ”LAN”-valikkoon ja valitse ”Enable DHCP server” ja paina ”Apply/Save”

Mikäli haluat muuttaa LAN-osoitteet muuksi kuin 192.168.1.0/255.255.255.0,
onnistuu se tässä samassa valikossa

Inteno FG101 R2

### Oppaat

  * [Asennus- ja käyttöohje (PDF)](/documents/753910/853489/DNA_LK_Ethernet-ja-Kuitu_Opas.pdf/72c02d3e-fa37-d3df-1477-04644879a028)
  * [Miten tarkistat tietokoneesi verkkokorttiasetukset (PDF)](/documents/753910/853489/Miten-tarkistat-tietokoneesi-verkkokorttiasetukset_ohje.pdf/54a48b6c-753e-5b2b-72dd-f40153ac70ee)

### Muut ohjeet

  * [Liitinkotelon asennusohjeet Kuitu (PDF)](/documents/753910/853489/Inteno%2BFG-101%2BKuituliitinkotelon%2Basennusohjeet.pdf/3eccc47b-4fee-a6d9-38dc-70d4bf9ae1d7)
  * [Päivitysohje (PDF)](/documents/753910/853489/Inteno_DNA_FG101_R2_modeemin_paivitys_v2.pdf/e71f12a0-353b-d11f-bb23-36eb9b2c98ce)
  * [Ohje sillatusta reitittäväksi muuttamiseen (PDF) ](/documents/753910/853489/Silta+Natiksi+FG101.pdf/a3f31092-d256-0385-582e-21b1373c1933)

### Päivitysohjelmistot

  * [Lataa päivitysohjelmisto (ZIP)](/documents/753910/853489/inteno_FG101R2_pa%CC%88ivitysohjelmisto_3.12DNT21.zip/5cd8190e-b21a-a907-4ce4-0ea9f2aebd9a)

