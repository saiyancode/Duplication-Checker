import requests
from bs4 import BeautifulSoup
from random import choice

AgentList = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
             "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/601.6.17 (KHTML, like Gecko) Version/9.1.1 Safari/601.6.17",
             "Mozilla/5.0 (X11; U; Linux x86_64; de; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8",
             "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0"]

# Idea - split all words from the text into a list. Then iterate over each word in each list to check if it's in that list

# Total number of matches/total number of words is a duplication percentage

#compare = ['http://www.canon.co.uk','http://www.canon.de']
compare = [line.rstrip('\n') for line in open('first.txt')]

#compare_2 = ['http://www.canon.ie/','http://www.canon.co.uk']
compare_2 = [line.rstrip('\n') for line in open('second.txt')]

def comparison():
	n = 1
	for a, b in zip(compare, compare_2):
		compare_text = []
		content = []
		userAgent = choice(AgentList)
		headers = {'User-Agent':userAgent}
		response = requests.get(a,headers=headers,timeout=50)
		status = response.status_code
		soup = BeautifulSoup(response.text, 'lxml')
		data = soup.findAll('p')
		for i in data:
			content = i.text
			content = content.split()
			compare_text.append(content)

		compare_text = [j for i in compare_text for j in i]
		compare_text = list(set(compare_text))

	# Now iterate over the like value

		compare_text_2 =[]
		userAgent = choice(AgentList)
		headers = {'User-Agent':userAgent}
		response_2 = requests.get(b,headers=headers,timeout=50)
		status_2 = response_2.status_code
		soup_2 = BeautifulSoup(response_2.text, 'lxml')
		data_2 = soup_2.findAll('p')
		for i in data_2:
			content = i.text
			content = content.split()
			compare_text_2.append(content)
			
		compare_text_2 = [j for i in compare_text_2 for j in i]
		compare_text_2 = list(set(compare_text_2))


		matches = 0
		for c in compare_text:
			for d in compare_text_2:
				#print(str(a)+','+str(b))
				if c == d:
					matches = matches + 1
		try:
			dupe = matches / len(compare_text)
		except:
			dupe = None

		f = open('data2.txt', 'a')
		f.write(str(a) + "," + str(b) + "," + str(matches) + "," + str(dupe)+"\n")

		print("Between " + str(a) +str(status) + " & " + str(b) + " there are " + str(matches) + " exact word matches, this is a duplication value of " + str(dupe))

comparison()


