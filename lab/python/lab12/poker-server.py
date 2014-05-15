# -*- coding: latin-1 -*-

# http://pymotw.com/2/select/
# http://www.tutorialspoint.com/python/python_dictionary.htm

# Sockets programmering i Python
# Utforskning av sockets api og andre Python moduler
# Module kan betraktes som en slags plug-in som utvider funksjonaliteten til et grunnlag
# Et grunnlag er programmeringsmiljø som man kan bruke for å gjøre "beregninger" / implementere "systemer"

# select module gir tilgang til platform-spesifikke INN/UT monitorerings-funksjoner
# select() er en POSIX funksjon som det finnes gode implementasjoner for i både UNIX- og Windows miljøer
# POSIX er et forsøk på å standardisere et operativsystem
import select

import socket
import sys
import Queue

import random # har ikke tenkt på det, tenkte bare at vi skulle gjøre 2 oppgaver

#jeg kopiert denne filen rett fra fronter og trodde at alle import og andre funksjoner var helt korrekt. og da fokuserte jeg bare på oppgave 1 og 2 der vi skulle løse
import lab11

# Her er data for pokerspillet
# For enkelhets skyld deler vi ut kort i det vi starter server
# Dette bør skje på forespørsel fra en klient i neste versjon av programmet
#hands = poker.deal(3)
hands = []
handsdelt = 0 # Vi trenger en variabel som holder styr på hvor mange hender er delt ut
numberOfPlayers = 0
board = []
#her skulle være en variable som viser antall spillere, men jeg har ombestemt meg og slettet den.

# Lage en TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Binde socketen på lokalmaskinen til porten 10000
server_address = ('localhost', 10000)
print >>sys.stderr, 'starter socket på %s og port %s' % server_address
server.bind(server_address)

# Høre / vente på innkommende forbindelser
server.listen(5)

# Med select() kan man følge med på mer enn en forbindelse av gangen
# Argumenter til select() er tre lister som inneholder kommunikasjonskanaler som skal observeres / monitoreres
# (1) liste av objekter for data som kommer inn fra andre enheter og skal leses/avleses/konsumeres
# (2) liste av objekter som vil motta data som er på vei ut, dvs. en slags lagerplass for data som sendes ut til andre enheter
# (3) en liste over de objektene som har feilet, kan være objekter fra både "input" og "output" kanaler
# Man må sette opp lister som inneholder INN-kilder og UT-bestemmelsessted
# Forbindelser blir lagt til og fjernet fra disse listen av hovedløkken til serveren

# Sockets som vi forventer å lese fra (kilder)
inputs = [ server ]

# Sockets hvilke vi forventer å skrive til (bestemmelsessted)
outputs = [ ]

# Man kan ha forskjellige kommunikasjonsstrategier
# Server kan vente for at en socket blir skrivbar (man kan skrive til den) før man sender noen data,
# istedenfor å sende responsen umiddelbart.
# I et slikt tilfelle, trenger hver UT-forbindelse en meldingskø, som fungerer som en mellomlager (buffer)
# Data må da sendes gjennom denne "bufferen", typen som brukes her er dictionary
message_queues = {}

# Hoveddelen av serverprogrammet er denne løkken som løper, og kaller select() som blokkerer utførelsen og 
# venter på nettverksaktivitet
while inputs:
	# Vent inntil minst en av socketene er klar for prosessering
	print >>sys.stderr, '\nventer på neste hendelse'
	readable, writable, exceptional = select.select(inputs, outputs, inputs)

# select returnerer tre nye lister, som er subset av de opprinnelige listene
# (1) alle socketene i readable listen har mellomlagret INN-data og er klare til å bli lest
# (2) alle socketene i writable har fri lagringsplass i deres lager og kan bli skrevet til
# (3) socketene som er returnert gjennom exceptional har hatt en feil (definisjon av uttak er platformavhengig)

	for key in message_queues.keys():
		print >>sys.stderr, 'spiller %s er meldt seg for spill' % str(key.getpeername())

# Socketene i readable representerer tre mulige tilfeller:
# (1) hvis socketen er hoved-"server"-socket, den som lytter etter forbindelser, da "readable"-tilstanden betyr
#     at den er klar til å akseptere en annen innkommende forbindelse;
# 	  I tillegg til å legge til en ny forbindelse i inputs-listen for monitorering, denne kode-seksjonen setter også
#     klient-socketen slik at den ikke blokkeres

