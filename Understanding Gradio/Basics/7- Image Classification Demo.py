import gradio as gr
import torch
from torchvision import models, transforms
from PIL import Image

# Load pre-trained model
model = models.resnet18(pretrained=True)
model.eval()

# Define image transformation
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def classify_image(image):
    image = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image)
    _, predicted = torch.max(outputs, 1)
    return predicted.item()

interface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3)
)

interface.launch()
