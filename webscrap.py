#This project is to fetch data from the web 

from urllib.request import urlopen
story = urlopen('https://sixty-north.com/c/t.txt')
story_words =[]
for line in story:
    line_words = line.decode('utf8').split() 
    for word in line_words:
        story_words.append(word)
        
story.close()
print (story_words)
    
