import random as r
import time

spells = [
	"Acceleratle",
	"Bang Family",
	"Bounce",
	"Flame Slash",
	"Hatchet Man",
	"Heal",
	"Hocus Pocus",
	"Kaclang",
	"Kacrackle Slash",
	"Kamikazee",
	"Magic Burst",
	"Metal Slash",
	"Oomph",
	"Psyche Up",
	"Sizz Family",
	"Snooze",
	"Whack Family",
	"Zoom"
]
weights = [
	0.0564,
	0.1250,
	0.0585,
	0.0629,
	0.0615,
	0.0311,
	0.0135,
	0.0248,
	0.0644,
	0.0178,
	0.0192,
	0.0291,
	0.0573,
	0.0562,
	0.1268,
	0.0600,
	0.0798,
	0.0557
]

spell_list = dict(zip(spells, weights))

pairs = {
	"Bang Family":{
		"Bang":0.4838,
		"Kaboom":0.5162
	},
	"Sizz Family":{
		"Sizz":0.4805,
		"Sizzle":0.5195
	},
	"Whack Family":{
		"Whack":0.4471,
		"Thwack":0.5529
	}
}

def grab_bag(spell_list):
	weights = list(spell_list.values())
	val = r.random()*sum(weights)
	running_sum = 0
	for s in list(spell_list.keys()):
		if (val > running_sum) and (val < running_sum + spell_list[s]):
			#print(s)
			return s
		else:
			running_sum += spell_list[s]

def get_menu(spell_list, pairs_list):
	m = ["","","",""]
	my_spells = spell_list.copy()
	for i in range(4):
		s = grab_bag(my_spells)
		del my_spells[s]
		#print(my_spells)
		m[i] = s
	for i in range(4):
		if m[i] in pairs_list.keys():
			my_spells = pairs_list[m[i]].copy()
			m[i] = grab_bag(my_spells)
	#print(m)
	return m

def simulate(n):
	with open("Simulate.csv", "w") as file:
		for i in range(n):
			m = get_menu(spell_list, pairs)
			csvstring = m[0] + "," + m[1] + "," + m[2] + "," + m[3] + "\n"
			file.write(csvstring)

simulate(20000)
