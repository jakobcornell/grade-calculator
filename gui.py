import tkinter as tk
from tkinter import filedialog, messagebox

import serialization

NUMBER_ENTRY_WIDTH = 6

course = None
category = None
assignment = None

dirty = True
current_file = None

def load_course(infile):
	try:
		course = serialization.deserialize(infile)
	except:
		print("error")
	category_list.delete(0, tk.END)
	for category in course.categories:
		category_list.insert(tk.END, category.name)
	assignment_list.delete(0, tk.END)

def confirm_loss():
	return messagebox.askokcancel("Confirm", "Are you sure? This will discard your changes.")

# main window
root = tk.Tk()
root.wm_title("Grade Calculator")

options = {}

# menus
menu = tk.Menu(root)

def on_open():
	global current_file
	new_file = filedialog.askopenfile()
	if new_file and (not dirty or confirm_loss()):
		current_file = new_file
		load_course(current_file)

def on_save():
	global current_file
	if current_file:
		serialization.serialize(course, current_file)
		dirty = False
	else:
		on_save_as()

def on_save_as():
	global current_file
	new_file = filedialog.asksaveasfile()
	if new_file:
		current_file = new_file
		on_save()

def on_quit():
	if not dirty or confirm_loss():
		root.destroy()

file_menu = tk.Menu(menu, tearoff = False)
file_menu.add_command(label = "Open", command = on_open)
file_menu.add_command(label = "Save", command = on_save)
file_menu.add_command(label = "Save As...", command = on_save_as)
file_menu.add_separator()
file_menu.add_command(label = "Quit", command = on_quit)
menu.add_cascade(label = "File", menu = file_menu)

options['menu'] = menu

content = tk.Frame(root, padx = 5, pady = 5)
content.pack()

# score output
score_section = tk.Frame(content)
score_label = tk.Label(score_section, text = "Score", padx = 5)
score_label.grid(row = 0, column = 0)
score_text = tk.Text(score_section, width = NUMBER_ENTRY_WIDTH, height = 1, padx = 5)
score_text.grid(row = 0, column = 1)
score_section.pack()

def set_score(score):
	score_text.configure(state = tk.NORMAL)
	score_text.delete(1.0, tk.END)
	score_text.insert(tk.END, str(score))
	score_text.configure(state = tk.DISABLED)

set_score(44.5)

# category section
category_section = tk.LabelFrame(content, text = "Categories", padx = 5, pady = 5)
category_section.pack()

# category listbox
category_list = tk.Listbox(category_section, selectmode = tk.BROWSE)
category_list.insert(tk.END, "item one")
category_list.insert(tk.END, "item two")
category_list.grid(row = 0, column = 0, padx = 5, pady = 5)

def on_category_select(event):
	print(event.widget.curselection())

category_list.bind('<<ListboxSelect>>', on_category_select)

# category options
category_options = tk.Frame(category_section)
name_label = tk.Label(category_options, text = "Name")
name_label.grid(row = 0, column = 0)
name_entry = tk.Entry(category_options)
name_entry.grid(row = 0, column = 1)
weight_label = tk.Label(category_options, text = "Weight", pady = 10)
weight_label.grid(row = 1, column = 0)
weight_entry = tk.Entry(category_options, width = NUMBER_ENTRY_WIDTH)
weight_entry.grid(row = 1, column = 1, sticky = tk.W)
weighting_box = tk.Checkbutton(category_options, text = "Weighting")
weighting_box.grid(row = 2, column = 0, columnspan = 2, sticky = tk.W)
category_options.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = tk.N)

# assignment section
assignment_section = tk.LabelFrame(content, text = "Assignments", padx = 5, pady = 5)
assignment_section.pack()

# assignment listbox
assignment_list = tk.Listbox(assignment_section, selectmode = tk.BROWSE)
assignment_list.insert(tk.END, "sample assignment")
assignment_list.grid(row = 0, column = 0, padx = 5, pady = 5)

def on_assignment_select(event):
	print("selected assignment")

assignment_list.bind('<<ListboxSelect>>', on_assignment_select)

# assignment options
assignment_options = tk.Frame(assignment_section)
name_label = tk.Label(assignment_options, text = "Name")
name_label.grid(row = 0, column = 0)
name_entry = tk.Entry(assignment_options)
name_entry.grid(row = 0, column = 1)
score_label = tk.Label(assignment_options, text = "Score", pady = 10)
score_label.grid(row = 1, column = 0, sticky = tk.W)
score_controls = tk.Frame(assignment_options)
earned_entry = tk.Entry(score_controls, width = NUMBER_ENTRY_WIDTH)
earned_entry.grid(row = 0, column = 0)
tk.Label(score_controls, text = "/").grid(row = 0, column = 1)
possible_entry = tk.Entry(score_controls, width = NUMBER_ENTRY_WIDTH)
possible_entry.grid(row = 0, column = 2)
score_controls.grid(row = 1, column = 1, sticky = tk.W)
weight_label = tk.Label(assignment_options, text = "Weight")
weight_label.grid(row = 2, column = 0)
weight_entry = tk.Entry(assignment_options, width = NUMBER_ENTRY_WIDTH)
weight_entry.grid(row = 2, column = 1, sticky = tk.W)
assignment_options.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = tk.N)

root.bind_all('<Control-o>', lambda event: on_open())
root.config(**options)

# launch window
root.mainloop()
