from collections import OrderedDict
import logging

from multiqc import config
from multiqc.plots import table, bargraph

#################################################

""" QWindowTrim submodule for HTStream charts and graphs """

#################################################

class QWindowTrim():


	def table(self, json, bps, index):

		# Table construction. Taken from MultiQC docs.

		if bps == 0:
			return ""

		headers = OrderedDict()

		headers["Qt_%_BP_Lost" + index] = {'title': "% Bp Lost", 'namespace': "% Bp Lost", 'description': 'Percentage of Input bps (SE and PE) trimmed.',
								   'suffix': '%', 'format': '{:,.2f}', 'scale': 'Greens'}
		headers["Qt_%_R1_BP_Lost" + index] = {'title': "% Bp Lost from R1", 'namespace': "% Bp Lost from R1", 'description': 'Percentage of Input bps (SE and PE) trimmed.',
									  'suffix': '%', 'format': '{:,.2f}', 'scale': 'RdPu'}
		headers["Qt_%_R2_BP_Lost" + index] = {'title': "% Bp Lost from R2", 'namespace': "% Bp Lost from R2", 'description': 'Percentage of Input bps (SE and PE) trimmed.',
									  'suffix': '%', 'format': '{:,.2f}', 'scale': 'Greens'}
		headers["Qt_%_SE_BP_Lost" + index] = {'title': "% Bp Lost from SE", 'namespace': "% Bp Lost from SE", 'description': 'Percentage of Input bps (SE and PE) trimmed.',
									  'suffix': '%', 'format': '{:,.2f}', 'scale': 'RdPu'}
		headers["Qt_Avg_BP_Trimmed" + index] = {'title': "Avg. Bps Trimmed", 'namespace': "Avg. Bpss Trimmed", 'description': 'Average Number of Basepairs Trimmed per Read', 
										'format': '{:,.2f}', 'scale': 'Blues'}
		headers["Qt_%_Discarded" + index] = {'title': "% Discarded",
									 'namespace': "% Discarded",
									 'description': 'Percentage of Reads (SE and PE) Discarded',
									 'suffix': '%',
									 'format': '{:,.2f}',
									 'scale': 'Oranges'
									}
		headers["Qt_Notes" + index] = {'title': "Notes", 'namespace': "Notes", 'description': 'Notes'}

		return table.plot(json, headers)


	def bargraph(self, json, bps):

		# config dict for bar graph
		config = {
				  "title": "HTStream: QWindowTrim Trimmed Basepairs Bargraph",
				  'id': "htstream_qwindowtrimmer_bargraph",
				  'ylab' : "Samples",
				  'cpswitch_c_active': False,
				  'data_labels': [{'name': "Read 1"},
       							 {'name': "Read 2"},
       							 {'name': "Single End"}]
				  }

		if len(json.keys()) > 150:
			html = '<div class="alert alert-info"> Too many samples for bargraph. </div>'	
			return html
			
		html = ""

		r1_data = {}
		r2_data = {}
		se_data = {}

		for key in json:

			r1_data[key] = {"LT_R1": json[key]["Qt_Left_Trimmed_R1"],
						    "RT_R1": json[key]["Qt_Right_Trimmed_R1"]}

			r2_data[key] = {"LT_R2": json[key]["Qt_Left_Trimmed_R2"],
						    "RT_R2": json[key]["Qt_Right_Trimmed_R2"]}

			se_data[key] = {"LT_SE": json[key]["Qt_Left_Trimmed_SE"],
						    "RT_SE": json[key]["Qt_Right_Trimmed_SE"]}

		# returns nothing if no reads were trimmed.
		if bps == 0:
			html = '<div class="alert alert-info"> No basepairs were trimmed from any sample. </div>'	
			return html


		cats = [OrderedDict(), OrderedDict(), OrderedDict()]
		cats[0]["LT_R1"] =   {'name': 'Left Trimmmed'}
		cats[0]["RT_R1"] =  {'name': 'Right Trimmmed'}
		cats[1]["LT_R2"] =   {'name': 'Left Trimmmed'}
		cats[1]["RT_R2"] =  {'name': 'Right Trimmmed'}
		cats[2]["LT_SE"] =   {'name': 'Left Trimmmed'}
		cats[2]["RT_SE"] =  {'name': 'Right Trimmmed'}


		return bargraph.plot([r1_data, r2_data, se_data], cats, config)


	def execute(self, json, index):

		stats_json = OrderedDict()
		overview_dict = {}

		# accumular variable that prevents empty bar graphs
		total_trimmed_bp = 0

		for key in json.keys():

			total_bp_lost = (json[key]["Fragment"]["basepairs_in"] - json[key]["Fragment"]["basepairs_out"]) 

			if total_bp_lost == 0:
				perc_bp_lost = 0
				total_r1 = 0 
				total_r2 = 0
				total_se = 0 

			else:
				perc_bp_lost = ( (json[key]["Fragment"]["basepairs_in"] - json[key]["Fragment"]["basepairs_out"]) / json[key]["Fragment"]["basepairs_in"] ) * 100

				try:
					total_r1 = ( (json[key]["Paired_end"]["Read1"]["basepairs_in"] - json[key]["Paired_end"]["Read1"]["basepairs_out"]) / total_bp_lost ) * 100
					total_r2 = ( (json[key]["Paired_end"]["Read2"]["basepairs_in"] - json[key]["Paired_end"]["Read2"]["basepairs_out"]) / total_bp_lost) * 100
					left_pe_trimmed = json[key]["Paired_end"]["Read1"]["leftTrim"] + json[key]["Paired_end"]["Read2"]["leftTrim"]
					right_pe_trimmed = json[key]["Paired_end"]["Read1"]["rightTrim"] + json[key]["Paired_end"]["Read2"]["rightTrim"]

				except:
					left_pe_trimmed = 0
					right_pe_trimmed = 0
					

				try:
					total_se = ( (json[key]["Single_end"]["basepairs_in"] - json[key]["Single_end"]["basepairs_out"]) / total_bp_lost ) * 100
				except:
					total_se = 0


			# trimmed reads by side
			lefttrimmed_bp = json[key]["Paired_end"]["Read1"]["leftTrim"] + json[key]["Paired_end"]["Read2"]["leftTrim"] + json[key]["Single_end"]["leftTrim"]
			rightrimmed_bp = json[key]["Paired_end"]["Read1"]["rightTrim"] + json[key]["Paired_end"]["Read2"]["rightTrim"] + json[key]["Single_end"]["rightTrim"]

			# total trimmed reads
			trimmed_bp = (lefttrimmed_bp + rightrimmed_bp)

			bp_in = json[key]["Fragment"]["basepairs_in"]

			overview_dict[key] = {
								  "Output_Bp": json[key]["Fragment"]["basepairs_out"],
								  "R1_Bp_Trim_Left": json[key]["Paired_end"]["Read1"]["leftTrim"] / bp_in, 
								  "R1_Bp_Trim_Right": json[key]["Paired_end"]["Read1"]["rightTrim"] / bp_in, 
								  "R2_Bp_Trim_Left": json[key]["Paired_end"]["Read2"]["leftTrim"] / bp_in, 
								  "R2_Bp_Trim_Right": json[key]["Paired_end"]["Read2"]["rightTrim"] / bp_in, 
								  "SE_Bp_Trim_Left": json[key]["Single_end"]["leftTrim"] / bp_in, 
								  "SE_Bp_Trim_Right": json[key]["Single_end"]["rightTrim"] / bp_in, 
								  }

			# sample dictionary entry
			stats_json[key] = {
							   "Qt_%_BP_Lost" + index: perc_bp_lost,
							   "Qt_%_R1_BP_Lost" + index: total_r1,
							   "Qt_%_R2_BP_Lost" + index: total_r2,
							   "Nt_%_SE_BP_Lost" + index: total_se,
							   "Qt_Avg_BP_Trimmed" + index: total_bp_lost / json[key]["Fragment"]["in"],
							   "Qt_Notes" + index: json[key]["Program_details"]["options"]["notes"],
							   "Qt_Left_Trimmed_R1": json[key]["Paired_end"]["Read1"]["leftTrim"],
							   "Qt_Right_Trimmed_R1": json[key]["Paired_end"]["Read1"]["rightTrim"],
							   "Qt_Left_Trimmed_R2": json[key]["Paired_end"]["Read2"]["leftTrim"],
							   "Qt_Right_Trimmed_R2": json[key]["Paired_end"]["Read2"]["rightTrim"],
							   "Qt_Left_Trimmed_SE": json[key]["Single_end"]["leftTrim"],
							   "Qt_Right_Trimmed_SE": json[key]["Single_end"]["rightTrim"]
						 	  }

			# total basepairs accumlation 
			total_trimmed_bp += trimmed_bp


		# sections and figure function calls
		section = {"Table": self.table(stats_json, total_trimmed_bp, index),
				   "Trimmed Basepairs": self.bargraph(stats_json, total_trimmed_bp),
				   "Overview": overview_dict}

		return section
	