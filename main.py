import pytesseract
from PIL import ImageGrab, Image
from collections import Counter
import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from collections import Counter
import nltk
from nltk.corpus import stopwords
import shutil
import os

def get_value(item):
    return item[1]

class Summ():
    def __init__(self, speech):
        self.speech = speech
        self.text = speech
        
    def remove_stop_words(self):
        self.text = re.sub('[^a-zA-Z.0-9,]', ' ', self.text)
        self.text = self.text.lower()
        self.mapping_sent = dict()
        for i in sent_tokenize(self.text): self.mapping_sent[i] = None
       
    def set_words_rank(self):
        mapping_words = dict()
        words = word_tokenize(self.text)
        #print(self.text)

        for i in words:
            i = i.lower()
            if i not in mapping_words and i != "" and i!=" " and i not in stopwords.words('english'):
                mapping_words[i] = words.count(i)
        
        return mapping_words
    
    def main(self):
        self.remove_stop_words()
        words_ranking = self.set_words_rank()
        sent_rank = dict()
        for sent in self.mapping_sent: 
            score = 0.0
            #sent = sent.replace(",", '')
            #sent = re.sub('[^a-zA-Z0-9]', ' ', sent)
            #print(sent)
            words_in_sent = word_tokenize(sent)
            
            for i in words_in_sent:
                i = i.lower()
               
                if(i != "" and i!=" "and i!= "." and i not in stopwords.words('english') and i!=")" and i!="(") and i!=",": score += words_ranking[i]

            sent_rank[sent] = score / len(words_in_sent)
        return sent_rank
            

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\PC\Desktop\FunnyProjects\tesseract.exe"


file = open('speech.txt', mode='r', encoding= 'utf-8')
with file as f:
    speech = f.read()

speech  = 'The tower is 324 meters (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 meters (410 ft) on each side. During its construction, the Eiffel  Tower surpassed the Washington Monument to become the tallest man-made structure  in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 meters.  Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is  now taller than the Chrysler Building by 5.2 meters (17 ft). Excluding transmitters,  the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.'
#img = ImageGrab.grabclipboard()
#speech = pytesseract.image_to_string(img)

s = Summ(speech)
ret = s.main()
final = sorted(ret.items(), key=get_value)
most_important_sent = int(input('How many important sent: '))
os.system('cls' if os.name == 'nt' else 'clear')
print("")
print(f"------------- Your {most_important_sent} most important sent in this text -------------".center(shutil.get_terminal_size().columns), end="\n\n")
for i in range(len(final)-1, len(final) - (most_important_sent + 1), -1): print(final[i][0].capitalize().center(shutil.get_terminal_size().columns), end='\n')
print("\n")

#img.save('img/clipboard_image.png')





