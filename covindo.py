import requests

link = "https://api.kawalcorona.com/indonesia/"
hasil = requests.get(link).json()

for i in hasil:
	print("")
	print("Data Covid Indonesia")
	print("Sumber data	: https://api.kawalcorona.com/indonesia/")
	print("Contact me	: http://bayuputra.my.id | putrabayu0180@gmail.com")
	print("")
	print("+ Negara 	:" +i["name"])
	print("+ Positif	:" +i["positif"])
	print("+ Sembiuh	:" +i["sembuh"])
	print("+ Meninggal	:" +i["meninggal"])
	print("+ Dirawat	:" +i["dirawat"])
