from datetime import date
from os import path
today = date.today()
namefile = today.__str__()+".txt"
textfile = "@startuml\n:Have a good day;\n@enduml"
if path.isfile(namefile):
	print "File is exist"
else:
	fo = open(namefile,"w")
	fo.write(textfile)
	fo.close()
