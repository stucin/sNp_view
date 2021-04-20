import matplotlib.pyplot as plt
plt.switch_backend('TkAgg')
#plt.switch_backend('Qt5Agg')
import numpy as np
import sys
import mplcursors
from tkinter import PhotoImage


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

def say_hello(systray):
	print("Hello, World!")

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
			cursor00 = mplcursors.cursor(axs[0, 0], multiple=True, bindings={"toggle_visible": "h", "left": "V", "right": "v"})
			cursor00.connect("add",cursor00_annotation)
			#axs[0, 0].xaxis.set_major_formatter(FormatStrFormatter('%.3e'))

			axs[0, 1].plot(my_data[:,0], my_data[:,plot_titles[1][1]])
			axs[0, 1].set_title(plot_titles[1][0])
			axs[0, 1].set_xlabel(xlabel_str)
			axs[0, 1].set_ylabel("S12 " + ylabel_str)
			axs[0, 1].minorticks_on()
			axs[0, 1].grid(b=True, which="Major")
			axs[0, 1].grid(b=True, which="Minor", linestyle=':')
			cursor01 = mplcursors.cursor(axs[0, 1], multiple=True, bindings={"toggle_visible": "h", "left": "B", "right": "b"})
			cursor01.connect("add",cursor01_annotation)
			
			axs[1, 0].plot(my_data[:,0], my_data[:,plot_titles[2][1]])
			axs[1, 0].set_title(plot_titles[2][0])
			axs[1, 0].set_xlabel(xlabel_str)
			axs[1, 0].set_ylabel("S21 " + ylabel_str)
			axs[1, 0].minorticks_on()
			axs[1, 0].grid(b=True, which="Major")
			axs[1, 0].grid(b=True, which="Minor", linestyle=':')
			cursor10 = mplcursors.cursor(axs[1, 0], multiple=True, bindings={"toggle_visible": "h", "left": "N", "right": "n"})
			cursor10.connect("add",cursor10_annotation)
			
			axs[1, 1].plot(my_data[:,0], my_data[:,plot_titles[3][1]])
			axs[1, 1].set_title(plot_titles[3][0])
			axs[1, 1].set_xlabel(xlabel_str)
			axs[1, 1].set_ylabel("S22 " + ylabel_str)
			axs[1, 1].minorticks_on()
			axs[1, 1].grid(b=True, which="Major")
			axs[1, 1].grid(b=True, which="Minor", linestyle=':')
			cursor11 = mplcursors.cursor(axs[1, 1], multiple=True, bindings={"toggle_visible": "h", "left": "M", "right": "m"})
			cursor11.connect("add",cursor11_annotation)
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
			cursor00 = mplcursors.cursor(axs, multiple=True, bindings={"toggle_visible": "h", "left": "V", "right": "v"})
			cursor00.connect("add",cursor00_annotation)
			#axs.xaxis.set_major_formatter(FormatStrFormatter('%.3e'))
			
		plt.subplots_adjust(wspace=0.2, hspace=0.3)
	else:
		fig = plt.figure()
		fig.canvas.set_window_title("No data to plot")
		
	mng = plt.get_current_fig_manager()
	mng.window.state('zoomed')
	try:
		iconname = "s2p_open_icon.ico"
		mng.window.wm_iconbitmap(sys.argv[0][:-len("s2p_open.pyw")] + iconname)
	except:
		print("Could not load the icon.")
	
	
	plt.show()


