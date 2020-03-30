from textblob import TextBlob

file1 = open("words.txt", "r+")
a = file1.read()

print("original text : "+str(a))

b = TextBlob(a)

print("corrected text : "+str(b.correct()))
file1.close()

d = open("words.txt", "w")
d.write(str(b.correct()))
d.close()
