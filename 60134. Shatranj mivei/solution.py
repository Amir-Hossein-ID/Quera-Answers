def fruits(fl):
	dic = {}
	for f in fl:
		if f['shape'] == "sphere" and f['mass'] <=600 and f["mass"] >=300 and f['volume'] >=100 and f['volume'] <=500:
			try:
				dic[f['name']]+=1
			except:
				dic[f['name']] =1
	return dic
