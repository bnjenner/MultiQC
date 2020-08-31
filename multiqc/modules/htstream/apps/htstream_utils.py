import json, math
import numpy as np

#################################################

""" Utilities for HTStream submodule """

#################################################

# convert json

def resolve(pairs):

	resolved_dict = {}
	index_dict = {}

	# iterates through json key value pairs
	for k, v in pairs:

		if k in index_dict.keys() and "hts_" in k:
			resolved_dict[k + "_" + str(index_dict[k])] = v
			index_dict[k] += 1

		elif "hts_" in k:
			resolved_dict[k + "_1"] = v
			index_dict[k] = 2

		else:
			resolved_dict[k] = v

	return  resolved_dict


#################################################

# Json and stats parsing functions

def parse_json(name, f):

	app_dict = {}
	apps = json.loads(f)

	try:

		# Allows for multiple instances of app
		for a in apps:
			i = 1
			app_name = a["Program_details"]["program"] + "_" + str(i)

			while app_name in app_dict.keys():
				i += 1
				app_name = a["Program_details"]["program"] + "_" + str(i)

			app_dict[app_name] = a	

	except:

		# Used to parse older json files. Will likely be removed in future.
		app_dict = json.loads(f, object_pairs_hook=resolve)
		log.warning("Sample " + name + " uses old json format. Please update to a newer version of HTStream.")

	return app_dict


#######################################

# prints keys in a pretty way

def key_print(dictionary):

	string = ""

	for key in dictionary.keys():
		string += key + ", "

	string = string[:-2] + "."

	return  string 


#######################################

# sample status div creator

def sample_status(samples):

	# color status dictinoary
	color_dict = {
				  "PASS": {"background": "#c3e6c3", "text": "#196F3D"},
				  "QUESTIONABLE": {"background": "#e6dcc3", "text": "#946A04"},
				  "FAIL": {"background": "#e6c3c3", "text": "#C15F5F"}
				  }

	# wrapper divs
	html = '<div class="hts_status_header" style="display: inline-block; margin-bottom: 8px;">Sample Checks: </div>'
	html += '<div style="display: inline-block;">\n'

	# initilize important variables
	index = 0
	lim = len(samples.keys()) - 1

	for sample, status in samples.items():

		# border radius formatting
		if index == 0:
			if index == lim:
				style = 'border-top-left-radius: 5px; border-bottom-left-radius: 5px; border-top-right-radius: 5px; border-bottom-right-radius: 5px;'
			else:
				style = 'border-top-left-radius: 5px; border-bottom-left-radius: 5px; margin-left: -4px;'
		elif index == lim:
			style = 'border-top-right-radius: 5px; border-bottom-right-radius: 5px; margin-left: -4px;'
		else:
			style = "margin-left: -4px;"

		# background and text colors
		color, text = color_dict[status]["background"], color_dict[status]["text"]

		html += '<div class="htstream_status" style="background-color: {c}; color: {t}; {r}">{s}</div>\n'.format(s=sample, c=color, t=text, r=style)

		index += 1

	# close divs
	html += "</div>\n"
	html += "<br>\n"

	# embed in alert div
	notice = '<div class="alert alert-info">{n}</div>'.format(n = html)	

	return notice


#######################################

# Quality by Base html formatter

def qual_by_cycle_html(read, status_div, line_plot, unique_id, button_list, heatmap, index):

	read_header  = " ".join(read.split("_")[1:3])

	# id of switch buttun, named after read type.
	btn_id = "-".join(read.split("_")[:3]).lower()
	

	# section header
	wrapper_html = '<h4> Quality by Cycle: ' + read_header + '</h4>'

	wrapper_html += status_div 


	line_btn_id = "htstream_qbc_line_{b}_{u}".format(b=btn_id, u=unique_id)
	heat_btn_id = "htstream_qbc_heat_{b}_{u}".format(b=btn_id, u=unique_id)

	wrapper_html += '<div class="btn-group hc_switch_group" style="margin-bottom: 10px;">\n'
	wrapper_html += '<button class="btn btn-default btn-sm active" onclick="htstream_plot_switch(this, \'{t}\')" id="{b}_btn">Linegraph</button>\n'.format(b=line_btn_id, t=heat_btn_id)
	wrapper_html += '<button class="btn btn-default btn-sm " onclick="htstream_plot_switch(this, \'{t}\')" id="{b}_btn">Heatmaps</button></div>\n'.format(b=heat_btn_id, t=line_btn_id)

	# this is where the previous html is added to the wrapper html (two separate divs that can be toggled for each graph)
	# line graph div
	wrapper_html += '<div id="htstream_qbc_line_{b}_{u}" class="htstream_fadein" style="margin-top: -5px;">'.format(b=btn_id, u=unique_id)
	wrapper_html += line_plot + "</div>"

	# The heatmaps of this section occur on a per sample basis, meaning we need another subset of buttons to switch between the samples
	heatmap_html = '<div class="btn-group hc_switch_group" style="margin-bottom: 20px; margin-top: 10px;">\n'

	for buttons in button_list:
		heatmap_html += buttons

	heatmap_html += '</div>\n\n'
	heatmap_html += heatmap

	# heatmap div
	wrapper_html += '<div id="htstream_qbc_heat_{b}_{u}" class="htstream_fadein" style="display:none;">'.format(b=btn_id, u=unique_id)
	wrapper_html += heatmap_html + "</div>"

	final_html = wrapper_html 

	return final_html 


