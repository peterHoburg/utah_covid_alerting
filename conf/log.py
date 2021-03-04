import logging
import os
import sys

log = logging.getLogger(__name__)
root_logger = logging.getLogger()

for handler in root_logger.handlers:
    root_logger.removeHandler(handler)

for handler in log.handlers:
    log.removeHandler(handler)

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(logging.Formatter("%(asctime)s - %(threadName)s - %(levelname)s - %(message)s"))

log.addHandler(stream_handler)

if os.environ.get("DEBUG") == "true":
    logging.disable(logging.DEBUG)
else:
    log.setLevel(logging.INFO)
