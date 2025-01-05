#!usr/bin/python3

import sys
import matplotlib
import matplotlib.pyplot as plt
import re
import os


def main(input_file):
  
  #define reference position at the alignment and percent identity for each alignment
  ref_pos = []
  percent_id = []
 
  #check if the file is a SAM file, if not print the erorr meesage
  if input_file.endswith('sam'):
    file_name = os.path.basename(input_file)
    match = re.search(r'(\S+)(.sam)',file_name)
    if match:
       xLabel = match.group(1)
  else:
    print("Please input a SAM file")
    sys.exit(1)
  
  #Open the file and for each line split the columns
  for line in open(input_file):
    #if header line ignore and move to the next line
    if line.startswith('@'):
        continue
    col = line.rstrip().split()

    #check if the referene position is 0 which means the read is not aligned, then move to the next iteration
    if col[3] == "0":
       continue
  
    #if the reference postion is positive continue to extract MD line
    else:
       R_pos = col[3]
      
       #In each col line extract the values of MD line, if the value is a digit its a match and if the value is a non digit its a mismatch
       for item in col:
          MD_match = re.search(r'(MD:Z:)([\d+AGTCN\^]+)',item)
          if MD_match:
              MD_value = MD_match.group(2)
              MD_cols = re.findall(r'\d+|[ACGTN\^]+',MD_value)
              if MD_cols:
                matches = 0
                mismatches = 0
                p_id = 0
                total = 0
                for item in MD_cols:
                  if item.isdigit():
                     #sum of matches
                     matches += int(item)
                  else:
                     #number of mismatches
                     mismatches += 1
                total = matches+mismatches
                #Percent identity is matches/total bases * 100
                p_id = round(100 * (matches / total),2)
                #Add reference position and percent identity in two lists
                ref_pos.append(R_pos)
                percent_id.append(p_id)
  
  #Create the Fragment Recruiment Plot
  size = 10
  for x,y in zip(ref_pos,percent_id):
    plt.scatter(x, y, label=f'({x}, {y})',c='green', s=size, edgecolors='none')
  plt.title('Fragment Recruitment Plot for ' + xLabel)
  plt.xlabel("Reference Genome position")
  plt.ylabel("Percent Identity")
  plt.ylim(75,100)
  plt.show()
  

if __name__ == '__main__':
 #check if the command line argument exists 
 try:
    input_file = sys.argv[1] 
 except IndexError:
    print("Please insert an input directory containing SAM files..")
    print("Usage: " + os.path.basename(__file__) + " <input_file>")
    sys.exit(1) #Exit with an error code
    
 main(input_file)          
