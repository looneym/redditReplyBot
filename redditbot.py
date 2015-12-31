import praw
import time


r = praw.Reddit(user_agent = "replybot for comments from users I suspect are from Ireland")
r.login()
print("logging in...")

content_tracker = {}
actioned_comments = []
words_to_match = [" arse ", " feck ", " shite ", " cop on " , " culchie ", " eejit ", \
                  " gaff ", " gammy " , " jackeen ", " langer " , " manky ", " naggin ", \
                  " skanger " , " gobshite " ]
reply_string = "Through sophisticated lexical analysis I have determined that you are from Ireland. Am I correct? \n \
\n \
\n \
----- \
\n \
\n \
^I'm ^a ^bot ^that ^looks ^for ^idiomatically ^Irish ^expressions ^in ^comments ^and ^then ^pokes ^the ^people ^who ^wrote ^them ^to ^see ^if ^my ^hunch ^checks ^out. \
\n \
\n \
^[source](https://github.com/looneym/redditReplyBot)"                 


def runBot(userMode):
    print("Bot running. Mode = " + userMode)
    print("getting subreddit...")
    subreddit = r.get_subreddit("all")
    print("getting comments...")
    comments = subreddit.get_comments(limit=1000)
    print("comments retrieved, begin comparison...")

    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)

        if comment.id in actioned_comments:
            print("bot has re-encountered a previously-actioned comment. ID: " + str(comment.id))

        if comment.id not in actioned_comments and isMatch:
            print("comment found, id = " + str(comment.id))
            content_tracker.update({comment.id:comment.body})
            actioned_comments.append(comment.id)
            print("comment cached")
            if userMode == "live" or userMode =="indefinite":
                comment.reply(reply_string)
                # comment.reply("Through sophisticated lexical analysis I have determined \
                #     that you are from Ireland. Am I correct?")
                print("comment replied to") 

        


    for commentID,commentText in content_tracker.items():
        print("comment id: ")
        print(commentID)
        print("comment text: ")
        print(commentText)
        print("===============================")



def userMenu():
    print("Enter a number to specify which mode to operate in")
    print("1 - Test mode - Any matches found are entered into a cache and printed to the console once all comments have been analysed")
    print("2 - Live mode - Comments are replied to in real time by the bot. Be careful, this can annoy people")
    print("3 - Indefinite mode - Bot will continually fetch and process new comments until it is interrupted")
    choice = input("Enter number: ")
    if int(choice) == 1:
        runBot("test")
    elif int(choice) == 2:
        runBot("live")
    elif int(choice) == 3:
        while True:
            runBot("indefinite")
            time.sleep(10)
            print("restart...")

userMenu()


