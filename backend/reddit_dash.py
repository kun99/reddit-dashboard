import praw
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("SECRET"),
    user_agent="windows:reddit-dash:1.0.0",
)

@app.get("/subreddit/{subreddit}")
async def get_subreddit_posts(subreddit):
    fetched_posts = []
    subreddit = reddit.subreddit(subreddit).hot(limit=10)
    print(subreddit)
    for submission in subreddit:
        json_file = {
        'title': submission.title,
        'upvotes': str(submission.score),
        'url': "https://www.reddit.com" + submission.permalink
        }
        fetched_posts.append(json_file)
    print(fetched_posts)
    return {"posts": fetched_posts}


@app.get("/subreddits/{subreddits}")
async def get_subreddit_posts(subreddits):
    fetched_subreddits = []
    subs = subreddits.split(",")
    for subreddit in subs:
        fetched_posts = []
        subreddit = reddit.subreddit(subreddit).hot(limit=10)
        for submission in subreddit:
            json_file = {
            'title': submission.title,
            'upvotes': str(submission.score),
            'url': "https://www.reddit.com" + submission.permalink
            }
            fetched_posts.append(json_file)
        fetched_subreddits.append(fetched_posts)
    print(fetched_subreddits)
    return {"subreddits": fetched_subreddits}