import logging
from logging import Logger
from typing import Dict

import pyudev
from playsound import playsound
from pyudev import Context, Device


class HaChaNo:
    __logger: Logger = logging.getLogger("HaChaNo")
    __sounds: Dict[str, str]

    def __init__(self, sounds: Dict[str, str]):
        self.__sounds = sounds

    def start(self):
        context: Context = pyudev.Context()
        monitor = pyudev.Monitor.from_netlink(context)
        monitor.filter_by("usb", "usb_device")
        self.__logger.info("Start listening for device changes.")
        for device in iter(monitor.poll, None):
            self.__on_event(device)

    def __on_event(self, device: Device):
        if device.action == "add":
            self.__logger.info("Added device '%s'.", device.device_path)
            self.__play__sound("add")
        elif device.action == "remove":
            self.__logger.info("Removed device '%s'.", device.device_path)
            self.__play__sound("remove")

    def __play__sound(self, sound: str):
        sound_path = self.__sounds.get(sound)
        if sound_path is None:
            self.__logger.warning("No sound configured for '%s'.", sound)
            return

        playsound(sound_path)
