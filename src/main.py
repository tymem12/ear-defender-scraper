import logging

import uvicorn
from dotenv import load_dotenv

from api.api import app

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )
    load_dotenv()

    uvicorn.run(app, host="0.0.0.0", port=8000)
