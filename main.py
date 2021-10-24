import logging
from typing import Dict

import yaml

from hachano import HaChaNo

logging.basicConfig(level=logging.INFO)

with open(r"./config.yaml", encoding="utf8") as file:
	config = yaml.load(file, Loader=yaml.SafeLoader)

	sounds: Dict[str, str] = config.get("sounds")
	if sounds is None:
		raise ValueError("'sounds' was not found in config.")

	HaChaNo(sounds).start()
