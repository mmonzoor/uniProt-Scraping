import sys
print(sys.version)
#ensure python3
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import pandas as pd 

#open downloaded fasta file from sequence
fasta = open("a2_fast.txt", "r")

def parsing(fasta):
	seqs = []
	for line in fasta: 
		for i in line:
			if i[0] == ">":
				seqs.append(line)
	return seqs

def params(): 
	
	p_name = []
	params.accession = []
	species = []

	for i in parsing(fasta): 
		pipe_break = i.split('|')
		params.accession.append(pipe_break[1])
		#print(pipe_break)
		protein = pipe_break[2].split('=')
		#print(protein)
		
		species.append(protein[1][:-3])
		#print(species)
		
		p_name.append(protein[0][:-2])
	
	d = {'protein_name':p_name, 'accession_#':params.accession, 'species': species, 'function':function()}
	return d

def function():
	
	''' scrape UniProt site for function '''
	function = []
		
		#print('http://www.uniprot.org/uniprot/' + i)
	try:
		for i in params.accession: 
			html = urlopen('http://www.uniprot.org/uniprot/' + i)
		
			bsObj = BeautifulSoup(html, 'html.parser')
			inner_f = []
			for item in bsObj.findAll("div", attrs={"class": "annotation"}):

				field = item.find("span", attrs={"property":"schema:text"})
				inner_f.append(field)
				#print(field)
			function.append(inner_f)
		#print(function[3])
		print(len(function))

		return function

	except urllib.error.HTTPError as err: 
		print('network error!')

def main():

	df = pd.DataFrame(data=params()).to_csv('table_q1', index=False)
	return df

if __name__ == '__main__':
	main()

fasta.close()
