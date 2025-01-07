# fragment_recruitment_plotter

This script generates a Fragment Recruitment Plot

The input file has to be in the format of a SAM file with .sam extension, an output of Bowtie2 alignmnent. The program parses the content of the SAM file, focusing specifically on the reference genome position at alignment and the MD line, and generates a fragment recruitment plot with reference genome position as x-axis and percent identity as y-axis.The reference genome name is given as the title of the plot. If the input file, the file extension or the file format is not followed properly, the program will exit and provide the necessary command.  
