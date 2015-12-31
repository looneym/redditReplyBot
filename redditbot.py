import praw
import time


r = praw.Reddit(user_agent = "replybot for comments from users I suspect are from Ireland")
r.login()
print("logging in...")

comment_cache = {}
words_to_match = [" arse ", " feck ", " shite ", " cop on " , " culchie ", "eejit ", \
                  " gaff ", " gammy " , " jackeen ", " langer " , " manky ", " naggin ", \
                  " skanger " , " gobshite " ]


def runBot(mode):
    print("getting subreddit...")
    subreddit = r.get_subreddit("ireland")
    print("getting comments...")
    comments = subreddit.get_comments(limit=1000)
    print("comments retrieved, begin comparison...")

    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in comment_cache and isMatch:
            print("comment found, id = " + str(comment.id))
            comment_cache.update({comment.id:comment.body})
            print("comment cached")
            if mode == live:
                comment.reply("Through sophisticated lexical analysis I have determined \
                    that you are from Ireland. Am I correct?")
                print("comment replied to")
            

    for commentID,commentText in comment_cache.items():
        print("comment id: ")
        print(commentID)
        print("comment text: ")
        print(commentText)
        print("========================================================")       

def userMenu():
    print("Enter a number to specify which mode to operate in")
    print("1 - Test mode - Any matches found are entered into a cache and printed \
          the console once all comments have been analysed")
    print("2 - 'Live mode' - Comments are replied to in real time by the bot. \
          Be careful, this can annoy people")
    choice = input("Enter number: ")
    if choice == 1:
        runBot("test")
    elif choice == 2:
        runBot("live")

userMenu()



