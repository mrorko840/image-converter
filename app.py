import sys
import os
import requests
import cloudinary
import cloudinary.uploader
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog,
    QLineEdit, QComboBox, QMessageBox, QInputDialog
)
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv

load_dotenv()
# Cloudinary Configuration
cloudinary.config(
    cloud_name="doihflfyz",
    api_key="144885736697597",
    api_secret="eoprw93aSKaEK0MFMRmGDiinkTo"
)
# cloudinary.config(
#     cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
#     api_key=os.getenv("CLOUDINARY_API_KEY"),
#     api_secret=os.getenv("CLOUDINARY_API_SECRET")
# )

class ImageConverterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.selected_file = None
        self.image_url = ""

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Image Converter")
        icon_path = os.path.join(os.path.dirname(__file__), "icon.ico")
        self.setWindowIcon(QIcon(icon_path))
        self.setGeometry(100, 100, 500, 500)

        layout = QVBoxLayout()

        self.file_label = QLabel("Select an image file or enter a URL", self)
        layout.addWidget(self.file_label)

        self.select_button = QPushButton("Browse", self)
        self.select_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_button)

        self.url_entry = QLineEdit(self)
        self.url_entry.setPlaceholderText("Enter image URL here")
        layout.addWidget(self.url_entry)

        self.url_button = QPushButton("Use URL", self)
        self.url_button.clicked.connect(self.select_url)
        layout.addWidget(self.url_button)

        self.format_label = QLabel("Select Output Format:", self)
        layout.addWidget(self.format_label)

        self.format_dropdown = QComboBox(self)
        self.format_dropdown.addItems(["PNG", "JPG", "JPEG"])
        layout.addWidget(self.format_dropdown)

        self.convert_button = QPushButton("Convert", self)
        self.convert_button.setEnabled(False)
        self.convert_button.clicked.connect(self.convert_image)
        layout.addWidget(self.convert_button)

        self.status_label = QLabel("", self)
        layout.addWidget(self.status_label)

        self.setLayout(layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Images (*.png *.jpg *.jpeg *.webp *.bmp *.gif *.avif)")
        if file_path:
            self.selected_file = file_path
            self.file_label.setText(f"Selected: {os.path.basename(file_path)}")
            self.convert_button.setEnabled(True)

    def select_url(self):
        url = self.url_entry.text().strip()
        if url:
            self.image_url = url
            self.selected_file = None
            self.file_label.setText("Using image from URL")
            self.convert_button.setEnabled(True)

    def convert_image(self):
        if not self.selected_file and not self.image_url:
            QMessageBox.warning(self, "No File Selected", "Please select an image or enter a URL!")
            return

        format_choice = self.format_dropdown.currentText().lower()
        save_dir = QFileDialog.getExistingDirectory(self, "Select Save Directory")
        if not save_dir:
            self.status_label.setText("No save directory selected!")
            return

        # ইউজার থেকে ফাইলের নাম ইনপুট নেওয়া
        file_name, ok = QInputDialog.getText(self, "File Name", "Enter file name (without extension):")
        if not ok or not file_name.strip():
            self.status_label.setText("No file name entered!")
            return
        file_name = file_name.strip()

        try:
            if self.image_url:
                response = requests.get(self.image_url)
                if response.status_code == 200:
                    img = Image.open(BytesIO(response.content))
                else:
                    raise Exception("Failed to fetch image from URL")
            else:
                if self.selected_file.lower().endswith(".avif"):
                    upload_result = cloudinary.uploader.upload(self.selected_file, format=format_choice)
                    img_url = upload_result.get("secure_url")
                    response = requests.get(img_url, stream=True)
                    if response.status_code == 200:
                        img = Image.open(BytesIO(response.content))
                    else:
                        raise Exception("Failed to fetch converted AVIF image from Cloudinary")
                else:
                    img = Image.open(self.selected_file)

            save_path = os.path.join(save_dir, f"{file_name}.{format_choice}")

            if format_choice in ["jpg", "jpeg"]:
                img = img.convert("RGB")
                img.save(save_path, format="JPEG", quality=95)
            else:
                img.save(save_path, format=format_choice.upper())

            self.status_label.setText("Conversion Successful!")
            QMessageBox.information(self, "Success", f"Image saved at:\n{save_path}")

        except Exception as e:
            self.status_label.setText(f"Error: {e}")
            QMessageBox.critical(self, "Error", f"Failed to convert image:\n{e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageConverterApp()
    window.show()
    sys.exit(app.exec())
