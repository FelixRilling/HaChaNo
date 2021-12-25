# HaChaNo

> **Ha**rdware **Cha**nge **No**tifier

Simple python script to play sounds when USB devices are connected or disconnected under linux.

## Dependencies

Requires Python 3.x and pip.

1. Ensure `libudev` is available on your system.
2. Install the python modules listed in `requirements.txt` using your package manager or pip.

## Usage

Configure the sounds in `config.yaml` to fit your needs, then start `main.py`.

Now, adding or removing USB devices will play the sound file configured.
