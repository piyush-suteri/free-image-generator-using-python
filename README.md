# Text to Image Generator

A desktop application that generates images from text descriptions using Pollinations.ai API. Built with Python and WebView for a seamless desktop experience.

![image](https://github.com/user-attachments/assets/8e22ec79-c17c-4888-bb26-352fb2108a38)

![Screenshot 2025-01-13 221455](https://github.com/user-attachments/assets/a3310614-cca2-4d78-b47c-bdaa596c6a9c)

## Features

- Text-to-image generation using Pollinations.ai
- User-friendly desktop interface
- Image history saved locally
- Automatic image viewer integration
- Cross-platform compatibility (Windows, macOS, Linux)

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/text-to-image-generator.git
cd text-to-image-generator
```

2. Install the required dependencies:

```bash
pip install pywebview requests
```

## Usage

1. Run the application:

```bash
python main.py
```

2. Enter a text description in the textarea
3. Click "Generate Image" button
4. Wait for the image to be generated
5. The generated image will be:
   - Saved in the `history` folder
   - Displayed in the application
   - Opened in your default image viewer

## Project Structure

```
text-to-image-generator/
├── main.py           # Python backend using webview
├── index.html        # Main application interface
├── styles.css        # Application styling
├── script.js         # Frontend functionality
├── assets/          # Images and resources
└── history/         # Generated images storage
```

## Technical Details

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python with pywebview
- **Image Generation**: Pollinations.ai API
- **Image Storage**: Local filesystem


## License

Free to use.

## Contact

Piyush Suteri - piyushsuteri5286@outlook.com

YouTube Channel: [@piyushsuteri](https://youtube.com/@piyushsuteri)

## Acknowledgments

- [Pollinations.ai](https://pollinations.ai) for providing the image generation API
- [pywebview](https://pywebview.flowrl.com/) for the desktop application framework
