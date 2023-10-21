import os, pathlib
from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests
import matplotlib.pyplot as plt
import matplotlib.patches

folder_output = "images/outputs"


### url
path_or_url = "http://images.cocodataset.org/val2017/000000039769.jpg"
path_or_url = "https://huggingface.co/datasets/mishig/sample_images/resolve/main/airport.jpg"
path_or_url =  "./images/28-northampton-rd-croydon-wider.png"
# image_file_path = "./images/28-northampton-rd-croydon.png"
# image_file_path = "./images/28-northampton-rd-croydon-wider.png"

p = pathlib.Path(path_or_url)
if p.is_file():
    image = Image.open(path_or_url).convert("RGB")
else:
    image = Image.open(requests.get(path_or_url, stream=True).raw)

# you can specify the revision tag if you don't want the timm dependency
processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)

# convert outputs (bounding boxes and class logits) to COCO API
# let's only keep detections with score > 0.9
target_sizes = torch.tensor([image.size[::-1]])
results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    print(
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
    )


# Create figure and axes
fig, ax = plt.subplots()
# Display the image
ax.imshow(image)
for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]

    # Create a Rectangle patch
    xy = box[:2]
    width = box[2]-box[0]
    height = box[3]-box[1]
    rectangle_patch = matplotlib.patches.Rectangle(xy, width, height, linewidth=1, edgecolor='r', facecolor='none')

    # Add the patch to the Axes
    ax.add_patch(rectangle_patch)

plt.show()
fig.savefig(
    os.path.join(folder_output, p.stem + "-detection.png")
)
