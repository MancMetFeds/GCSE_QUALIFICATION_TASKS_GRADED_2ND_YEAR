from tkinter import *
import time
from random import randint
from random import shuffle

#WINDOW CONFIG
bg_col = "#FFFFFF"
window = Tk()
window.title("Memory Game")
window.geometry("500x500")
window.configure(background=bg_col)

        #####TASK ONE###
#OPEN AND READ FILE
file = open("words.txt","r")
word_list=[]
for words in file:
    word_list.append(words.strip())
file.close()
print("original word list:", word_list)

        #####TASK TWO:PART ONE###

#DISPLAY WINDOW CONTENTS
title = Label(text="Memory Game", bg="#FFFFFF", width=11)
title.grid(row=1,column=1)
blank = Label(text=" ", bg="#FFFFFF")
blank.grid(row=2,column=1)

wordone = Label(text="word.1", bg="#FFFFFF")
wordone.grid(row=3,column=0)
wordtwo = Label(text="word.2", bg="#FFFFFF")
wordtwo.grid(row=3,column=1)
wordthree = Label(text="word.3", bg="#FFFFFF")
wordthree.grid(row=3,column=2)
wordfour = Label(text="word.4", bg="#FFFFFF")
wordfour.grid(row=4,column=0)
wordfive = Label(text="word.5", bg="#FFFFFF")
wordfive.grid(row=4,column=1)
wordsix = Label(text="word.6", bg="#FFFFFF")
wordsix.grid(row=4,column=2)
wordseven = Label(text="word.7", bg="#FFFFFF")
wordseven.grid(row=5,column=0)
wordeight = Label(text="word.8", bg="#FFFFFF")
wordeight.grid(row=5,column=1)
wordnine = Label(text="word.9", bg="#FFFFFF")
wordnine.grid(row=5,column=2)
blanktwo = Label(text=" ", bg="#FFFFFF")
blanktwo.grid(row=6,column=0)
# SETTINGS        
attempts = [0,0]    #####TASK FIVE###
correctatt= [0]
attempts1=Label(text=(attempts[0]), fg='#000000')
attempts1.grid(row=1, column=9)
attempts2=Label(text=(attempts[1]), fg='#000000')
attempts2.grid(row=1, column=10)
correctatt1=Label(text=correctatt[0], fg='#FFFFFF')
correctatt1.grid(row=0, column=11)

        #######TASK EIGHT#########
def increase_attempts(result):
    if result=="+1":
        correctatt[0]+= 1
        correctatt1.configure(text=correctatt[0])
        if correctatt[0] == 2:
            wordone.destroy()
            wordtwo.destroy()
            wordthree.destroy()
            wordfour.destroy()
            wordfive.destroy()
            wordsix.destroy()
            wordseven.destroy()
            wordeight.destroy()
            wordnine.destroy()
            success=Label(text="SUCCESS", font=30, fg='#00FF00')
            success.grid(row=4, column=1)
        else:
            return

##########TASK FIVE######
    elif result=="-1":
        attempts[0]+=1
        attempts1.configure(text=attempts[0])
        if attempts[0]==3:
            wordone.destroy()
            wordtwo.destroy()
            wordthree.destroy()
            wordfour.destroy()
            wordfive.destroy()
            wordsix.destroy()
            wordseven.destroy()
            wordeight.destroy()
            wordnine.destroy()
            gameover=Label(text="GAMEOVER", font=30, fg='#FF0000')
            gameover.grid(row=4, column=1)
        else:
            return

#######TASK SEVEN#####
    elif result=="/1":
        attempts[1]+=1
        attempts2.configure(text=(attempts[1]))
        if attempts[1]==3:
            wordone.destroy()
            wordtwo.destroy()
            wordthree.destroy()
            wordfour.destroy()
            wordfive.destroy()
            wordsix.destroy()
            wordseven.destroy()
            wordeight.destroy()
            wordnine.destroy()
            gameover=Label(text="GAMEOVER", font=30, fg='#FF0000')
            gameover.grid(row=4, column=1)
        else:
            return
    attempts1.configure(text=" ")
    attempts2.configure(text=" ")


          #####TASK TWO:PART TWO###

