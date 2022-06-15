import tweepy
from urllib import request
from datetime import date

# 認証
auth = tweepy.OAuthHandler('自身のコンシューマーキー', '自身のコンシューマーシークレット')
auth.set_access_token('自身のアクセストークンキー', '自身のアクセストークンシークレット')
api = tweepy.API(auth)

#IDlog.txtから最後に読み込んだツイートのidを得る
def get_SinceId():
    with open('IDlog.txt', 'r') as f:
        since_id = f.read()
    return int(since_id)

# 読み込んだidをIDlog.txtに書き込む
def store_latestId(tweets):
    with open('IDlog.txt', 'w') as f:
        str_latest_id = str(tweets[0].id)
        f.write(str_latest_id)

# 画像のurlを得る
def get_urls(tweets):
    for i in range(len(tweets)):
        if(hasattr(tweets[i], 'extended_entities')):
            media = tweets[i].extended_entities['media']
            for j in range(len(media)):
                urls.append(media[j]['media_url_https'])

# Acquired_Imagesフォルダに特定の命名規則で画像ファイルを格納する
def create_imagefile(tweets, urls):
    today = date.today()
    file_name = 'Acquired_Images/{0}-{1}-{2}_{3}.jpg'
    get_urls(tweets)
    for i in range(len(urls)):
        image = request.urlopen(urls[i])
        with open(file_name.format(today.year-2020, today.month, today.day, i+1), mode='wb') as f:
            f.write(image.read())
        image.close()


#main部分
user_id = 'XXX' #画像を取得するアカウントのユーザーid
tweets = api.user_timeline(user_id, since_id=get_SinceId(), tweet_mode='extended')
urls = []

# ツイートの更新がある場合のみ画像取得を試みる
if(len(tweets) != 0):
    store_latestId(tweets)
    create_imagefile(tweets, urls)
