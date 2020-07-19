from tweepy import Cursor
import tweepy
import time


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

NUMBER_OF_RETWEETERS = 30


class Tweet:
    def __init__(self):
        auth = tweepy.OAuthHandler('consumer_api_key', 'consumer_pass')
        auth.set_access_token('access_token', 'access_token_secret')

        self.api = tweepy.API(auth, wait_on_rate_limit=True,
                              wait_on_rate_limit_notify=True)

    def get_my_followers(self):
        """ returns the list of people i'm following """
        return [follower.name for follower in Cursor(self.api.followers).items()]

    def follow_tweets(self):
        tweets = self.search_tweets()

    def follow_my_followers(self):
        for follower in Cursor(api.followers).items():
            try:
                follower.follow()
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    def follow_retweeters(self):
        people = self.get_retweeters()
        for person in people:
            person.follow()

    def get_retweeters(self):
        tweets = self.search_tweets()
        retweeters = {}
        [retweeters.update({tweet: Cursor(api.retweeters(
            tweet).items(NUMBER_OF_RETWEETERS))}) for tweet in tweets]
        return retweeters

    def retweet_tweets(self):
        """ retweet all tweets in search tuples """
        tweets = self.search_tweets()

        for tweet in tweets:
            try:
                tweet.retweet()
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    def like_tweets(self):
        """ favorite all searched tweets """
        tweets = self.search_tweets()

        for tweet in tweets:
            try:
                tweet.fovorite()
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

    def search_tweets(self):
        """ returns tweets as list """

        # gather search terms
        tweets = []
        for search_term in SEARCH_TERMS.items():
            keyword = search_term[0]
            number_of_tweets = search_term[1]

            # search current keyword in the loop
            for tweet in Cursor(self.api.search(keyword)).items(number_of_tweets):
                tweets.insert(tweet, 0)  # order doesnt matter

        return tweets

    def get_user(self):
        return api.me()

if __name__ == '__main__':
    obj = Tweet()
    obj.like_tweets()
