# YouTubeVideoCrawlar Example
This project is an example for videos downloading from YouTube on Python 3 by requests, shutil and pafy 


We can use three packages(requests, shutil and pafy) to download the YouTube video.


## pafy Introduction

[pafy](http://pythonhosted.org/Pafy/) provide a simple way to get information of YouTube video such as title, viewcount, author and rating.

There is a example down  below.

```python

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
```

Because you can't directly click right mouse button to download the video on YouTube website, we have to find the real direction of url by `video.streams`.


```python
streams = video.streams

#for s in streams:
#    print(s.resolution, s.extension, s.get_filesize(), s.url)
```

## To get web content by using requests.

After finding real url by pyfy, we can use `requests` to get the web content.

> Use stream=True  

```python
res=requests.get(s.url,stream=True)
````

## Download the video you want by shutil.

> get more information from [Python Documentation](https://docs.python.org/3/library/shutil.html)

```python
with open('D://{}.mp4'.format(title),'wb') as f:
  shutil.copyfileobj(res.raw,f)
```

## Try it. 

>[Example](https://github.com/ChiLunHuang/YouTubeVideoCrawlar-Example/blob/master/sample.py)

