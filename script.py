import find_and_write as fnw 
import re
import mechanize

tarurl="http://nitsikkim.ac.in/"

if __name__=='__main__':
	depts=['cse','eee','ece','me','ce','bio-tech']
	
	br=mechanize.Browser()
	response=br.open(tarurl)
	
	
	for dept in depts:
		fil=open(dept+".txt","r").read()
		rolls=fil.split("\r\n")
	
		for roll in rolls:
			temp=br.click_link(text='Results')
			br.open(temp)
			br.select_form(nr=0)
			print "fetching result of "+roll
			br.form['roll']=roll
			control=br.form.find_control("year")
			for item in control.items:
				if item.name=="FOURTH":
					item.selected=True
			status=br.submit()
			result_html=status.read()
			
			fnw.fetch_and_write(result_html)
			br.back()
		





