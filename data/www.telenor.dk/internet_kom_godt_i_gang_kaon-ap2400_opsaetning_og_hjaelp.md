# Opsætning af Kaon AP2400

Det betyder dioderne (lamperne) på routeren

Routeren har to lamper: den øverste viser, om WiFi er tilsluttet, og den
nederste viser, om der er forbindelse. Under opstart lyser den nederste diode
(WAN) kortvarigt **hvid**.

  * Hvis den nederste lampe (WAN) lyser **rød** , er der ikke fysisk forbindelse til internettet  
 **Det kan du gøre:** tjek, om kablerne er korrekt tilsluttet og trykket helt
i bund

  * Blinker den nederste lampe (WAN) **orange** er der fysisk forbindelse, men ingen IP-adresse  
 **Det kan du gøre:** Prøv at nulstille routeren ved at trykke en nål eller
lignende genstand ind i reset-hullet i bunden af routeren. Dette skal gøres,
mens routeren er tændt, og reset-knappen holdes inde i 12 sekunder. Hvis reset
er korrekt udført, vil dioderne begynde at blinke ca. 10-20 sekunder efter
reset-knappen er sluppet

  * Lyser den nederste lampe fast **grøn** , modtager routeren IP-adressen og er online  
 **Det kan du gøre:** Tjek om dine enheder er forbundet til det korrekte WiFi,
og om kablerne er trykket i bund

  * Når den øverste lampe lyser **grøn,** er WiFi slået til, og hvis lampen er slukket, er WiFi slået fra. Den blinker, hvis WPS er aktiveret

##  Flere indstillinger

Sådan logger du ind på routeren (fx for at ændre WiFi-navn og password)

For at logge ind på routeren kræver det, at der er oprettet forbindelse til
routeren fra den enhed, der anvendes til login.  
I en browser taster du **http://10.0.0.1:2033** og trykker **Enter** for at
åbne login-siden.

**Username:** admin  
 **Password** : står på undersiden af routeren, og hedder "Router Kode".

Sådan ændrer du WiFi-navn og password

  * Log ind på din router ved at følge guiden 'Sådan logger du ind på routeren'. Gå derefter til menupunktet **WiFi**
  * Under **WiFi-Indstillinger** vælger du **WiFi 2,4 GHz** eller **WiFi 5 GHz** \- afhængigt af hvilket netværk, du ønsker at ændre navn på  
Bemærk: hvis du ikke ønsker to forskellige netværk, anbefales det, at du
navngiver dem med samme navn og password. På den måde får routeren mulighed
for at flytte din enhed over på det netværk, der er bedst i forhold til
signalstyrke og hastighed

  * Når du har indtastet de nye oplysninger, trykker du på **Gem  
** Bemærk: Hvis du har været tilsluttet via WiFi, vil din enhed blive logget
af netværket, og du skal logge på med de nye oplysninger

Fast LAN IP

Fast LAN IP bruges, hvis det er vigtigt, at din enhed har en bestemt IP-
adresse. Det kan fx være et lydanlæg eller en computer, der skal opsættes
portforward til.

1\. Log ind på din router ved at åbne din browser og taste:
**http://10.0.0.1:2033**

OBS: Der kan forekomme en advarsel på siden, ignorer denne og fortsæt.

Brugernavn: admin

Password: Indtast adgangskode til din router. Koden står på undersiden af
routeren og hedder Router Kode

2\. Klik på menuen **Advanced Parameters** og åbn **Network**

3\. Under punktet **Static DHCP leases** er der muligt at opsætte, slette
eller redigerer de faste IP-adresser

4\. Vælg enheden, der skal bruge en fast IP fra listen

5\. Skal enheden have en specifik IP, kan den ændres i det midterste felt

6\. Tryk på **Add** yderst til højre

7\. For at ændre i en IP skal den tidligere regel slettes, og en ny skal
oprettes

Reglerne kan slettes ved at trykke på skraldespanden i højre side.

Sådan opsætter du Port Forward

  * Log ind på din router ved at følge guiden 'Sådan logger du ind på routeren'. Herefter skal du vælge menupunktet **Netværk**
  * Vælg derefter fanen **Port Omdirigering**
  * Indtast de portoplysninger, der skal forwardes, samt den MAC-adresse, der skal forwardes til. Bemærk: IP-adresser må IKKE indtastes her
  * Vælg **Opret**

Sådan aflæser du signalstyrken på dit WiFi

  * Log ind på din router ved at følge guiden 'Sådan logger du ind på routeren'. Herefter skal du vælge menupunktet **Tilsluttede enheder**
  * På oversigten over tilsluttede enheder, finder du den enhed, du oplever, er langsom, eller har udfald, og klikker på navnet
  * Her aflæser du signalstyrken ( **Signal Strength** ). Hvis værdien er i spændet **-20 til –50** , indikerer det, at enheden modtager et godt signal. Fra **-50 til -70** vil signalet være acceptabelt, men du vil kunne opleve, at den modtagne hastighed er lavere. En signalstyrke fra **-70 til -100** indikerer, at der er lavt signal mellem routeren og enheden, du måler på. Dette vil kunne opleves i form af udfald på WiFi eller meget lav hastighed.

Du kan få gode råd til at forbedre din WiFi-dækning i hjemmet
[her](/shop/landingpage/bedre-wifi/).

Sådan tilslutter du enheder til routeren via WPS

Hvis du har en enhed (printer, smart device, WiFi-extender osv), der skal
tilsluttes via WPS, gøres det på følgende måde:

  * Placer den enhed, du ønsker at WPS-parre i umiddelbar nærhed af den tændte router
  * På siden af routeren findes en knap ved navn **WPS**. Tryk én gang og kortvarigt på denne. Hvis WPS-parringen er aktiveret, blinker den nederste diode på routeren. Du har nu 2 minutter til at gennemføre de følgende steps:

  1. Tryk på **WPS** -knappen på dit eget device, og vent i op til to minutter
  2. WPS-Parring er nu gennemført

Routerens specifikationer

**Specs på router:**

  * 1x 1Gbit LAN/WAN port
  * 4x 1Gbit LAN porte
  * 1x USB 3.0 port

  
**WiFi-tilslutning:**

  * IEEE 802.11b/g/n/ac/ax/