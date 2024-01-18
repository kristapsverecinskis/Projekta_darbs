# Projekta_darbs
##Programma priekš projekta darba "Lietojumprogrammatūras automatizēšanas rīki".

Projekta demonstrejuma video(https://youtu.be/QomoDa29_QI)

Projekta uzdevums:

Es pedēja laikā saskartos ar to, ka bieži vien aizmirstu paroles vai lietotajvardus. Lielākoties visas drošas programmas un aplikācijas kurās var droši saglabāt paroles ir maksas. Tādēļ es jau kādu laiku vēlējos izveidot programmu ar kuras palīdzību es varētu saglabāt lokāli uz sava datora paroles datubāzē, bet saskaros ar problēmu, ka jebkurš pie mana datora esot var piekļut datubazei ar parolem. Šogad kursa laika bija javeido programmas ar datu atšīfrēšanu, tādēļ radās ideja izveidot programmu ar lokālu šifra atslegu un paroles šifret izmantojot to atslēgu. Tākā man vidusskola bija saskarsme ar python un sqlite datubāzēm, es izveidoju scriptu, kas izveidos man datubāzi kura var saglabat majaslapas nosaukumu, lietotājvardu un šifretu paroli. Tālāk tika izveidots scripts kas izveido unikalu atslegu un saglaba to "parole.key" failā.


Prokta laika lietotas Python bibliotēkas:

Projekta izstrade tiek lietotas divas bibliotēkas:
- sqlite3 - šī bibliotēka tiek lietotā,lai izveidotu sqlite datubazi (programmas kods priekš izveides ir "datubazes_izveide" mapē) un, lai atvērtu sqlite datubāzi programmā un ievadīt datubāzē datus, kā arī, lai nolasītu nepieciešamos datus no datubāzes.
- cryptography.fernet - ši bibliotēka tika lietota, lai izveidotu atslēgu (programmas kods priekš atslēgas izveides atrodas "atslegas_izveide" mapē), kā arī, lai šifrētu paroli izmantojot doto atslēgu un atšifrētu paroli izmantojot doto atslēgu.

Programmas izmantošana:

- Lai sev iegūtu unikālu šifra atlsēgu palaidiet programmu, kas atrodas "atslegas_izveide" mapē ,un tiks saglabāta "parole.key" failā.
- Lai iegūtu jaunu datubāzi bez ierakstiem palaidiet programmu, kas atrodas "datubazes_izveide" mapē, un tiks izveidota datubāze ar nosaukumu "paroles.db".
- Izveidojiet jaunu mapi kur ievietojat savu šifra atslēgu un datubāzi, un ievietojat "main.py", no "Programma" mapes.
- Palaižot "main.py" jums piedavas divas izvēles. 1. jauns ieraksts, 2. paradit lietotajvardu ar paroli, ja netiks ievadīts 1 vai 2, priekš izvēles programma tiks aizvērta. Ievadot konsole skaitli 1 jums vaidzes ievadit majaslapas nosaukumu, tad lietotajvardu un paroli. ievadītie dati būs redzami datubāze tikai parole būs šifrēta. Izvēloties 2 jums prasis ievadīt mājaslapu no kuras velaties ietotajvardu ar paroli, ja datubaze nebus majslapas programma tiks aizverta, bet ja bus tad tiks paradits lietotājvards un atšifreta parole, no dotas mājaslapas.


