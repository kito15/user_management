import logging
import sys
from pathlib import Path

def setup_logger():
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            # Log to console
            logging.StreamHandler(sys.stdout),
            # Log to file
            logging.FileHandler(log_dir / "app.log")
        ]
    )
    
    return logging.getLogger(__name__)

logger = setup_logger()
