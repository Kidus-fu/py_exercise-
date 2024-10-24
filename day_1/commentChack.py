goodComments = ['Stunning 🖤','niggers', 'Looking good 👍', 'Natural beauty 🔥', 'My favorite ❤️', 'I love you', 'Very pretty!', 'So adorable! ❤️', 'Saved to phone', 'Amazing ?', 'Love it!', 'So beautiful ?', 'Mah girl ✨', 'You look fantastic!', 'Absolutely Stunning!', '❤️❤️❤️', '✨✨✨?✨✨✨', 'Looking classy ?', 'Looking great', 'My idol ?', 'Fashion icon','asswhore', 'The best', 'I love so much <3', 'That’s amazing', 'Looking awesome my man!', 'So fabulous', 'Hot girl fall 🔥', 'Looking adorable', 'Why u so fine', 'My G', 'Showing how it’s done!', 'Beautiful pics ❤️', 'What a masterpiece—you and the background', 'Number one 🔥', 'Livin’ that life!', 'Absolute legend', 'Kingship 👑', 'That’s so awesome!', 'You’re awesome!', 'Stoked for you!', 'Epic! 🔥', 'Way to go', 'Big moves 🔥', 'It’s happening!', 'Let’s go!', 'So damn fine', 'Not first, but still commenting', 'Notice me please', 'Did not disappoint', 'You just made a post', 'Welcome to the club', 'You’re perfect', 'Legend brother❤️', 'Your style is impeccable!', 'When u smile, I smile', 'I love that shirt', 'Did you hear they passed a law banning ice cream?', ' Don’t worry, it was ruled un', 'cone', 'stitutional!']
commentCount = 0
for i in goodComments:
    commentCount += 1
badwordes = open("OffensiveWords-CommaSeparated.csv")
badWordsList = []
for i in badwordes:
    badWordsList.append(i.replace("\n",""))
badWordAlp = sorted(badWordsList)
badWordGet = 0
loopIndex = 0
for i in goodComments:
    loopIndex += 1
    for j in badWordsList:
        if i == j:
            badWordGet += 1
            badWordIndex = loopIndex -1
            print(f"I get {badWordGet} in goodcomments index {badWordIndex} value is {goodComments[badWordIndex]}")