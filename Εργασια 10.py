#!/usr/bin/python
# -*- coding: utf-8 -*-
# http://www.contrib.andrew.cmu.edu/~gc00/reviews/pokerrules
import itertools
import random

#Ελέγχει αν όλα είναι τα ίδια
def Five_of_a_Kind(h):
	kinds=[c[0] for c in h]
	kinds=list(set(kinds))
	if len(kinds)==1:
		return kinds[0]
	else:
		return 0

def print_hand(l):
	txt=""
	for c in l:
		txt+=str(c[0])+str(c[1])+","
	txt=txt[:-1]
	return txt

#Για να μη γράφουμε τα χαρτιά ας 
#φτιάξουμε την τράπουλα προγραμματιστικά
cards=[str(i) for i in range(1,11)] 
cards+=["J","Q","K"] #πρόσθεσε τις φιγούρες
suits=["S","H","D","C"] #βάλε τα χρώματα
deck=itertools.product(cards,suits) #Φτιάξε όλα τα φύλλα
deck=list(deck) #Ας τα έχω σε μία λίστα...
#Ας βάλουμε 2 τράπουλες
deck+=deck
#Ανακάτωσε την τράπουλα
random.shuffle(deck)
user_hand=[]
comp_hand=[]
#Μοίρασε τα χαρτιά
for i in range(5):
	user_hand+=[deck.pop()]
	comp_hand+=[deck.pop()]
print "Τα χαρτιά σου είναι: ",print_hand(user_hand)
cards2change=raw_input("Πόσα χαρτιά θες να αλλάξεις; Enter για έξοδο, αα χαρτιού με κενό για τα χαρτιά που θες να αλλάξεις.")
cards2change=cards2change.strip()
cards2change=cards2change.split()
cards2change=[int(c) for c in cards2change]
cards2change.sort(reverse=True)

if len(cards2change)>0:
	for crd in cards2change:
		user_hand.pop(crd-1)
	for i in range(len(cards2change)):
		user_hand+=[deck.pop()]
	print "Τα χαρτιά σου τώρα είναι: ",print_hand(user_hand)
print Five_of_a_Kind(user_hand)
print "Τα χαρτιά του υπολογιστή είναι: ",print_hand(comp_hand)


