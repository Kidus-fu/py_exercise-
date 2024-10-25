import qrcode
import os

class QRMaker:
    def __init__(self, data, name="QRCODE_IMG", img_format="png"):
        """
        Initializes the QRMaker class with the provided data, name, and image format.
        
        :param data: The data to encode in the QR code.
        :param name: The name of the output image file.
        :param img_format: The image format (e.g., png, jpg).
        """
        self.data = data
        self.name = name
        self.img_format = img_format
    
    def create_qr_image(self):
        """
        Generates and saves a QR code image based on the data and other parameters.
        The image is saved in the 'QR-images' folder.
        """
        # Set up QR code configuration
        qr = qrcode.QRCode(
            border=15,
            box_size=15,
            version=5,
            error_correction=qrcode.constants.ERROR_CORRECT_H  # High error correction
        )
        
        # Ensure the QR-images folder exists
        os.makedirs("QR-images", exist_ok=True)
        
        # Generate the QR code
        qr.add_data(self.data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save and display the image
        file_path = f"QR-images/{self.name}.{self.img_format}"
        img.save(file_path)
        img.show()
        print(f"QR code saved as '{file_path}'.")

# Collect user input with improved prompts and validation
def main():
    print("Welcome to the QR Code Generator!")
    name = input("Enter the name for the QR code image file (default is 'QRCODE_IMG'): ")
    img_format = input("Enter the image format (e.g., png, jpg) [default: png]: ").strip() or "png"
    data = input("Enter the data to encode in the QR code: ").strip()

    # Validate data input
    if not data:
        print("Error: Data for the QR code cannot be empty.")
        return
    
    # Initialize and create QR code
    qr_maker = QRMaker(data=data, name=name or "QRCODE_IMG", img_format=img_format)
    qr_maker.create_qr_image()

if __name__ == "__main__":
    main()
