#-*- coding:utf-8 -*-
import tweepy
from django.core.management.base import BaseCommand

# class Command(BaseCommand):
#   def handle(self, *args, **options):
auth = tweepy.OAuthHandler('your Consumer API key', 'your Consumer API secret key')
auth.set_access_token('your Access token', 'your Access token secret')
api = tweepy.API(auth)

#ユーザプロフィール取得
# try :
profile = api.get_user(id='uyun125')

print ('表示名: ', profile.name) #表示名
print ('アカウント名: ', profile.screen_name) #アカウント名 @*
print ('画像URL: ', profile.profile_image_url) #アイコン画像のURL
print ('ツイート数: ', profile.statuses_count) #ツイート数
print ('フォロー数: ', profile.friends_count) #フォロー数
print ('フォロワー数: ', profile.followers_count) #フォロワー数
    # except tweepy.error.TweepError, e:
      # print (e.message)

    #タイムライン取得（最新10件）
    # try :
    #   for tweet in tweepy.Cursor(api.user_timeline, id='user name').items(10):
    #     print (tweet.id) #id
    #     print (tweet.text) #本文
    # except tweepy.error.TweepError, e:
    #   print (e.message)
