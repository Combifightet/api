"""Module responsible for running the webserver instance."""

import os
import uvicorn

from src.app import app


if __name__ == '__main__':
    uvicorn.run(
        app,
        host=os.getenv('HOST', 'localhost'),
        port=int(os.getenv('PORT', '8000')),
    )
