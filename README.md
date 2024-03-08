# Database prosjekt

## ER-modell og relasjonsdatabaseskjema

### ER-modell

![ER-modell bilde](ER-model.png)

#### Antakelser og begrunnelse

- En forutsetning vi gjorde var i relasjonen mellom Task og Employee. Vi tenkte at det kan forekomme oppgaver som ikke trenger å knyttes mot et bestemt stykke, men fortsatt være en arbeidsoppgave, for eksempel vedlikehold av scener. 
- Vi tenkte også at det ikke ville forekomme stykker som ikke trengte at noen oppgaver måtte gjøres.
- “Time” i “Showings” og “Ticket_purchases” tilsvarer tid og dato, da dette kan nyttes i SQLite.

### Relasjonsdatabaseskjema

Vi markerer primærnøkler med understrek og fremmednøkler i kursiv.

**halls**(<u>hall_id</u>, name)

- Alle tabeller er på 1NF når de har atomiske verdier og en primærnøkkel. Hall_id fungerer som en unik identifier, derfor er denne tabellen på 1NF, 2NF og 3NF. 2NF er oppfylt siden det ikke er noen delvis avhengighet. 3NF er oppfylt siden det ikke er noen transitive avhengigheter. BCNF er også oppfylt siden alle avhengigheter er av funksjonell karakter. Tabellen oppfyller også kravene til 4NF, det er ingen flerverdiavhengigheter.

**areas**(<u>area_id</u>, name, *hall_id*)

- Oppfyller alle normalformene siden area_id er en unik identifier, og det er ingen delvise eller transitive avhengigheter. BCNF er oppfylt fordi alle avhengigheter er av funksjonell karakter. Den tilfredsstiller også 4NF siden det ikke er noen flerverdiavhengigheter.

**seats**(<u>seat_id</u>, chair_number, row_number, *hall_id*, *area_id*)

- Tabellen oppfyller alle normalformene da seat_id er en unik identifier, og det er ingen delvise eller transitive avhengigheter. BCNF er oppfylt siden alle avhengigheter er av funksjonell karakter. Og det er ingen flerverdiavhengigheter, dermed er 4NF også oppfylt.

**plays**(<u>play_id</u>, name, *hall_id*)

- Tabellen oppfyller alle normalformene da play_id er en unik identifier, og det er ingen delvise eller transitive avhengigheter. BCNF oppfylt siden alle avhengigheter er av funksjonelle. Og det er ingen flerverdiavhengigheter, dermed er 4NF også oppfylt.

**showings**(<u>showing_id</u>, time, *play_id*)

- Alle normalformene er oppfylt fordi showing_id er en unik identifier, og det er ingen delvise eller transitive avhengigheter. BCNF oppfylt fordi alle avhengigheter er av funksjonell karakter. 4NF er også oppfylt siden det ikke er flerverdiavhengigheter.

**customers**(<u>customer_id</u>, name, mobile_number, address)

- Tabellen oppfyller normalformene fordi customer_id er unik og det er ingen delvise eller transitive avhengigheter. BCNF er oppfylt siden alle avhengigheter er av funksjonell karakter. Det er ingen flerverdiavhengigheter, derfor oppfyller tabellen 4NF.

**ticket_purchases**(<u>ticket_purchase_id</u>, time, *customer_id*)

- Tabellen oppfyller alle normalformene: Ingen delvise eller transitive avhengigheter, alle avhengigheter er funksjonelle, og det er ingen flerverdiavhengigheter.

**ticket_prices**(<u>ticket_price_id</u>, group, price, *play_id*)

- Denne tabellen oppfyller alle normalformene. Det er ingen delvise eller transitive avhengigheter, alle avhengigheter er funksjonelle og det er ingen flerverdisavhengigheter.

**tickets**(<u>*showing_id*</u>, <u>*seat_id*</u>, <u>*ticket_purchase_id*</u>, *ticket_price_id*)

- Tabellen oppfyller alle normalformene. Ticket_id gir en unik identifier, ingen delvise- eller transitive avhengigheter. Alle avhengigheter er av funksjonell karakter, derfor er BCNF også oppfylt. Det er ingen flerverdiavhengigheter, derfor oppfyller tabellen 4NF.

**acts**(<u>act_id</u>, number, name, *play_id*)

- Oppfyller alle normalformene av samme grunner som tidligere nevnt - unik identifier, ingen delvise- eller transitive avhengigheter, alle avhengigheter er funksjonelle og ingen flerverdiavhengigheter.

**roles**(<u>role_id</u>, name)

- Oppfyller alle normalformene av samme grunner som tidligere nevnt - unik identifier, ingen delvise- eller transitive avhengigheter, alle avhengigheter er funksjonelle og ingen flerverdiavhengigheter.

**roles_in_act**(<u>*act_id*</u>, <u>*role_id*</u>)

- Oppfyller alle normalformene av samme grunner som tidligere nevnt - unik identifier, ingen delvise- eller transitive avhengigheter, alle avhengigheter er funksjonelle og ingen flerverdiavhengigheter.

**actors**(<u>actor_id</u>, name)

- Oppfyller alle normalformene av samme grunner som tidligere nevnt - unik identifier, ingen delvise- eller transitive avhengigheter, alle avhengigheter er funksjonelle og ingen flerverdiavhengigheter.

**played_by**(<u>*role_id*</u>, <u>*actor_id*</u>)

- Oppfyller alle normalformene av samme grunner som tidligere nevnt - unik identifier, ingen delvise- eller transitive avhengigheter, alle avhengigheter er funksjonelle og ingen flerverdiavhengigheter.

**employees**(<u>employee_id</u>, name, email, status)

- Oppfyller alle normalformene av samme grunner som tidligere nevnt - unik identifier, ingen delvise- eller transitive avhengigheter, alle avhengigheter er funksjonelle og ingen flerverdiavhengigheter.

**tasks**(<u>task_id</u>, description, play_id, *employee_id*)

- Oppfyller alle normalformene av samme grunner som tidligere nevnt - unik identifier, ingen delvise- eller transitive avhengigheter, alle avhengigheter er funksjonelle og ingen flerverdiavhengigheter.
