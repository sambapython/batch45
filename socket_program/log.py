import logging
logging.basicConfig(level=logging.DEBUG, 
	filename="log.txt",
	format="%(asctime)s==>%(levelname)s==>%(message)s",
	)
logging.info("info message")
logging.error("error message")
logging.debug("debug message")
logging.warn("warning message")