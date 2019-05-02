#!/usr/bin/env python3
import random, time, lists_o_stuff, tkinter as tk
from tkinter import ttk


#------ INIT ------
''' Window '''
window = tk.Tk()
window.title('The Boy or Girl Paradox')
window.geometry('850x600')
window.minsize(800, 540)

''' Flags '''
simulate_for_girls = tk.BooleanVar(value=True)
simulate_for_name = tk.BooleanVar(value=True)
diff_names_only = tk.BooleanVar(value=True)

''' Miscellanea '''
all_girl_names = len(lists_o_stuff.girl_names)
ttk.Style().configure('TCombobox', relief='flat')
name = tk.StringVar()
run = tk.IntVar(value=1)


#------ DEFINE ------
class wrap_label(tk.Label):
	''' Label that wraps to size '''
	def __init__(self, master=None, **kwargs):
		tk.Label.__init__(self, master, **kwargs)
		self.bind('<Configure>', lambda e: self.config(wraplength=self.winfo_width()))

class child:
	''' Each child receives a gender and a name. '''
	def __init__(self):
		self.isFemale = random.choice([True, False])
		if self.isFemale:
			self.name = lists_o_stuff.girl_names[random.randint(0, all_girl_names-1)]
		else:
			self.name = 'Dude'

def diversify_names(first_child, second_child):
	''' Naming your two children the same is bad for their development. '''
	while first_child.name==second_child.name:
		if second_child.isFemale:
			second_child.name = lists_o_stuff.girl_names[random.randint(0, all_girl_names-1)]
		else:
			second_child.name = 'Bro'
	return (first_child, second_child)

def Pairs_of_children():
	''' This is the fun part, creating the pairs of children. '''
	if diff_names_only.get():
		Pairs = (diversify_names(child(), child()) for _ in range(int(families.get())))
	else:
		Pairs = ((child(), child()) for _ in range(int(families.get())))
	return(Pairs)

def run_simulation():
	''' Now to run the simulation. '''
	# Init
	sis, bro, named_sis, named_sis_bro = 0, 0, 0, 0
	result_sis, result_named_sis = 0, 0
	time_1 = time.time()

	# add brothers and sisters of what we're checking, then divide them to find the percentage
	for firstborn, secondborn in Pairs_of_children():
		if simulate_for_girls.get():
			if firstborn.isFemale or secondborn.isFemale:
				sis += 1
				if not firstborn.isFemale or not secondborn.isFemale:
					bro += 1
		if simulate_for_name.get():
			if firstborn.name==Chosen_name.get() or secondborn.name==Chosen_name.get():
				named_sis += 1
				if not firstborn.isFemale or not secondborn.isFemale:
					named_sis_bro += 1
	time_2 = time.time()

	# Output
	results.config(state='normal')

	results.insert('end', 'Simulation #{}. Over {:,} pairs of siblings:\n'.format(run.get(), int(families.get())))
	try:
		result_sis = bro/sis * 100
		results.insert('end', '- For the {} girls we found, the odds of a male brother were: {:.2f}%.\n'.format(sis, result_sis))
	except ZeroDivisionError:
		results.insert('end', '- We aren\'t checking the odds for all girls.\n')
	try:
		result_named_sis = named_sis_bro/named_sis * 100
		results.insert('end', '- For the {} \'{}\' we found, the odds of a male brother were: {:.2f}%.\n'.format(named_sis, Chosen_name.get(), result_named_sis))
	except ZeroDivisionError:
		results.insert('end', '- We found no children named {}. There were too many spiders.\n'.format(Chosen_name.get()))
	timing = time_2 - time_1
	results.insert('end', 'This run took %0.3f seconds.\n\n' % timing)
	run.set(value=run.get() + 1)
	results.see('end')

	results.config(state='disabled')

def update_text(event):
	''' Update girl's name in the checkbox description according to the user's choiche '''
	check_name.config(text="Check the odds of a male brother for a girl named {}.".format(Chosen_name.get()))
	pass

def clear_simulation():
	''' Clear the results at the press of a button '''
	results.config(state='normal')
	results.delete('1.0', 'end')
	run.set(value=1)
	results.config(state='disabled')

def darker_bg():
	''' returns a slightly darker colour than default background '''
	colour = ''
	for i in window['bg']:
		if not i=='#':
			colour += i
	red = int(colour[0:2], 16) - 35
	green = int(colour[2:4], 16) - 35
	blue = int(colour[4:6], 16) - 35
	darker = hex(red)[2:] + hex(green)[2:] + hex(blue)[2:]
	return '#' + darker


