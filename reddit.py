import praw
import config



#Fetch the post information from Reddit and return the text of the post
def get_reddit_post(subreddit):
    reddit = praw.Reddit(
        client_id=config.client_id,
        client_secret=config.client_secret,
        password=config.password,
        user_agent=config.user_agent,
        username=config.username,
    )

    posts = reddit.subreddit(subreddit).top(time_filter="day", limit = 1)
    post = next(posts)
    ##selftext, title
    return [post.title, post.selftext]