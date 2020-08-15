# Simple Twitter Bot [FUN PROJECT]

## Usage

```py
    obj = Tweet()
    obj.like_tweets()
```

## Search Keywords

Search keywords are key-value paired, where keys refer to the search terms and the values are the number of tweets to return in correspondance with the search term.

Configure your desired search terms, the default are:

```py
SEARCH_TERMS = {
    'Javascript': 200,
    'Python Programming': 300,
    'TedXTalk': 20,
    'SSH': 10,
    'Cats': 100,
    'SQL': 20,
    'CSS': 50,
    'HTML5': 30,
    'Django': 100,
    'Love': 20,
    'Politics': 5
}
```

# Methods defined

```search_tweets``` returns list of tweets based on the keywords defined i ``` SEARCH_TERMS ```
```py
def search_tweets(self):
```

returns ```list``` of followers
```py
def get_my_followers(self):
```

```py
def follow_tweets(self):
```

```py
def follow_my_followers(self):
```

```py
def follow_retweeters(self):
```


```py
def get_retweeters(self):
```


```py
def retweet_tweets(self):
```

```py
def like_tweets(self):
```
