from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file); indata = in_file.read() # Colons as well as lines split code

print "The input file is %d bytes long" % len(indata)
print "Ready, hit Return to continue, CTRl-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()