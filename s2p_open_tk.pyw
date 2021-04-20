import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
from matplotlib import pyplot as plt
import numpy as np
import sys
import mplcursors
from tkinter import PhotoImage


LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)
style.use("default")


#######################################################################################################
#######################################################################################################
def cursor00_annotation(sel):
	sel.annotation.set_text(
		cursor_annotation_x.format(sel.target[0]) + cursor00_annotation_y.format(sel.target[1]))
	sel.annotation.get_bbox_patch().set(fc="powderblue", alpha=1)

def cursor01_annotation(sel):
	sel.annotation.set_text(
		cursor_annotation_x.format(sel.target[0]) + cursor01_annotation_y.format(sel.target[1]))
	sel.annotation.get_bbox_patch().set(fc="powderblue", alpha=1)
	
def cursor10_annotation(sel):
	sel.annotation.set_text(
		cursor_annotation_x.format(sel.target[0]) + cursor10_annotation_y.format(sel.target[1]))
	sel.annotation.get_bbox_patch().set(fc="powderblue", alpha=1)
	
def cursor11_annotation(sel):
	sel.annotation.set_text(
		cursor_annotation_x.format(sel.target[0]) + cursor11_annotation_y.format(sel.target[1]))
	sel.annotation.get_bbox_patch().set(fc="powderblue", alpha=1)
#######################################################################################################
#######################################################################################################

def naprintej(noter):
	print(noter)

edit_print = ""

def popupmsg_wE(noter):

	def leave_print():
		global edit_print
		edit_print = (e.get())
		print(edit_print)
		popupmsg_wE.destroy()
	
	popupmsg_wE = tk.Tk()
	popupmsg_wE.geometry("300x150")
	popupmsg_wE.wm_title("Kaj bi?")
	label = ttk.Label(popupmsg_wE, text=noter, font=NORM_FONT)
	label.pack(side="top", fill="x", pady=10)
	B1 = ttk.Button(popupmsg_wE, text="Okay", command=leave_print)
	B1.pack()
	
	e = ttk.Entry(popupmsg_wE)
	e.insert(0, noter)
	e.pack()
	e.focus_set()

	popupmsg_wE.mainloop()

nekej = "Navem!"
senekej = "Pujma nimam"

def blebni(kej, kva):
	global nekej
	global senekej
	nekej = kej
	senekej = kva
	print(nekej)
	print(senekej)

def file_save():
	fd = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
	if fd is None: # asksaveasfile return `None` if dialog closed with "cancel".
		return
	text2save = "blablahehehokinj03jf02j"
	fd.write(text2save)
	fd.close() # `()` was missing.
	
def popupmsg(msg):
	popup = tk.Tk()
	popup.geometry("300x150")
	#def leavemini():
	#	popup.destroy()
	popup.wm_title("!")
	label = ttk.Label(popup, text=msg, font=NORM_FONT)
	label.pack(side="top", fill="x", pady=10)
	B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
	B1.pack()
	popup.mainloop()

# def animate(i):
	# pullData = open("sampleData.txt", "r").read()
	# dataList = pullData.split("\n")
	# xList = []
	# y1List = []
	# y2List = []
	# for eachLine in dataList:
		# if len(eachLine) > 1:
			# x, y1, y2 = eachLine.split(",")
			# xList.append(int(x))
			# y1List.append(int(y1))
			# y2List.append(int(y2))
	# xIter = [0,1]
	# yIter = [0,1]
	# for x in xIter:
		# for y in yIter:
			# axs[x,y].clear()
			# axs[x,y].plot(xList, y1List, "g", label="Garej")
			# axs[x,y].plot(xList, y2List, "r", label="Dalej")
			# axs[x,y].grid(b=True, which="Major")
			# axs[x,y].set_title("Moj graf")
			# axs[x,y].legend(bbox_to_anchor=(0, 1.02, 1, 0.102), loc=3, ncol=2, borderaxespad=0)

