Technical Aspects:
 - SPEF: Stands for Standard Parasitic Extraction Format
 - its the IEEE standard for representing data of wires of a chip in ASCII format
 - Useful for :
 	- Delay calculation
	- Speed of operation (meeting timing requirements)
	- signal integrity (quality of the signal) 
 - Language: Python

Refrences: (under the refrences folder)
 - 05-Capacitance-Driving-a-Load-2012-13-B
 - 2012_Bookmatter_ProcessVariationsAndProbabilis
 - ISPD_2013_Contest_Details
 - post2spefformat-150920142958-lva1-app6891

How to build:
 - enter the command:
	python <src file> <path to def file> <path to lib file> <path to lef file> <path to spef file to write to>
	example:
	python def2spef "/home/areeg/Desktop/Digital 2/project 2/def2spef/tests/pic27ch/pic27ch.def" "/home/areeg/Desktop/Digital 2/project 2/def2spef/libs/osu018_stdcells.lib" "/home/areeg/Desktop/Digital 2/project 2/def2spef/libs/osu018_stdcells.lef" "/home/areeg/Desktop/Digital 2/project 2/def2spef/tests/pic27ch/pic27ch.spef"

What is done:
 - name_mapping
 - ports
 - D_Nets without calculations

What is missing:
 - Special nets in name mapping and D_nets
 - parsing the routes
 - calculations
