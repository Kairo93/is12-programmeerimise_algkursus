from time import gmtime, strftime

news = {}

def add_item():
	global news
	
	title = raw_input("Pealkiri: ")
	content = raw_input("Sisu: ")
	author = raw_input("Autor: ")
	
	id = len(news)
	
	if id in news:
		id = news.keys()[-1]+1
	
	news[id] = {'title': title, 'content': content, 'author': author}
		
def remove_item():
	number = int(raw_input("Kirje number: "))	
	
	del news[number]
	
def list_items():

	print '{0:<10}'.format('#'),
	
	for heading in news.values()[-1].keys():
		print '{0:>10}'.format(heading),
	
	print "\n"
	
	for counter in news:
				
		print '{0:<10}'.format(counter),
		
		for item in news[counter].values():
			print '{0:>10}'.format(item),
		
		print

def edit_item():
	id = int(raw_input("ID: "))
	key = raw_input("Key: ")
	value = raw_input("Value: ")
	
	edit = news[id]
	edit[key] = value

while True:
	command = raw_input('\n\nSisesta "UUS" uue kirje jaoks\nSisesta "KUSTUTA" kirje kustutamiseks\nSisesta "VAATA" kirjete vaatamiseks\nSisesta "MUUDA" kirjete muutmiseks\n\n')
	
	if command.lower() == 'uus':
		add_item()
	if command.lower() == 'vaata':
		list_items()
	if command.lower() == 'kustuta':
		remove_item()
	if command.lower() == 'muuda':
		edit_item()		
	if command.lower() == 'end':
		break