class SeaofBTCapp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		
		tk.Tk.iconbitmap(self, default="s2p_open_icon.ico")
		tk.Tk.wm_title(self, "s2p_open")
		self.state("zoomed")
		
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		self.geometry(str(int(screen_width/1.3)) + "x" + str(int(screen_height/1.3)))
		
		container = tk.Frame(self)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)
		
		menubar = tk.Menu(container)
		
		filemenu = tk.Menu(menubar, tearoff=0)
		filemenu.add_command(label="Save settings", command = lambda: popupmsg("Not supported!"))
		filemenu.add_command(label="Save As", command = file_save)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=quit)
		menubar.add_cascade(label="File", menu=filemenu)
		
		edit = tk.Menu(menubar, tearoff=1)
		edit.add_command(label="resno", command=lambda: popupmsg_wE("blaaaa"))
		edit.add_command(label="blabla", command=lambda: blebni(edit_print, "vseeno2"))
		edit.add_command(label="blablabla", command=lambda: blebni("blablablaaaa", "vseeno3"))
		edit.add_command(label="hehe", command=lambda: blebni("heheho", "vseeno4"))
		menubar.add_cascade(label="Edit", menu=edit)
		
		tk.Tk.config(self, menu=menubar)
		
		self.frames = {}
		# for F in (s2p_open_mainWindow):
			# frame = F(container, self)
			# self.frames[F] = frame
			# frame.grid(row=0, column=0, sticky="nsew")
		
		frame = s2p_open_mainWindow(container, self)
		self.frames[s2p_open_mainWindow] = frame
		frame.grid(row=0, column=0, sticky="nsew")
		
		self.show_frame(s2p_open_mainWindow)
	
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# class StartPage(tk.Frame):
	# def __init__(self, parent, controller):
		# tk.Frame.__init__(self, parent)
		# label = ttk.Label(self, text="ALPHA Bitcoin trading application, use at your own risk.", font=LARGE_FONT)
		# label.pack(pady=10, padx=10)
		# button1 = ttk.Button(self, text="Agree", command=lambda: controller.show_frame(s2p_open_mainWindow))
		# button1.pack(pady=10, padx=10)
		# button2 = ttk.Button(self, text="Disagree", command=quit)
		# button2.pack(pady=10, padx=10)
		