#######################################

# Primers heatmap html formatter

def primers_heatmap_html(unique_id, button_list, heatmap):

	wrapper_html = '<h4> Primer Counts </h4>'
	wrapper_html  += '''<div class="mqc_hcplot_plotgroup">'''
	
	# The heatmaps of this section occur on a per sample basis, meaning we need another subset of buttons to switch between the samples
	heatmap_html = '<div class="btn-group hc_switch_group">\n'

	for buttons in button_list:
		heatmap_html += buttons

	heatmap_html += '</div>\n\n<br></br>\n\n'
	heatmap_html += heatmap

	# heatmap div
	wrapper_html += '<div id="htstream_heat_primers_{u}" class="htstream_fadein">'.format(u=unique_id)
	wrapper_html += heatmap_html + "</div></div>"

	final_html = wrapper_html 

	return final_html 


#######################################

# Quality by Base html formatter

def stats_histogram_html(read, data, unique_id, button_list, notice):


	header_dict = {"PE": "Paried End",
				   "R1": "Read 1",
				   "R2": "Read 2",
				   "SE": "Single End"}


	read_header = header_dict[" ".join(read.split("_")[1:2])]


	html = '<h4>Read Length Histogram: '+ read_header + '</h4>'

	if data != {}:

		html += '''<div class="mqc_hcplot_plotgroup">'''
		html += '<div class="btn-group hc_switch_group">\n'

		for buttons in button_list:
			html += buttons

		html += '</div>\n\n'

		html += '''<div class="hc-plot-wrapper">'''

		data = "["+ json.dumps(data) +"]"

		html += '''<div id="htstream_histogram_{r}_{u}" class="hc-plot"></div></div></div>'''.format(r = read, u = unique_id)
		html += '''<script type="text/javascript" class="htstream_histogram_content_{r}_{u}">{d}</script>'''.format(r = read, u = unique_id, d = data) 

	html += notice

	return html


#######################################

# composition plot

def composition_html(title, table, linegraph, data_type):
	
	# section header
	wrapper_html = title

	table_btn_id = "htstream_comp_table_{b}".format(b=data_type)
	line_btn_id = "htstream_comp_line_{b}".format(b=data_type)

	wrapper_html += '<div class="btn-group hc_switch_group htstream_exempt">\n'
	wrapper_html += '<button class="btn btn-default btn-sm active" onclick="htstream_plot_switch(this, \'{t}\')" id="{b}_btn">Reduction Table</button>\n'.format(b=table_btn_id, t=line_btn_id)
	wrapper_html += '<button class="btn btn-default btn-sm " onclick="htstream_plot_switch(this, \'{t}\')" id="{b}_btn">Composition Line Graph</button></div>\n'.format(b=line_btn_id, t=table_btn_id)
	wrapper_html += "<br></br>"

	# this is where the previous html is added to the wrapper html (two separate divs that can be toggled for each graph)
	# line graph div
	wrapper_html += '<div id="{b}" class="htstream_fadein">'.format(b=table_btn_id)
	wrapper_html += table + "</div>"

	# this is where the previous html is added to the wrapper html (two separate divs that can be toggled for each graph)
	# line graph div
	wrapper_html += '<div id="{b}" class="htstream_fadein" style="display:none;">'.format(b=line_btn_id)
	wrapper_html += linegraph + "</div>"

	final_html = wrapper_html 

	return final_html 


#######################################

# scale overview linegraph plot

def normalize(data, samples_list, stats_order):

	n, m = data.shape # rows, col
	to_delete = []
	raw_data = {}
	factor_dict = {}

	include_list = ["hts_Stats"]

 	# format dictionary for output pca stats (raw data)
	for x in range(len(samples_list)):
		raw_data[samples_list[x]] = dict(zip(stats_order, data[:,x]))



	for x in range(n):

		app = "_".join(stats_order[x].split(": ")[0].split("_")[:-1])
		stat = stats_order[x].split(": ")[-1]
		stat = app + "_" + stat

		row = data[x,:]		

		# remove rows with no variation, also, mean center and normalize variance
		if np.all(row == row[0]) and len(samples_list) > 1:
			to_delete.append(x)
			continue

		elif np.all(row == 0):
			to_delete.append(x)
			continue

		if stat in factor_dict.keys() and app in include_list:
			scale = factor_dict[stat] 

		elif max(row) < 0.1 or max(row) > 1:
			scale = math.floor(-1 * math.log10(max(row)))
			
			if app in include_list:
				factor_dict[stat] = scale

		else:
			continue

		row = row * (10 ** (scale))
		factor = " x 10^" + str(scale)
		stats_order[x] = stats_order[x] + factor

		data[x,:] = row	


	# remove indeterminant columns
	to_delete = sorted(to_delete, reverse=True)
	for x in to_delete:	
		data = np.delete(data, x, 0)
		stats_order.remove(stats_order[x])


	return data, stats_order, raw_data



