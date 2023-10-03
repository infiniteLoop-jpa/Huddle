from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image, ImageDraw

def image_manipulation(request):
    # Open an image file
    image = Image.open('https://www.boredpanda.com/blog/wp-content/uploads/2022/07/Cat-Virus-Exe-Funny-Pics-188-62c3dd4206b72__700.jpg')

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Perform some manipulation (e.g., add text)
    draw.text((10, 10), "Hello, Alondra!", fill=(255, 0, 0))

    # Save the modified image to a response
    response = HttpResponse(content_type='image/jpeg')
    image.save(response, 'JPEG')

    return response

# Create your views here.
