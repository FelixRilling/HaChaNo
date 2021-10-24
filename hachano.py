from logging import Logger, getLogger
from typing import Dict

from pydub import playback, AudioSegment
from pyudev import Context, Device, Monitor


class HaChaNo:
	__logger: Logger = getLogger("HaChaNo")
	__sounds: Dict[str, str]

	def __init__(self, sounds: Dict[str, str]):
		self.__sounds = sounds

	def start(self):
		context: Context = Context()
		monitor = Monitor.from_netlink(context)
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
		playback.play(AudioSegment.from_file(sound_path))
