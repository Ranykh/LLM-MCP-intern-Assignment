from services.image_db import Session, Image, list_images_between
from datetime import datetime

# Step 1: Add sample images
session = Session()
session.add_all([
    Image(name="image_11-00.jpg", timestamp=datetime.strptime("11:00", "%H:%M")),
    Image(name="image_11-03.jpg", timestamp=datetime.strptime("11:03", "%H:%M")),
    Image(name="image_11-06.jpg", timestamp=datetime.strptime("11:06", "%H:%M")),
])
session.commit()

print("✅ Sample images inserted into DB.")

# Step 2: Test the query function
results = list_images_between("11:00", "11:05")
print("🖼️ Images between 11:00 and 11:05:")
for image_name in results:
    print(" →", image_name)