#----- WINDOW CONTENTS -----
if __name__=='__main__':
	# Comment
	commentframe = tk.Frame(window)
	commentframe.pack(side='top', pady=15, padx=22, fill='x')

	comment = wrap_label(commentframe, text='This program demonstrates the claims of the famous "Boy or Girl Paradox" by simulating rows upon rows of randomised pairs of siblings, finding the ones which contain at least one girl, and then counting the odds of the other sibling being male.\n\nCheck it out for yourself.')
	comment.config(fg='#222222', bg=darker_bg(), font=('Default', 9), wraplength=comment.winfo_reqwidth(), justify='left', relief='flat', height=4, width=45)
	comment.pack(fill='x', expand=True)

	# Root
	frame = tk.Frame(window)
	frame.pack(side='top', fill='both', expand=True, padx=50)

	# Select name
	select_girl_name = tk.Frame(frame)
	select_girl_name.pack(side='top', fill="both")

	top_left = tk.Frame(select_girl_name)
	top_left.pack(side='left', fill='both', expand=True)

	sentence = tk.Label(top_left, text='Choose the name of the girl:', fg='#2C2C2C')
	sentence.pack(anchor='w', padx=20)

	Chosen_name = ttk.Combobox(top_left, values=lists_o_stuff.girl_names, state='readonly', textvariable=name)
	Chosen_name.current(0)
	Chosen_name.bind("<<ComboboxSelected>>", update_text)
	Chosen_name.pack(anchor='w', pady=24, padx=25)

	top_right = tk.Frame(select_girl_name)
	top_right.pack(side='right', fill='x', expand=True, padx=10)

	# Select families
	families_label = tk.Label(top_right, text='Choose the number of pairs of siblings to simulate:', fg='#2C2C2C')
	families_label.pack(anchor='nw')

	families = tk.Spinbox(top_right, relief='sunken', state='readonly', values=lists_o_stuff.numeros)
	families.pack(side='left', pady=5)

	warning = wrap_label(top_right, text='A word of advice.\nBelow 10,000 families the name you chose may not appear, and above 100,000 families the simulation may take a long time', wrap=200, justify='left', height=5)
	warning.config(font=("Default", 8), fg='#222222', bg=darker_bg())
	warning.pack(anchor='w', fill='x', expand=True, padx=10)

	# Flags
	checkboxes = tk.Frame(frame)
	checkboxes.pack(side='top', fill='both', pady=10)

	phrase = tk.Label(checkboxes, text='What do you want to check?', fg='#2C2C2C')
	phrase.pack(anchor='w')

	# Checkboxes
	flagframe = tk.Frame(checkboxes)
	flagframe.pack(fill='both', pady=10)

	check_girl = tk.Checkbutton(flagframe, text="Check the odds of a girl having a male brother.", variable=simulate_for_girls, onvalue=True, offvalue=False, fg='#2C2C2C')
	check_girl.pack(anchor='w')

	check_name = tk.Checkbutton(flagframe, text="Check the odds of a girl named {} having a male brother.".format(name.get()), variable=simulate_for_name, onvalue=True, offvalue=False, fg='#2C2C2C')
	check_name.pack(anchor='w')

	diff_names = tk.Checkbutton(flagframe, text="Ensure two siblings won't have the same name, because that's lazy parenting.", variable=diff_names_only, onvalue=True, offvalue=False, fg='#2C2C2C')
	diff_names.pack(anchor='w')

	# Simulation
	simulationframe = tk.Frame(frame)
	simulationframe.pack(side='bottom', fill='both', expand=True, pady=10)

	buttons = tk.Frame(simulationframe)
	buttons.pack(side='top', fill='x')

	runbutton = tk.Button(buttons, text='Run Simulation', fg='#2C2C2C', command=run_simulation)
	runbutton.pack(side='left')

	clearbutton = tk.Button(buttons, text='Clear Simulation', fg='#2C2C2C', command=clear_simulation)
	clearbutton.pack(side='right')

	showresults = tk.Frame(simulationframe)
	showresults.pack(fill='both', expand=True, pady=10)

	results = tk.Text(showresults, height=50, width=200, wrap='word', bg='#008080', fg='#40E0D0')
	results.pack(side='left', fill='both', expand=True)

	sidebar = tk.Scrollbar(results, relief='flat', command=results.yview)
	sidebar.pack(side='right', fill='y')
	results.config(yscrollcommand=sidebar.set)

	# Window loop
	window.mainloop()
