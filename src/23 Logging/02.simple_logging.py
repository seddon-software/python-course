'''
The logging module is very flexible and allows many different texchniques.  Here we look at the simplest way og logging:
'''
import logging

LOG_FILENAME = "simple_logging.log"
logging.basicConfig(
    filename= f"{LOG_FILENAME}",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

logging.info("Program started")
logging.error("Something went wrong")


with open(f"{LOG_FILENAME}", "r") as f:
    content = f.read()
print(content)
