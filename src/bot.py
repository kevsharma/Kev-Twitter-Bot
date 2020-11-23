import tweepy

# Setting up the authentication and linking account.
auth = tweepy.OAuthHandler("wughahxX55YCnvHJfsIT4ilaG", "B2hmBpTvydj9MMXg9O8ZwjURCSpICzRsZCfPjuRluztLaSJQaL")
auth.set_access_token("1329514293310726144-2gcsKAopFLJX8peU73zDckqUTmsKvf", "eSXFwjWJttwrTbaDtrdN3veXZ9FOhkdp75170cydq4xGD")
api = tweepy.API(auth)

# Printing friends <- This was taken from the introductory documentation.
user = api.get_user("Bot3Hangman")
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
    print(friend.screen_name)

# Making a sample tweet


# 