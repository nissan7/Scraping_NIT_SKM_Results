import re
import os

def fetch_and_write(result_html,dept_in):

	re_session=re.compile("<td><b>Session:&nbsp;&nbsp;</b>(.+?)</td>")
	re_name=re.compile("td colspan=2><b>Name:&nbsp;&nbsp;</b>(.+?)</td>")
	re_roll=re.compile("<td><b>Roll No.:&nbsp;&nbsp;</b>(.+?)</td>")
	re_dept=re.compile("<td colspan=2><b>Department:&nbsp;&nbsp;</b>(.+?)</td>")
	re_sem=re.compile("<td><b>Semester:&nbsp;&nbsp;</b>(.+?)</td>")
	re_subres=re.compile("<tr><td class='text-center'>(.+?)</td><td>(.+?)</td><td class='text-center'>(.+?)</td><td class='text-center'>(.+?)</td><td class='text-center'>(.+?)</td></tr>")
	re_tgp=re.compile("<tr><td><b>Total Grade Point (.+?):</b></td><td>(.+?)</td><th colspan=3 class='text-center'>Remarks</th></tr>")
	re_sgpa_passed=re.compile("<tr><td><b>SGPA:</b></td><td>(.+?)</td><td class='text-center' colspan=3>(.+?)</td></tr>")
	re_cgpa=re.compile("<td><b>CGPA:</b></td><td>(.+?)</td>")

	session=re.findall(re_session,result_html)
	name=re.findall(re_name,result_html)
	roll=re.findall(re_roll,result_html)
	dept=re.findall(re_dept,result_html)
	sem=re.findall(re_sem,result_html)
	result=re.findall(re_subres,result_html)
	tgp=re.findall(re_tgp,result_html)
	sgpa_passed=re.findall(re_sgpa_passed,result_html)
	cgpa=re.findall(re_cgpa,result_html)
	
	
	try:
		file=open('result_cse/'+str(name[0])+".txt","a+")
		if len(file.read())==0:
			try:
				file.write("NAME: "+name[0]+"\tROLL NO: "+roll[0]+"\n\nDEPT: "+dept[0]+"\n\n\n")
			except:
				print "unale to write personal details"
	except:
		print "Error in creating/locating directory\ncheck if you have created required directory"
	
	
	
	try:
		file.write("SEMESTER: "+sem[0]+"\tSESSION: "+session[0]+"\n\n\n")
	except:
		print "unable to write sem and session"
	
	try:
		for row in result:
			for col in row:
				file.write(col+" ")
			file.write("\n\n")
	except:
		print "unable to write result details"
	try:
		file.write("TOTAL GRADE POINT: "+tgp[0][1])
	except:
		print "unable to write tgp"
	try:
		file.write("\t\tSGPA: "+sgpa_passed[0][0])
	except:
		print "unable to write sgpa"
	try:
		file.write("\t\tCGPA: "+cgpa[0])
	except:
		print "unable to write cgpa"
	try:
		file.write("\t\tREMARK: "+sgpa_passed[0][1]+"\n\n\n\n")
	except:
		print "unable to write remark"	
			
	