def shuffleone(words):
    shuffle (word_list)
    wordone.configure(text=word_list[0])
    wordtwo.configure(text=word_list[1])
    wordthree.configure(text=word_list[2])
    wordfour.configure(text=word_list[3])
    wordfive.configure(text=word_list[4])
    wordsix.configure(text=word_list[5])
    wordseven.configure(text=word_list[6])
    wordeight.configure(text=word_list[7])
    wordnine.configure(text=word_list[8])
    answerone=(word_list[9])
    print('\n',"this is the second answer -->", answerone)


        #####TASK THREE###
    
    #timer -- change loop range to change count down
    for i in range(10,-1,-1):
        i=str(i)
        timertwo=Label(text=" you have "+i+" seconds left")
        timertwo.grid(row=7, column=1)
        time.sleep(1)
        window.update()
    timertwo.configure(text="            Times Up!            " , fg = '#B33A3A' , bg = '#FFFFFF')
    window.update()

    
    file=open("words.txt","r")
    word_list2=[]
    for words in file:
        shuffle(word_list2)
        word_list2.append(words.strip())
    print ('\n',"shuffled list:", word_list2)
    removedword=randint(0,len(word_list2))
    p=9
    reshuffled=(word_list2[p-1])
    for word in reshuffled:
        [word.replace(x,"").strip() for x in word_list2 if reshuffled.startswith(x)]
    wordone.configure(text=word_list2[0])
    wordtwo.configure(text=word_list2[1])
    wordthree.configure(text=word_list2[2])
    wordfour.configure(text=word_list2[3])
    wordfive.configure(text=word_list2[4])
    wordsix.configure(text=word_list2[5])
    wordseven.configure(text=word_list2[6])
    wordeight.configure(text=word_list2[7])
    wordnine.configure(text=word_list2[8])
    window.update()
    answer=(word_list2[9])
    print('\n',"this is the first answer -->", answer)

##########TASK FOUR##########
    blankthree = Label(text=" ", bg="#FFFFFF")
    blankthree.grid(row=8, column=1)
    infoentryone = Label(text="Removed Word: ", bg="#FFFFFF")
    infoentryone.grid(row=9, column=0)
    entryone = Entry()
    entryone.grid(row=9, column=1)
    introentrytwo = Label(text="Replacement Word: ", bg="#FFFFFF")
    introentrytwo.grid(row=10, column=0)
    entrytwo = Entry()
    entrytwo.grid(row=10, column=1)
    buttonone = Button(text='Check', command=lambda: check ("buttonone", entryone, entrytwo, answer, answerone, feedbackone, feedbacktwo), padx=5, pady=5)
    buttonone.grid(row=9,column=2)
    buttontwo = Button(text="Check", command=lambda: check ("buttontwo", entryone, entrytwo, answer, answerone, feedbackone, feedbacktwo), padx=5, pady=5)
    buttontwo.grid(row=10,column=2)
    feedbackone = Label(text=" ", bg="#FFFFFF")
    feedbackone.grid(row=9, column=3)
    feedbacktwo = Label(text=" ", bg="#FFFFFF")
    feedbacktwo.grid(row=10, column=3)
    
            #####TASK FOUR####
def check(identify, entryone, entrytwo, answer, answerone, feedbackone, feedbacktwo):
    if identify == "buttonone":
        print(answer)
        ret = entryone.get()
        if ret.upper()  == (answer.upper()) :
            feedbackone.configure(text="Correct", fg="#00FF00")
            print (ret.upper())
            increase_attempts("+1")
        else:
            feedbackone.configure(text="Incorrect",fg="#FF0000" )
            increase_attempts("-1")
            return

            #####TASK SIX###
    elif identify == "buttontwo":
        ret2= entrytwo.get()
        if ret2.upper()  == (answerone.upper()) :
            feedbacktwo.configure(text="Correct", fg="#00FF00")
            print (ret2.upper())
            increase_attempts("+1")
        else:
            feedbacktwo.configure(text="Incorrect", fg="#FF0000" )
            increase_attempts("/1")
            return


shuffleone(words)
