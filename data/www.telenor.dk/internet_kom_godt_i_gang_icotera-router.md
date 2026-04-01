# Opsætning af Icotera i4882-70

Det betyder dioderne (lamperne) på routeren

Routeren har to lamper: den foroven viser, om WiFi er tilsluttet, og den
nedenunder viser, om der er forbindelse.

  * Hvis den nederste lampe (WAN) lyser rød, er der ikke fysisk forbindelse til internettet.  
 **Det kan du gøre:** Tjek kablerne for at se, om de er trykket helt i bund.

  * Blinker lyset i den nederste lampe, er der fysisk forbindelse, men ingen IP-adresse.  
 **Det kan du gøre:** Prøv at resette routeren ved at trykke en nål eller
lignende genstand ind i reset-hullet i bunden af routeren. Dette skal gøres,
mens routeren er tændt, og reset-knappen holdes inde i 10 sekunder. Hvis reset
er korrekt udført, vil lamperne begynde at blinke, efter at reset-knappen er
sluppet

  * Lyser den nederste lampe fast grøn, modtager routeren en IP-adresse og er online.  
 **Det kan du gøre:** Tjek derfor, om dine enheder er forbundet til det
korrekte WiFi, og om kabler er trykket i bund.

  * Når den øverste lampe (WiFi) lyser grøn er WiFi slået til, hvis lampen er slukket er WiFi slået fra. Hvis lampen blinker, er WPS aktiveret.

##  Flere indstillinger

Sådan logger du ind på routeren (fx for at ændre WiFi-navn og password)

  * For at logge ind på routeren kræver det, at der er oprettet forbindelse til routeren fra den enhed, der anvendes til login
  * I en browser taster du **http://10.0.0.1:80** og trykker **Enter** for at åbne login-siden  
 **Username:** admin  
**Password:** står på undersiden af routeren, og hedder "Router Kode". Hvis
ikke der er en Router Kode, anvendes dit WiFi-password.

Sådan ændrer du WiFi-navn og password

  * Log ind på din router ved at følge guiden 'Sådan logger du ind på routeren'. Når du er logget ind, skal du vælge menupunktet **Settings** og derefter **WiFi 2,4 GHz** eller **WiFi 5 GHz** , afhængigt af hvilket netværk du ønsker at ændre navn på  
 **Bemærk:** hvis du ikke ønsker 2 forskellige netværk, anbefales det, at du
navngiver dem med samme navn og password. På den måde får routeren mulighed
for at flytte din enhed over på det netværk, der er bedst i forhold til
signalstyrke og hastighed

  * Når du har indtastet de nye oplysninger, vælger du **Apply** , øverst på siden.  
 **Bemærk:** Hvis du har været tilsluttet via WiFi, vil din enhed blive logget
af netværket, og du skal logge på med de nye oplysninger

Sådan opsætter du Port Forward

Port Forwarding er en måde at give internetadgang til forskellige enheder -
det kan fx være et overvågningskamera eller en PlayStation. Har du problemer
med at forbinde enheden, får du koden **Strict Nat** , og så gør du følgende:

  * Log ind på din router ved at følge guiden 'Sådan logger du ind på routeren'. Når du er logget ind på routeren i et browser-vindue, skal du vælge menupunktet **Port Forward**
  * Sæt flueben i **Enable** ud for første ledige linje i højre side af vinduet
  * Indtast de portoplysninger, der skal forwardes samt den IP-adresse, der skal forwardes til   
**Bemærk:** Der skal laves en separat linje for hver regel, der opsættes

  * Når du har indtastet de nye oplysninger, vælger du **Apply** øverst på siden

Sådan aflæser du signalstyrken på dit WiFi

  * Log ind på din router ved at følge guiden 'Sådan logger du ind på routeren'. Når du er logget ind, skal du under menupunktet **Status** vælge enten **Wi-Fi 2,4 GHz** eller **Wi-Fi 5 GHz**
  * På oversigten over tilsluttede enheder, **Associated Clients** , finder du den enhed, du oplever, er langsom eller har udfald
  * I kolonnen **RSSI** aflæser du signalstyrken. Hvis værdien er i spændet **-20 til -50** , indikerer det, at enheden modtager et godt signal. Fra **-50 til -70** vil signalet være acceptabelt, men du vil kunne opleve, at den modtagne hastighed er lavere. Signalstyrke Fra **-70 til -100** indikerer, at der er lavt signal mellem routeren og enheden, du måler på. Dette vil kunne opleves i form af udfald på WiFi eller meget lav hastighed. Oplever du langsommere WiFi end forventet, er et godt råd at flytte enheden og routeren tættere på hinanden

Sådan tilslutter du enheder til routeren via WPS

Hvis du har en enhed (printer, smart device, WiFi-extender eller lignende),
der skal tilsluttes via WPS, gøres det på følgende måde:

  * Placer den enhed, du ønsker at WPS-parre i umiddelbar nærhed af den tændte router
  * På forsiden af routeren findes en knap ved navn **WPS**. Tryk én gang og kortvarigt på denne. Er WPS-parring aktiveret, blinker den nederste diode på routeren. Du har nu to minutter til at gennemføre de følgende steps:

  1. Tryk på **WPS** -knappen på dit device, og vent i op til to minutter
  2. WPS-Parring er nu gennemført

Routerens specifikationer

**Porte:**

  * 1x 2.5Gbit WAN port - benyttes ved tilkobling til fibermodem
  * 1x 2.5Gbit LAN port
  * 2x 1Gbit LAN porte
  * 1x USB 3.0 port

**WiFi-tilslutning:**

  * IEEE 802.11b/g/n 2.4 GHz
  * IEEE 802.11ax 2.4 GHz
  * IEEE 802.11ac 5 GHz
  * IEEE 802.11ax 5 GHz

**Kendte begrænsninger:**

  * Opsætning af Fast LAN IP (static lease) er ikke muligt
  * i4882-70-routeren kan ikke sættes i Bridge Mode. For alternative løsninger, er du velkommen til at kontakte Telenor
  * Det kan opstå problemer med at tilgå routerens GUI - dette kan løses ved at genstarte routeren