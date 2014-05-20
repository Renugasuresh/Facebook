phonebook={
	"Mohit":13629739,
	"suresh":35758085,
	"parnitha":6457485094,
	"Renuga":4867846495
	"XYZ":4883673777"
	"ABC":3344564555"
	}
phonebook.update({"XYZ"})
phonebook.update("ABC")}
for name,number in phonebook.iteritems():
	print "phone number of %s is %d"%(name,number)
