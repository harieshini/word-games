with open ("7_story.txt", "r") as f:
    story=f.read()

words=set()
start= -1
target_start="<"
target_end=">"

for i,char in enumerate(story):
    if char==target_start:
        start=i

    if char==target_end and start!= -1:
        word=story[start:i+1]
        words.add(word)
        start= -1

answers={}

for word in words:
    answer=input("Enter a word for: "+ word + ": ")
    answers[word]=answer

for word in words:
    story=story.replace(word,answers[word])

print(story)
