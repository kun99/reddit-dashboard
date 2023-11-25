import asyncpraw
import asyncio
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

reddit = asyncpraw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("SECRET"),
    user_agent="windows:reddit-dash:1.0.0",
)

@app.get("/subreddit/{subreddit}")
async def get_subreddit_posts(subreddit):
    fetched_posts = []
    subreddit = reddit.subreddit(subreddit).hot(limit=10)
    for submission in subreddit:
        json_file = {
        'title': submission.title,
        'upvotes': str(submission.score),
        'url': "https://www.reddit.com" + submission.permalink
        }
        fetched_posts.append(json_file)
    return {"posts": fetched_posts}

@app.get("/subreddits/{subreddits}")
async def get_subreddit_posts(subreddits):
    subs = subreddits.split("+")
    subs.pop()
    #for every subreddit, create a task to get submissions from it
    tasks =[]
    for subreddit in subs:
        tasks.append(fetch_submissions(subreddit))
    results = await asyncio.gather(*tasks)
    return {"subreddits": results}

async def fetch_submissions(subreddit):
    subreddit = await reddit.subreddit(subreddit)
    fetched_posts = []
    #just retrieving submissions from the subreddit
    async for submission in subreddit.hot(limit=10):
        json_file = {
            'title': submission.title,
            'upvotes': str(submission.score),
            'url': "https://www.reddit.com" + submission.permalink,
            'image': submission.url
        }
        fetched_posts.append(json_file)
    return fetched_posts

# @app.get("/subreddits/{subreddits}")
# async def get_subreddit_posts(subreddits):
#     fetched_subreddits = []
#     subreddit = reddit.subreddit(subreddits).hot(limit=10)
#     for submission in subreddit:
#         json_file = {
#             'title': submission.title,
#             'upvotes': str(submission.score),
#             'url': "https://www.reddit.com" + submission.permalink,
#             'image': submission.url
#         }
#         fetched_subreddits.append(json_file)
#     print(fetched_subreddits)
#     return {"subreddits": fetched_subreddits}