import time

def animate_sentence(word):
  for word in word_list:
    for char in word:
      print(char,end='',flush=True)
      time.sleep(0.2)
    print(" ",end='',flush=True)

word_list=["Welcome","to","the","World","of","Code"]
animate_sentence(word_list)
