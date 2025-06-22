import logging
import os
from datetime import datetime

# Step 1: Create a log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Define the logs directory and ensure it exists
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Step 3: Create the full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Step 4: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Optional: Log a test message

logging.info("Logging is configured and ready to use.")

logger = logging.getLogger(__name__)


if __name__=="__main__":
    logging.info("Logging is configured and ready to use.")