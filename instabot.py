from instagrapi import Client
import random
import getpass
try:
    name=input('Enter your username')
    password=getpass.getpass('Enter your password and click enter to continue')
    print('Starting bot automation....')
    client=Client()
    client.login(name,password)

    comments=['Awesome','Nice','Great']
    hashtag='programming'
    medias=client.hashtag_medias_recent(hashtag,20)
    for i,media in enumerate(medias):
        client.media_like(media.id)
        if i%5==0:
            client.user_follow(media.user.pk)
            reply=random.choice(comments)
            client.media_comment(media.id,reply)

except :
    print('Stopping bot...')
