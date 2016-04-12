
# YouTubeCrawlar-Testing: Using requests, shutil and pafy.
# 2016-04-12, by ChiLun, Huang.

# A Crawler for YouTube Videos .
import requests,shutil 
import pafy

# Set the url and use pafy to find information from YouTube.
# There are lots of information can retrieve such as the title, rating and viewcount of the video .
# see more about Pafy (http://pythonhosted.org/Pafy/).

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

# video.streams can find the real url direction of the video.

streams = video.streams

#for s in streams:
#    print(s.resolution, s.extension, s.get_filesize(), s.url)

# If i want to search and download video and its format is mp4, i can choose the result i want by information from streams.
# requests is for getting webpage data and declare that is a stream.
# shutil.copyfileobj(res.raw,f) can get a content of copy. See more (https://docs.python.org/3/library/shutil.html) 
print('Finding video......')
checkmp4=0
for s in streams:
    if checkmp4!=1 :
        #1280x720 mp4
        if ('1280x720') in str(s) and ('mp4') in str(s):
            print('Got result 1280x720')
            #print(s)
            #print(s.url)
            res=requests.get(s.url,stream=True)
            with open('D://{}.mp4'.format(title),'wb') as f:
                shutil.copyfileobj(res.raw,f)
            print('Mission complete(1280x720)')
            checkmp4=1
        #640x360 mp4
        elif ('640x360') in str(s) and ('mp4') in str(s):
            print('Got result 640x360')
            #print(s)
            #print(s.url)
            res=requests.get(s.url,stream=True)
            with open('D://{}.mp4'.format(title),'wb') as f:
                shutil.copyfileobj(res.raw,f)
            print('Mission complete(640x360)')
            checkmp4=1

        else:
            print('Mission complete: Not found')
# Once the video get, the file will be closed.            
f.close()            
     
