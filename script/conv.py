import sys
if len(sys.argv)<=1:
	print("NO input file given")
	exit()
else:
	lfile=sys.argv[1]
	t=lfile.split(".")
	if len(t)>1:
		t[-2]=t[-2]+"_conv"
		outfile_name=str.join(".",t)
		print("Loading file: "+lfile)
		print("Output file: "+outfile_name)


pen_up = False
i=0
last_z=999

of = open(outfile_name,'w')
of.write("M3S0\r\n")
of.write("G4P0.200\r\n")
of.write("G1F25000\r\n")

with open(lfile) as fin:
	for l in fin:
		if l.find("G21")>=0 or l.find("G91")>=0:
			i+=1
		elif l.find("G1")>=0 or l.find("G0")>=0:
			l_st = l
			if l.find("Z"):
				length = l.find("Z")
				l_st = l[l.find("G"):length]
				l_lo = l[length+1:]

				# check if it is only this number left or if there are further char
				l_z=""
				l_z_f=0.0
				try:
					for ii in l_lo:
						#print("check "+ii)
						if ii=="+" or ii=="." or ii=="-" or (ii>="0" and ii<="9"):
							l_z+=ii
						else:
							l_z_f=float(l_z)
#							print(l)
#							print(str(l_z_f))
							break
				except:
					pass

				
				if last_z!=l_z_f:
					if not(pen_up) and l_z_f>0.0:
#						print("up")
						pen_up = True

						of.write("M3S0\r\n")
						of.write("G4P0.200\r\n")
					elif pen_up and l_z_f<0.0:
#						print("down")
						of.write("")
						pen_up = False

						of.write("M3S200\r\n")
						of.write("G4P0.200\r\n")
					last_z=l_z_f

#			print("in:"+l)
#			print("out:"+l_st)
			of.write(l_st+"\r\n")
		i=i+1
#		if i>10:
#S			break

print(str(i)+" Lines converted")
of.write("G0X0Y0\r\n")
of.close()
