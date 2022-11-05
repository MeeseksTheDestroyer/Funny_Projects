import pytesseract
from PIL import ImageGrab, Image
from collections import Counter
import re
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from collections import Counter

class Summ():
    def __init__(self, speech):
        self.speech = speech
        self.text = None
        
    def remove_stop_words(self, text):
        self.text = re.sub('[^a-zA-Z.]', ' ', text)
        self.mapping_sent = dict()
        for i in sent_tokenize(text): self.mapping_sent[i] = None

        return text

    def set_words_rank(self):
        mapping_words = dict()
        words = self.text.split(' ')
        for i in words:
            i = re.sub('[^a-zA-Z]', '', i)
            i = i.lower()
            if i not in mapping_words and i != "" and i!=" ":
                mapping_words[i] = words.count(i)
        return mapping_words
    
    def main(self):
        self.remove_stop_words(self.speech)
        print(self.set_words_rank())
        words_ranking = self.set_words_rank()
        sent_rank = dict()
        for sent in self.mapping_sent: 
            score = 0.0
            words_in_sent = word_tokenize(sent)
            print(words_in_sent)
        
            for i in words_in_sent:
                i = i.lower()
                if(i != "" and i!=" "and i!= "."): score += words_ranking[i]

            sent_rank[sent] = score / len(words_in_sent)
        print(sent_rank)
            

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\PC\Desktop\FunnyProjects\tesseract.exe"



img = ImageGrab.grabclipboard()
speech = pytesseract.image_to_string(img)

s = Summ(speech)
s.main()

img.save('img/clipboard_image.png')







