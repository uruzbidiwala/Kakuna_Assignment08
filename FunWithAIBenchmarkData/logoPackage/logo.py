# File Name : logo.py
# Student Name: Uruz B, Shantele K, Nogaye G
# email:  bidiwaur@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:  3/27/2025
# Course #/Section: IS 4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Created code for logoPackage and visualPackage to run the graph and picture

# Brief Description of what this module does.Added a chart and logo
# Citations: ChatGPT and Youtube

# Anything else that's relevant:

from PIL import Image
import os

def load_logo():
    """Loads and returns the Assignment08pic.jpg image resized to 200x200 pixels."""
    # Get the absolute path of the image
    image_path = os.path.join(os.path.dirname(__file__), "../LogoPicture/Assignment08pic.jpg")
   
    try:
        img = Image.open(image_path)
        return img
    except FileNotFoundError:
        print(f"Error: Image file not found at {image_path}")
        return None
