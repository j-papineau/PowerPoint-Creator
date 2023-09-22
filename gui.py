from tkinter import *
import customtkinter
import csv
import os
from regions import *

# bigvars
regions_from_data = ["region1", "region2"]
regions_children = []

regions_one = []
regions_two = []
regions_three = []

region_buttons = []

selected_region = "None"

# gui funcs

def confirm_button():
    populateRegions(scroll_frame_2)

def region_button(self):
    region_title.configure(text=f'Selected Region: {self}')
    print(self)
    # create comparison using given name
    showResults(self)

def populateRegions(scroll_pane):

    # get region names from data
    regions_one = create_region_objects(range_one.get() + ".csv")
    regions_two = create_region_objects(range_two.get() + ".csv")
    regions_three = create_region_objects(range_three.get() + ".csv")

    if len(region_buttons) > 0:
        for btn in region_buttons:
            btn.destroy()

    for region in regions_one:
        name = region.name
        name_var = customtkinter.StringVar(value=name)
        btn = customtkinter.CTkButton(master=scroll_pane, text=name, command= lambda x=name: region_button(x))
        region_buttons.append(btn)
        btn.pack(pady=10)


def showResults(region_name):
    # enable text boxes
    result_one.configure(state='normal')
    result_two.configure(state='normal')
    # clear text boxes

    # refresh data 

    regions_one = create_region_objects(range_one.get() + ".csv")
    regions_two = create_region_objects(range_two.get() + ".csv")
    regions_three = create_region_objects(range_three.get() + ".csv")

    # find region 
    print(f'comparing {region_name}')

    result_one.delete("0.0", "end")
    result_two.delete("0.0", "end")

    # get results as strings and print

    # print(regions_one)

    compare = Region_Comparison(regions_one[0], regions_two[1])
    testString = compare.toString()

    result_one.insert("0.0", testString)


    # reset text boxes to read only
    result_one.configure(state='disabled')
    result_two.configure(state='disabled')
    



# set theme and color

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# create window
root = customtkinter.CTk()
root.geometry("1080x700")
root.title("Region Comparison App")

# create tab view
tabview = customtkinter.CTkTabview(master=root)
tabview.pack(padx=20, pady=20, fill=BOTH)

tabview.add("Region Comparison")  # add tab at the end
tabview.add("PowerPoint Builder")  # add tab at the end
tabview.set("Region Comparison")  # set currently visible tab



frame = customtkinter.CTkFrame(master=tabview.tab("Region Comparison"), height=600, corner_radius=10)
frame.pack(side='left')

title_font = customtkinter.CTkFont("Arial", 20, weight='bold')
sub_font = customtkinter.CTkFont("Arial", 16)
title = customtkinter.CTkLabel(master=frame, text="Available Data Ranges", font=title_font )
title.pack(pady=10, padx=10)
scroll_frame = customtkinter.CTkScrollableFrame(master=frame, height=400)
scroll_frame.pack()


# display available data ranges
data_ranges = get_data_ranges()

range_one = customtkinter.StringVar(value=data_ranges[0])
range_one_combo_box = customtkinter.CTkComboBox(scroll_frame ,values=data_ranges, variable=range_one)
range_one_label = customtkinter.CTkLabel(scroll_frame, text="Date Range 1", font=sub_font)
range_one_label.pack(pady=10)
range_one_combo_box.pack()

range_two = customtkinter.StringVar(value=data_ranges[0])
range_two_combo_box = customtkinter.CTkComboBox(scroll_frame ,values=data_ranges, variable=range_two)
range_two_label = customtkinter.CTkLabel(scroll_frame, text="Date Range 2", font=sub_font)
range_two_label.pack(pady=10)
range_two_combo_box.pack()

range_three = customtkinter.StringVar(value=data_ranges[0])
range_three_combo_box = customtkinter.CTkComboBox(scroll_frame ,values=data_ranges, variable=range_three)
range_three_label = customtkinter.CTkLabel(scroll_frame, text="Date Range 3", font=sub_font)
range_three_label.pack(pady=10)
range_three_combo_box.pack()




data_ranges_button = customtkinter.CTkButton(master=frame, text="Confirm", command=confirm_button)
data_ranges_button.pack()

# regions from data 
regions_frame = customtkinter.CTkFrame(master=tabview.tab("Region Comparison"))
regions_label = customtkinter.CTkLabel(master=regions_frame, text="Regions for Comparison", font=title_font)
regions_frame.pack(side='left', padx=10)
regions_label.pack(pady=20, padx=10)
scroll_frame_2 = customtkinter.CTkScrollableFrame(master=regions_frame, height=400)
scroll_frame_2.pack(pady=10)

# init results frame

results_frame = customtkinter.CTkFrame(master=tabview.tab("Region Comparison"), height=450, width=400)
results_label = customtkinter.CTkLabel(master=results_frame, text="Results" ,font=title_font)
results_frame.pack(side='left', padx=10)
results_label.pack(pady=8, padx=10)

# results content area probably needs grid
region_title = customtkinter.CTkLabel(master=results_frame, text=f'Region: {selected_region}', font=sub_font)
region_title.pack(pady=10)

results_sub_frame = customtkinter.CTkScrollableFrame(master=results_frame, height=400, width=400)
results_sub_frame.pack()

# metrics we care about Cost, CpC, Leads, Sales, CpL, Close
# set up result frame -- REGION 1

result_one = customtkinter.CTkTextbox(results_sub_frame, state='disabled', width=400)
result_two = customtkinter.CTkTextbox(results_sub_frame, state='disabled', width=400)

result_one.pack(pady=5)
result_two.pack(pady=5)


# create powerpoint


root.mainloop()
