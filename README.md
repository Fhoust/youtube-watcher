# YouTube Watcher

A simple example Python script using Selenium to watch YouTube videos.

## Requirements

* Selenium
* WebDriver
    * [Google Chrome](https://chromedriver.chromium.org/)
    * [FireFox](https://github.com/mozilla/geckodriver/releases)

## Instalation

Download the WebDriver compatible with your browser then run:

``` shell
pip install -r requirements.txt
```

## Running

Fill the videos.json file with your videos information like bellow:

``` json
{
	"videos": [
    {"name": "<SOME NAME TO IDENTIFY>", "url": "<VIDEO_URL>", "duration": <VIDEO_DURATION_SECONDS>},
    ...
    ]
}
```

An example:

``` json
{
	"videos": [
    {"name": "Gorn - Alimta", "url": "https://youtu.be/x9t-Zktobm4", "duration": 511},
    {"name": "Interkosmos", "url": "https://youtu.be/zLYsVuWgR4I", "duration": 1392},
    {"name": "SKRILLEX - Bangarang", "url": "https://youtu.be/avFw-55j8BI", "duration": 227},
    ...
    ]
}
```

Then run:

``` shell
python3 main.py
```