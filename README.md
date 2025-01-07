This script generates a Fragment Recruitment Plot

The input file has to be in the format of a SAM file with .sam extention, an output of Bowtie2 alignmnent. The program parses the content of the SAM file, specifically the reference genome position at alignment and MD line, and produces a fragment recruitment plot with reference genome position as x-axis and percent identity as y-axis.The reference genome name is given as the title of the plot. If the input file, proper file extention or the format is not followed the program will exit and provide the necessary command.  
