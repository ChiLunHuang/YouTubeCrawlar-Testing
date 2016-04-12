
#!/usr/bin/python
# -*- coding: utf-8 -*-

#抓音樂  
import requests,shutil 
import pafy
url = "https://www.youtube.com/watch?v=AxhObEpZcp0"  
title=url.strip().split('/watch?v=')[1]
video = pafy.new(url)

print(video.title)
print(video.rating)
print(video.viewcount)
print(video.author)
print(video.length)
print(video.duration) 
print(video.description)

streams = video.streams

#for s in streams:
#    print(s.resolution, s.extension, s.get_filesize(), s.url)


print('Finding video......')
checkmp4=0
for s in streams:
    if checkmp4!=1 :
        if ('1280x720') in str(s) and ('mp4') in str(s):
            print('Got result 1280x720')
            print(s)
            print(s.url)
            res=requests.get(s.url,stream=True)
            with open('D://{}.mp4'.format(title),'wb') as f:
                shutil.copyfileobj(res.raw,f)
            print('Mission complete')
            checkmp4=1
        elif ('640x360') in str(s) and ('mp4') in str(s):
            print('Got result 640x360')
            print(s)
            print(s.url)
            res=requests.get(s.url,stream=True)
            with open('D://{}.mp4'.format(title),'wb') as f:
                shutil.copyfileobj(res.raw,f)
            print('Mission complete')
            checkmp4=1

        else:
            print('Mission complete:not found')
            #for s in streams:
            #    print(s.resolution, s.extension)
            
     
