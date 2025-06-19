import barcode
from barcode.writer import ImageWriter
from barcode import Code128

def generate_barcode_png(data):
    # Generate Code128 barcode with PNG output
    code = Code128(data, writer=ImageWriter())
    filename = code.save("barcode")  # Will save as barcode.png
    print(f"Barcode saved as {filename}.png")

# Sample data
data = "1234-5678-9012"
generate_barcode_png(data)
