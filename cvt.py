import rawpy

# Open the CR3 file using rawpy.imread()
with rawpy.imread("0N1A4133.CR3") as raw:
    # Convert the raw image to a 8-bit RGB image
    rgb = raw.postprocess()

    # Save the RGB image as a JPG file using the save() method
    Image.fromarray(rgb).save("output.jpg")
