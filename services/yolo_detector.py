from ultralytics import YOLO
import time
import logging
from concurrent.futures import ThreadPoolExecutor, TimeoutError

# Configuration for resiliency\ nRETRY_COUNT = 3
RETRY_DELAY = 1  # seconds between retries
DETECTION_TIMEOUT = 10  # seconds max per detection

# Load YOLOv8 nano model (downloads weights on first run)
model = YOLO('yolov8n.pt')


def detect_cars(image_path: str, conf_threshold: float = 0.5) -> bool:
    """
    Run object detection on image_path and return True if a 'car' is detected above confidence threshold.
    Implements retry on transient errors and enforces a timeout per inference.
    """
    for attempt in range(1, RETRY_COUNT + 1):
        try:
            # Execute inference with timeout
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(model, image_path)
                results = future.result(timeout=DETECTION_TIMEOUT)

            detections = results[0]
            # Check for 'car' class (COCO id 2)
            for cls, conf in zip(detections.boxes.cls, detections.boxes.conf):
                if int(cls) == 2 and conf >= conf_threshold:
                    return True
            return False

        except TimeoutError:
            logging.warning(f"YOLO detection timed out for {image_path} on attempt {attempt}")
        except Exception as e:
            logging.warning(f"Transient error on YOLO detection for {image_path} (attempt {attempt}): {e}")
        # Retry after delay
        if attempt < RETRY_COUNT:
            time.sleep(RETRY_DELAY)

    logging.error(f"YOLO detection failed after {RETRY_COUNT} attempts for {image_path}")
    return False
