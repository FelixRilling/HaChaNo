# HaChaNo

> **Ha**rdware **Cha**nge **No**tifier

Simple Python script to play sounds when usb devices are added and removed under linux, the same way windows does.

## Dependencies

Requires Python 3.x and pip.

1. Ensure `libudev` is available.
2. Prepare [PyGObject requirements](https://pygobject.readthedocs.io/en/latest/getting_started.html#) ("Installing from PyPI with pip").
3. Install pip dependencies.
 ```shell script
pip install -r requirements.txt
```
 
## Usage

Configure the sounds in `config.yaml` to fit your needs, then start `main.py`.

Now, adding or removing USB devices will play the sound file configured.
