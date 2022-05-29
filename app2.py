from pytube import YouTube

pritam = YouTube("https://www.youtube.com/watch?v=rUWxSEwctFU")

# pritam.streams


# print(dir(pritam.streams))
'''

['__abstractmethods__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '_abc_impl', '_filter', 'all', 'asc', 'count', 'desc', 'filter', 'first', 'fmt_streams', 'get_audio_only', 'get_by_itag', 'get_by_resolution', 'get_highest_resolution', 'get_lowest_resolution', 'index', 'itag_index', 'last', 'order_by', 'otf']


'''

# print(pritam.streams)
i = 1
for item in pritam.streams:
    print(i)
    print(item.itag)
    print(pritam.streams.get_by_itag(item.itag).filesize)
    print(item.mime_type)
    res = item.resolution
    if res == None:
        res = item.abr
    print(res)
    # print(item.type)
    i += 1

'''
[<Stream: itag="17" mime_type="video/3gpp" res="144p" fps="6fps" vcodec="mp4v.20.3" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="18" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="22" mime_type="video/mp4" 
res="720p" fps="25fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="313" mime_type="video/webm" res="2160p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="401" mime_type="video/mp4" res="2160p" fps="25fps" vcodec="av01.0.12M.08" progressive="False" type="video">, <Stream: itag="271" mime_type="video/webm" res="1440p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="400" mime_type="video/mp4" res="1440p" fps="25fps" vcodec="av01.0.12M.08" progressive="False" type="video">, <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="25fps" vcodec="avc1.640028" progressive="False" type="video">, <Stream: itag="248" mime_type="video/webm" res="1080p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="399" mime_type="video/mp4" res="1080p" fps="25fps" vcodec="av01.0.08M.08" progressive="False" type="video">, <Stream: itag="136" mime_type="video/mp4" res="720p" fps="25fps" vcodec="avc1.4d401f" progressive="False" type="video">, <Stream: itag="247" mime_type="video/webm" res="720p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="398" mime_type="video/mp4" res="720p" fps="25fps" vcodec="av01.0.05M.08" progressive="False" type="video">, <Stream: itag="135" mime_type="video/mp4" res="480p" fps="25fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="244" mime_type="video/webm" res="480p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="397" mime_type="video/mp4" res="480p" fps="25fps" vcodec="av01.0.04M.08" progressive="False" type="video">, <Stream: itag="134" mime_type="video/mp4" res="360p" fps="25fps" vcodec="avc1.4d401e" 
progressive="False" type="video">, <Stream: itag="243" mime_type="video/webm" res="360p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: 
itag="396" mime_type="video/mp4" res="360p" fps="25fps" vcodec="av01.0.01M.08" progressive="False" type="video">, <Stream: itag="133" mime_type="video/mp4" res="240p" fps="25fps" vcodec="avc1.4d4015" progressive="False" type="video">, <Stream: itag="242" mime_type="video/webm" res="240p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="395" mime_type="video/mp4" res="240p" fps="25fps" vcodec="av01.0.00M.08" progressive="False" type="video">, <Stream: itag="160" mime_type="video/mp4" res="144p" fps="25fps" vcodec="avc1.4d400c" progressive="False" type="video">, <Stream: itag="278" mime_type="video/webm" res="144p" fps="25fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="394" mime_type="video/mp4" res="144p" fps="25fps" vcodec="av01.0.00M.08" progressive="False" type="video">, <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">, <Stream: 
itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]



'''