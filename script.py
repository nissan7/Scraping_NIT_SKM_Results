import find_and_write as fnw 
import re
import mechanize
import os

if not os.path.exists('./result_cse'):
	os.makedirs('./result_cse')
tarurl="http://nitsikkim.ac.in/"
def roll2sem(roll):
	if roll[1:3]=="16":
		return 4
	elif roll[1:3]=="15":
		return 6
	elif roll[1:3]=="14":
		return 8
	else:
		return 0
		

if __name__=='__main__':
	#print semester,department
	sems=['FIRST','SECOND','THIRD','FOURTH','FIFTH','SIXTH','SEVENTH','EIGHTH']
	
	br=mechanize.Browser()
	response=br.open(tarurl)
	
	fil=open("cse.txt","r").read()
	rolls=fil.split("\r\n")
	dept="cse"
	for roll in rolls:
		print "fetching result of "+roll
		if roll !='':
			semcontrol=roll2sem(roll)
		else:
			semcontrol=0
		for i in range(semcontrol):
			temp=br.click_link(text='Results')
			br.open(temp)
			br.select_form(nr=0)
			br.form['roll']=roll
			control=br.form.find_control("year")
			for item in control.items:
				if item.name==sems[i]:
					item.selected=True
			status=br.submit()
			result_html=status.read()			
			fnw.fetch_and_write(result_html,dept)
			br.back()
		





