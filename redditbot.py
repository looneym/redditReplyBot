import praw
import time



r = praw.Reddit(user_agent = "replybot for comments from users I suspect are from Ireland")
r.login()
print("logging in...")

comment_cache = []
words_to_match = ["arse", "feck", "shite"]


def runBot():
    print("getting subreddit...")
    subreddit = r.get_subreddit("test")
    print("getting comments...")
    comments = subreddit.get_comments(limit=1000)
    print("comments retrieved, begin comparison...")

    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if comment.id not in comment_cache and isMatch:
            print("comment found, id = " + str(comment.id))
            comment.reply("Through sophisticated lexical analysis I have determined that you are from Ireland. Am I correct?")
            comment_cache.append(comment.id)
            print("comment replied to and cached")

while True:
    runBot()
    time.sleep(10)            



