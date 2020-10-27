import time
from os import system
from random import randint, shuffle, randrange, sample
import json 
import uuid
from app.data import *



def random_sentence():
    """

    This method will return a random sentence

    """

    num = randrange(0,5)
    return nouns[num] + ' is ' + adv[num] + ' ' + adj[num] + " "


def generate_sentence():
    """

    This will generate a new sentence

    """

    final_tweet = random_sentence()

    tweet_words = str(uuid.uuid4()).split("-")
    shuffle(tweets_hashtags)
    shuffle(tweet_words)
    for i in range(3):
        if i%2 == 0:
            final_tweet += tweet_words[i] + " " + tweets_hashtags[i] + " "
        else:
            final_tweet += tweets_hashtags[i] + " " + tweet_words[i] + " "

    return final_tweet


def send_tweet():
    """

    This will just cURL using the system of os lib in python
    All parameters are in the format

    """

    with open("./accounts.json", "r") as filek:
        accounts = json.loads(filek.read())
        for a in accounts:

            system("curl 'https://mobile.twitter.com/i/api/1.1/statuses/update.json' \
            -H 'authority: mobile.twitter.com' \
            -H 'pragma: no-cache' \
            -H 'cache-control: no-cache' \
            -H 'authorization: {}' \
            -H 'x-twitter-client-language: en' \
            -H 'x-csrf-token: {}' \
            -H 'x-twitter-auth-type: OAuth2Session' \
            -H 'x-twitter-active-user: yes' \
            -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' \
            -H 'content-type: application/x-www-form-urlencoded' \
            -H 'accept: */*' \
            -H 'origin: https://mobile.twitter.com' \
            -H 'sec-fetch-site: same-origin' \
            -H 'sec-fetch-mode: cors' \
            -H 'sec-fetch-dest: empty' \
            -H 'referer: https://mobile.twitter.com/compose/tweet' \
            -H 'accept-language: en-US,en;q=0.9' \
            -H 'cookie: {}' \
            --data-raw 'include_profile_interstitial_type=1&include_blocking=1&include_blocked_by=1&include_followed_by=1&include_want_retweets=1&include_mute_edge=1&include_can_dm=1&include_can_media_tag=1&skip_status=1&cards_platform=Web-12&include_cards=1&include_ext_alt_text=true&include_quote_count=true&include_reply_count=1&tweet_mode=extended&simple_quoted_tweet=true&trim_user=false&include_ext_media_color=true&include_ext_media_availability=true&auto_populate_reply_metadata=false&batch_mode=off&status={} {}' \
            --compressed > out.json".format(a["authorization"], a["x_csrf_token"], a["cookie"], generate_sentence(), str(randint(0, 99999999999))) )
            
            time.sleep(1)


def test_json():
    """

    Just a function to test the validity of a json file

    """

    try:
        print(json.loads(open("./out.json")))
    except Exception as es:
        print(es)
        return False
    
    return True


def proceed():
    """

    Per round, what it is done

    """

    send_tweet()
    # We check if the limit have been reach
    with open("./out.json", "r") as filek:
        if "errors" in filek.read() :
            print("\n--- LIMIT REACHED ---")
            print("\n--- WAITING FOR 1HOURS ---")
            time.sleep(3600)
        else:
            # we choose a random waiting range from 5s to 35s
            time.sleep(randint(10, 35))
    print("\n---------------------")
