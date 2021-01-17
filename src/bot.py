from datetime import date
from datetime import timedelta
import time
from time import sleep
import tweepy
import holidays
import os
from os import environ

# Secure api keys
auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('ACCESS_TOKEN'), os.environ.get('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)

# Aggregate holidays around the world into allHolidays
allHolidays = holidays.AR() + holidays.AU() + holidays.AT() + holidays.BE()
allHolidays = allHolidays + holidays.CA() + holidays.CO() + holidays.CZ() + holidays.DK()
allHolidays = allHolidays + holidays.FI() + holidays.FRA() + holidays.DE() + holidays.HU()
allHolidays = allHolidays + holidays.IT() + holidays.JP() + holidays.MX() + holidays.NL()
allHolidays = allHolidays + holidays.NZ() + holidays.PL() + holidays.PT()
allHolidays = allHolidays + holidays.PTE()+ holidays.SI() + holidays.SK() + holidays.ZA()
allHolidays = allHolidays + holidays.ES() + holidays.CH() + holidays.UK() + holidays.US()

# Get the appropriate tweet for the day.
def initializeTweet(today):
    isTodayHoliday = today in allHolidays
    if(isTodayHoliday == False):
        tweet = "Unfortunately, today isn't a holiday."
    else:
        tweet = "Today is " + str(allHolidays.get(today)) + "!"

    return tweet


#temp = date.today()
while(True):
    tweet = initializeTweet(date.today())
    api.update_status(tweet)
    #print(str(temp) + " -> " + str(tweet))
    #temp = temp + timedelta(days=1)
    time.sleep(60 * 60 * 24)
    