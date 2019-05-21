# Conversion Tool from DEF Format to SPEF format

## Technical Aspects:
 - SPEF: Stands for Standard Parasitic Extraction Format
 - its the IEEE standard for representing data of wires of a chip in ASCII format
 - Useful for :
 	- Delay calculation
	- Speed of operation (meeting timing requirements)
	- signal integrity (quality of the signal) 
 - Language: Python

## Refrences: (under the refrences folder)
 - Lecture 06 - Capacitance, Driving a Load-2011-12-B
 - Process Variations And Probabilis, Standard Formats for Circuit Characterization
 - ISPD 2013 Contest Details
 - SPEF Format
 - LEF/DEF Language Reference

## How to build and install:
 - enter the command:
 		
		python [src file] [path to def file] [path to lib file] [path to lef file] [path to spef file to write to]

## example usage:
		python def2spef "/home/areeg/Desktop/Digital 2/project 2/def2spef/tests/pic27ch/pic27ch.def" "/home/areeg/Desktop
		/Digital 2/project 2/def2spef/libs/osu018_stdcells.lib" "/home/areeg/Desktop/Digital 2/project 2/def2spe
		/libs/osu018_stdcells.lef" "/home/areeg/Desktop/Digital 2/project 2/def2spef/tests/pic27ch/pic27ch.spef"
	
## What is done:
 - name_mapping
 - ports
 - D_Nets without calculations
 - Wire Segments
 - Capacitance Calculations
 - Resistance Calculations