class s2p_open_mainWindow(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		label = ttk.Label(self, text="Graph Page!", font=LARGE_FONT)
		label.pack(pady=10, padx=10)
		button1 = ttk.Button(self, text="Quit", command=quit)
		button1.pack(pady=10, padx=10)

		canvas = FigureCanvasTkAgg(fig, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		
		toolbar = NavigationToolbar2Tk(canvas, self)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		header = []
		header_length = 0
		with open(sys.argv[1], 'r') as read_obj:
			lines_read = read_obj.readlines()
			for row in lines_read:
				if ((row[0][0].strip() != '#') and (row[0][0].strip() != '!') and (row[0][0].strip() != '')):
					break
				header.append(row)
				header_length = header_length + 1

		idx_sxx = 0
		for idx, yesno in enumerate([s.lower().find("s11")>0 for s in header]):
			if yesno:
				idx_sxx = idx
		
		hashtag_position = [s[0].find("#") for s in header].index(0) + 1
		my_data = np.float_(list(map(str.split, map(str.strip, lines_read)))[header_length:])	
		
		plot_titles = [["S11", 1], ["S12", 5], ["S21", 3], ["S22", 7]]
		
		if header[hashtag_position-1].lower().find("ghz") > 0:
			xlabel_str = "f [GHz]"
			cursor_annotation_x = 'f = {:.4e} GHz\n'
		elif header[hashtag_position-1].lower().find("mhz") > 0:
			xlabel_str = "f [MHz]"
			cursor_annotation_x = 'f = {:.4e} MHz\n'
		elif header[hashtag_position-1].lower().find("khz") > 0:
			xlabel_str = "f [kHz]"
			cursor_annotation_x = 'f = {:.4e} kHz\n'
		elif header[hashtag_position-1].lower().find(" hz") > 0:
			xlabel_str = "f [Hz]"
			cursor_annotation_x = 'f = {:.4e} Hz\n'
		else:
			xlabel_str = "f [???]"
			cursor_annotation_x = 'f = {:.4e} ???\n'
		
		
		if (header[hashtag_position-1].lower().find("ma") > 0) and (header[hashtag_position-1].lower().find("s") > 0):
			ylabel_str = "[ ]"
			cursor00_annotation_y = "S11 = {:.2e}"
			cursor01_annotation_y = "S12 = {:.2e}"
			cursor10_annotation_y = "S21 = {:.2e}"
			cursor11_annotation_y = "S22 = {:.2e}"
		elif (header[hashtag_position-1].lower().find("db") > 0) and (header[hashtag_position-1].lower().find("s") > 0):
			ylabel_str = "[dB]"
			cursor00_annotation_y = "S11 = {:.2f} dB"
			cursor01_annotation_y = "S12 = {:.2f} dB"
			cursor10_annotation_y = "S21 = {:.2f} dB"
			cursor11_annotation_y = "S22 = {:.2f} dB"
		elif (header[hashtag_position-1].lower().find("ri") > 0) and (header[hashtag_position-1].lower().find("s") > 0):
			ylabel_str = "[real]"
			cursor00_annotation_y = "S11 = {:.2e} Real"
			cursor01_annotation_y = "S12 = {:.2e} Real"
			cursor10_annotation_y = "S21 = {:.2e} Real"
			cursor11_annotation_y = "S22 = {:.2e} Real"
		else:
			ylabel_str = "?????"
			cursor00_annotation_y = "S11 = {:.2e} ???"
			cursor01_annotation_y = "S12 = {:.2e} ???"
			cursor10_annotation_y = "S21 = {:.2e} ???"
			cursor11_annotation_y = "S22 = {:.2e} ???"

		if len(my_data[0,:]) == 9:
			fig, axs = plt.subplots(2, 2);
			
			fig.suptitle(sys.argv[1] + "\n" + header[idx_sxx].split("!")[1] + header[hashtag_position-1])
			fig.canvas.set_window_title("Left & right click places and removes a marker. Hint: v, b, n, m keys move cursors right, hold shift, and they will go left")

			axs[0, 0].plot(my_data[:,0], my_data[:,plot_titles[0][1]])
			axs[0, 0].set_title(plot_titles[0][0])
			axs[0, 0].set_xlabel(xlabel_str)
			axs[0, 0].set_ylabel("S11 " + ylabel_str)
			axs[0, 0].minorticks_on()
			axs[0, 0].grid(b=True, which="Major")
			axs[0, 0].grid(b=True, which="Minor", linestyle=':')
			#axs[0, 0].xaxis.set_major_formatter(FormatStrFormatter('%.3e'))

			axs[0, 1].plot(my_data[:,0], my_data[:,plot_titles[1][1]])
			axs[0, 1].set_title(plot_titles[1][0])
			axs[0, 1].set_xlabel(xlabel_str)
			axs[0, 1].set_ylabel("S12 " + ylabel_str)
			axs[0, 1].minorticks_on()
			axs[0, 1].grid(b=True, which="Major")
			axs[0, 1].grid(b=True, which="Minor", linestyle=':')

			
			axs[1, 0].plot(my_data[:,0], my_data[:,plot_titles[2][1]])
			axs[1, 0].set_title(plot_titles[2][0])
			axs[1, 0].set_xlabel(xlabel_str)
			axs[1, 0].set_ylabel("S21 " + ylabel_str)
			axs[1, 0].minorticks_on()
			axs[1, 0].grid(b=True, which="Major")
			axs[1, 0].grid(b=True, which="Minor", linestyle=':')

			
			axs[1, 1].plot(my_data[:,0], my_data[:,plot_titles[3][1]])
			axs[1, 1].set_title(plot_titles[3][0])
			axs[1, 1].set_xlabel(xlabel_str)
			axs[1, 1].set_ylabel("S22 " + ylabel_str)
			axs[1, 1].minorticks_on()
			axs[1, 1].grid(b=True, which="Major")
			axs[1, 1].grid(b=True, which="Minor", linestyle=':')

			
		elif len(my_data[0,:]) == 3:
			fig, axs = plt.subplots(1, 1);
			
			fig.suptitle(sys.argv[1] + "\n" + header[idx_sxx].split("!")[1] + header[hashtag_position-1])
			fig.canvas.set_window_title("Left & right click places and removes a marker. Hint: v key move cursors right, hold shift, and they will go left")

			axs.plot(my_data[:,0], my_data[:,plot_titles[0][1]])
			axs.set_title(plot_titles[0][0])
			axs.set_xlabel(xlabel_str)
			axs.set_ylabel("S11 " + ylabel_str)
			axs.minorticks_on()
			axs.grid(b=True, which="Major")
			axs.grid(b=True, which="Minor", linestyle=':')

			#axs.xaxis.set_major_formatter(FormatStrFormatter('%.3e'))

		plt.subplots_adjust(wspace=0.2, hspace=0.3)
	else:
		fig = plt.figure()
		fig.canvas.set_window_title("No data to plot")
		
	# mng = plt.get_current_fig_manager()
	# mng.window.state('zoomed')
	# try:
		# iconname = "s2p_open_icon.ico"
		# mng.window.wm_iconbitmap(sys.argv[0][:-len("s2p_open.pyw")] + iconname)
	# except:
		# print("Could not load the icon.")
			
	app = SeaofBTCapp()
	
	#fig.canvas.mpl_connect()
	if len(sys.argv) > 1:
		if len(my_data[0,:]) == 9:
			cursor00 = mplcursors.cursor(axs[0, 0], multiple=True, bindings={"toggle_visible": "h", "left": "V", "right": "v"})
			cursor00.connect("add",cursor00_annotation)
			cursor01 = mplcursors.cursor(axs[0, 1], multiple=True, bindings={"toggle_visible": "h", "left": "B", "right": "b"})
			cursor01.connect("add",cursor01_annotation)
			cursor10 = mplcursors.cursor(axs[1, 0], multiple=True, bindings={"toggle_visible": "h", "left": "N", "right": "n"})
			cursor10.connect("add",cursor10_annotation)
			cursor11 = mplcursors.cursor(axs[1, 1], multiple=True, bindings={"toggle_visible": "h", "left": "M", "right": "m"})
			cursor11.connect("add",cursor11_annotation)
		elif len(my_data[0,:]) == 3:
			cursor00 = mplcursors.cursor(axs, multiple=True, bindings={"toggle_visible": "h", "left": "V", "right": "v"})
			cursor00.connect("add",cursor00_annotation)
			
	app.mainloop()
