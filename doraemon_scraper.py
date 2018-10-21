# This Scrapes Doraemon RAW Manga using BeautifulSoup

from bs4 import BeautifulSoup
import requests
import os

url = "https://doraemon.mangawiki.org/read-manga/index.php?manga=Doraemon-Manga-Raw&chapter=Doraemon_Vol_01_RAW&page="
i = 1
img_url = []

while True:
	try:
		r = requests.get(url + str(i))
		i += 1
		data = r.text
		soup = BeautifulSoup(data, "lxml")

		manga_found = False

		for link in soup.find_all('img'):
			image = link.get("src")
			img_url = "http://doraemon.mangawiki.org/read-manga/" + image 
				
			if 'mangas' in img_url:
				manga_found = True
				img_name = os.path.split(img_url)[1]
	
				#Replace the text in the quotes with the path of your choice in the next 3 lines

				img_name = os.path.join('c:/Users/sarth/Documents/Manga/ドラえもん', img_name) 
				if not os.path.exists('c:/Users/sarth/Documents/Manga/ドラえもん'):
					os.makedirs('c:/Users/sarth/Documents/Manga/ドラえもん')

				r2 = requests.get(img_url)
				
				with open(img_name, 'wb') as f:
					f.write(r2.content)
					
		if manga_found == False:
			print ("That's all!")
			break

	except:
 		print("There You Go!")
 		break

 	
