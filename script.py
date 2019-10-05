import find_and_write as fnw 
import re
import mechanize
import os


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
	#semester=input("choose the semester\n0-All\n1-FIRST\n2-SECOND\n3-THIRD\n4-FOURTH\n5-FIFTH\n6-SIXTH\n7-SEVENTH\nEIGHTH\n")
	#department=input("choose the dept\n0-All\n1-cse\n2-eee\n3-ece\n4-me\n5ce\n6-bio-tech")
	
	#print semester,department
	depts=['cse','eee','ece','me','ce','bio-tech']
	sems=['FIRST','SECOND','THIRD','FOURTH','FIFTH','SIXTH','SEVENTH','EIGHTH']
	batches=['batch15','batch16','batch14']
	
	for dept in depts:
		for batch in batches:
			path='./result/'+dept+'/'+batch+'/'
			if not os.path.exists(path):
				os.makedirs(path)
	
	br=mechanize.Browser()
	response=br.open(tarurl)
	
	if 1:
		for dept in depts:
			fil=open(dept+".txt","r").read()
			rolls=fil.split("\r\n")
		
			for roll in rolls:
				
				if roll !='':
					print "On"+roll
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
		





