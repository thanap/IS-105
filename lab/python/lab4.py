# -*- coding: latin-1 -*-

#
#  IS-105 LAB4
#
#  lab4.py - kildekode som inneholder studentenes løsning.
#         
#
#
import sys
import os
import subprocess
import re
import psutil # Kan installeres med "pip2.7 install psutil"

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'student1': 'Thananchai Prasomwong', \
			'student2': 'Kent Brekke Amundsen', \
            'student3': '-', \
}

# Oppgave 1
# 	Funksjonen lager en strukturert utskrift av resultater fra
#   kallet psutil.cpu_times(). 
#	Modulen psutil må være installert.
#
#   Utskriften skal være følgende (verdiene skal selvsagt være forskjellige):
#		user = 3088.16
#		nice = 0.99
#		system = 897.37
#		idle = 72353.81
#		iowait = 19.29
#		irq = 6.82
#		softirq = 3.07
#		steal = 0.00
#		guest = 0.00
#
print ""
print 5*"-" + " Oppgave 1 " + 5*"-"
def psutils_use():
	"""
	Henter lister med systeminformasjon fra /proc og bearbeider disse
	
	user = 178.09999999999999
	nice = 0.029999999999999999 
	system = 1125.3599999999999 
	idle = 6601.1000000000004
	iowait = 5.0499999999999998 
	irq = 68.780000000000001
	softirq = 78.870000000000005 
	steal = 0.0
	guest = 0.0
	
	"""
	# Impleementer funksjonen her
	pc_info = str(psutil.cpu_times())
	info_lister = pc_info.replace(', ', '\n').replace('(', ':\n').replace(')', '\n')
	print info_lister

	
psutils_use()
print ""

# Oppgave 2
#	Gitt følgende liste (inn-data):
# 	proglangs = [('Python', '1989', 'Guido van Rossum'), ('C', '1969', 'Dennis Ritchie'), ('Java/Oak', '1991', 'James Gosling'), ('C++', '1979', 'Bjarne Stroustrup'), ('Ruby', '1991', 'Yukihiro "Matz" Matsumoto'), ('Perl', '1987' , 'Larry Wall'), ('Go/golang', '2007', 'Robert Griesemer, Rob Pike, and Ken Thompson')]
#
#	skal funksjonen produsere følgende ut-data:
#
#		C ble startet 1969 av Dennis Ritchie.
#		C++ ble startet 1979 av Bjarne Stroustrup.
#		Perl ble startet 1987 av Larry Wall.
#		Python ble startet 1989 av Guido van Rossum.
#		Java/Oak ble startet 1991 av James Gosling.
#		Ruby ble startet 1991 av Yukihiro "Matz" Matsumoto.
#		Go/golang ble startet 2007 av Robert Griesemer, Rob Pike, and Ken Thompson.
#			
print 5*"-" + " Oppgave 2 " + 5*"-"
proglangs_tuples = [
                ('Python', '1989', 'Guido van Rossum'), 
                ('C', '1969', 'Dennis Ritchie'),
                ('Java/Oak', '1991', 'James Gosling'), 
                ('C++', '1979', 'Bjarne Stroustrup'),
                ('Ruby', '1991', 'Yukihiro "Matz" Matsumoto'), 
                ('Perl', '1987' , 'Larry Wall'),
                ('Go/golang', '2007', 'Robert Griesemer, Rob Pike, and Ken Thompson')]
    
sorted(proglangs_tuples, key=lambda proglangs: proglangs[1])
    


def liste_funksjon():
    ny_lister = [proglang + ' ble startet ' + year + ' av ' + person_s + '.' for proglang, year, person_s in proglangs_tuples]
    for element in ny_lister:
        print element
print liste_funksjon()
print ""

# Standardkall for evalueringen
print 5*"-" + " Studenter: " + 5*"-"
for s in gruppe.values():
	if s is not "-":
		print s