# Behandler inputs her
	for s in readable:
		if s is server:
			# En lesbar (readable) server socket er klar til å akseptere forbindelser
			connection, client_address = s.accept()
			print >>sys.stderr, 'en ny forbindelse fra', client_address
			connection.setblocking(0)
			inputs.append(connection)

			# Gi forbindelse en kø for data som man ønsker å sende
			message_queues[connection] = Queue.Queue()
# (2) Dette er tilfelle når man har en allerede etablert forbindelse som man allerede 
#     har brukt for å sende data
#     Data leses med recv(), så blir plassert i en kø, slik at den kan bli sendt gjennom socketen tilbake til klienten
		else:
			data = s.recv(1024)
			if data:
				# En lesbar klient-socket som har data
				print >>sys.stderr, 'mottok "%s" fra %s' % (data, s.getpeername())

				

				# Koden skrevet av studenter
				# Sjekk meldingskø og også inputs
				# Her kan man behandle data som man mottar
				# Man kan også gi forskjellig respons til forskjellige klienter
				# OPPGAVE: del ut en hånd til en klient som sender JOIN
				# Her må du tenke på en algoritme som klarer å begrense antall klienter som kan spille
				# og hvor du også må finne en måte å dele ut kort på til hver av spillere
				# hands er her laget ved start av server, men finn også ut 
				if data == 'JOIN\n':
					#data = ' '.join(str(x) for x in hands[0])
					#message_queues[s].put(data)
					
					if numberOfPlayers == 3:
						print >>sys.stderr, 'maks antall spillere er nådd'
						#errir = 'for mange spillere med.' jeg har ikke linux på den pcen jeg bruker å programere derfor det er umulig for meg å sjekke skrivefeilen. jeg kjørte python i windows, men det fungerte ikke som det skulle.
						error = 'for mange spillere med'
						message_queues[s].put(error)

					else:
						board.append(s.getpeername())
						numberOfPlayers += 1
						#joined = 'Det er %d av %d spillere med' % (numberOfPlayers +her skulle være en variable som viser antall spillere på bordet,
						#men jeg har slettet det variable fordi den var litt komplisert for andre som er i gruppe og jeg har glemt å endre på det. denne funksjon skulle egentlig være en "%d" istedet for to av them.
						joined = 'Du er spiller nr %d' % numberOfPlayers # %d står for number of players
						message_queues[s].put(joined)

				if data == 'DEAL\n':
					if numberOfPlayers == 3:
						hands = lab11.deal(3)
						play = dict(zip(board, hands))
						dealSuccess = 'kort utdelt'
						message_queues[s].put(dealSuccess)

					else:
						error = "Det er ikke nok spillere"
						message_queues[s].put(error)

				if data == "GETHAND\n":
						hand = play.get(s.getpeername())
						handString = str(hand)
						message_queues[s].put(handString)
						

				# Legg til UT-kanalen for responsen
				if s not in outputs:
					outputs.append(s)
# (3) En lesbar socket uten tilgjengelige data er fra en klient som har koblet seg fra, slik at strømmen kan lukkes
			else:
				# Interpreter en tom resultat som en lukket forbindelse
				print >>sys.stderr, 'lukker', client_address, 'etter at ingen data kunne leses'
				# Stopper å høre for IN-data på denne forbindelsen
				if s in outputs:
					outputs.remove(s)
				inputs.remove(s)
				s.close()

				# Fjern meldingskø
				del message_queues[s]

# Det er mindre antall muligheter for writable
# Hvis det er data i køen for en forbindelse, neste melding blir sendt
# Ellers, forbindelsen fjernes fra liste for UT-forbindelser, slik at i neste omgang i løkken select()
# ikke skal indikere at socketen er klar til å sende data
	for s in writable:
		try:
			next_msg = message_queues[s].get_nowait()
		except Queue.Empty:
			# Ingen meldinger venter -> stoppe sjekking for skrivbarhet
			print >>sys.stderr, 'UT køen for', s.getpeername(), 'er tom'
			outputs.remove(s)
		else:
			print >>sys.stderr, 'sender "%s" til %s' % (next_msg, s.getpeername())
			s.send(next_msg)

# Til slutt, hvis det er en feil i socketen, den blir lukket
	for s in exceptional:
		print >>sys.stderr, 'behandler feilsituasjon for', s.getpeername()
		# Stoppe å høre for input for forbindelsen
		inputs.remove(s)
		if s in outputs:
			outputs.remove(s)
		s.close()

		# Fjern meldingskø
		del message_queues[s]
