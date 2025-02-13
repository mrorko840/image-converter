# Image Converter

![Image Converter](https://img.shields.io/badge/PyQt6-GUI-blue.svg) ![Python](https://img.shields.io/badge/Python-3.8%2B-brightgreen.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A powerful and user-friendly **Image Converter** application built with **PyQt6**, allowing users to convert image formats easily from local files or URLs. It supports **PNG, JPG, and JPEG** formats and offers seamless **Cloudinary** integration for AVIF conversion.

## 🚀 Features

- 📂 **Select Image** from your device
- 🌐 **Fetch Image** from a URL
- 🔄 **Convert Images** to PNG, JPG, or JPEG
- ☁ **Cloudinary Integration** for AVIF conversion
- 💾 **Save Converted Images** with custom filenames
- 🖥 **Easy-to-Use GUI** with PyQt6

## 🖼️ Preview

<img src="https://i.imgur.com/kW8WuJM.png" alt="App Screenshot" width="330px">

## 🔧 Installation

Ensure you have Python **3.8+** installed, then follow these steps:

```sh
#Step1: Clone the repository
git clone https://github.com/mrorko840/image-converter.git
cd image-converter

#Step2: Create a virtual environment (Optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

#*************************************************************
#if you are using PyCharm Software then you can ignore Step2 *
#*************************************************************

#Step3: Install dependencies
pip install -r requirements.txt
```

## 🛠️ Usage

Run the application with:

```sh
python app.py
```

## 📦 Dependencies

The required dependencies are listed in `requirements.txt`:

```
PyQt6==6.8.1
pillow==11.1.0
requests==2.32.3
cloudinary==1.42.2
pyinstaller==6.12.0
```

## 🔑 Make Application

Make .exe file using this command(**_windows_**):

```
pyinstaller --onefile --noconsole --icon=icon.ico --add-data "icon.ico;." app.py
```

Make .app file using this command(**_mac_**):

```
pyinstaller --windowed --name "ImageConverter" --icon=icon.ico app.py
```

## 📝 License

This project is licensed under the **MIT License**.

## 🤝 Contributing

Feel free to fork this repository, open issues, and submit pull requests. Contributions are welcome! 🎉

## 📞 Contact

For any queries, reach out to

<a target="_blank" style="display: inline-flex; align-items: center; gap: 8px; text-decoration: none;" href="https://www.facebook.com/mr.orko.10">
    <img style="width: 16px; height: 16px; vertical-align: middle;" src="https://cdn.freebiesupply.com/logos/large/2x/facebook-logo-2019.png"> হিমেল
</a>
<br />
<a target="_blank" style="display: inline-flex; align-items: center; gap: 8px; text-decoration: none;" href="https://www.facebook.com/Engineer.MD.Shariful.Islam.Tutul">
    <img style="width: 16px; height: 16px; vertical-align: middle;" src="https://cdn.freebiesupply.com/logos/large/2x/facebook-logo-2019.png"> MD Shariful Islam Tutul
</a>