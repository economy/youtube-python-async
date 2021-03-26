# youtube-python-async
===================
#### Python - Youtube Data API v3

**youtube-python-async** is an asynchronous client for the YouTube API, based on [youtube-python](https://github.com/rohitkhatri/youtube-python).
        It uses the [Youtube Data API v3](https://developers.google.com/youtube/v3/).
## Installation
``` 
pip install git+git://github.com/economy/youtube-python-async.git
```

## Set up API client

```python
from youtube_async import API

api = API(client_id='', client_secret='', api_key='', access_token='optional')
```

## Query [videos](https://developers.google.com/youtube/v3/docs/videos)
```python
video = await api.get('videos', id='B7FJV9KIn58')
```

## Query [channels](https://developers.google.com/youtube/v3/docs/channels/list)
```python
channel = await api.get('channels', id='UCLFZ5qAH-l_WiRd_EOzX2og')
```

## Contributing
[https://github.com/economy/youtube-python-async](https://github.com/rohitkhatri/youtube-python)

## Youtube Data API v3
[Youtube Data API v3 Doc](https://developers.google.com/youtube/v3/)
