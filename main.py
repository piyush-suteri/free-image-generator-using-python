import webview
import requests
import os
import urllib.parse
from datetime import datetime


class API:
    def receive_url(self, description):
        print(f"Received description: {description}")

        # Construct the URL using the description (send to image API)
        url = f"https://image.pollinations.ai/prompt/{urllib.parse.quote(description)}.jpg"
        response = requests.get(url)

        if response.status_code == 200:
            try:
                # Create a 'history' folder to store images
                history_folder = os.path.join(os.getcwd(), 'history')
                os.makedirs(history_folder, exist_ok=True)

                # Generate a filename: shorten description and clean unsupported characters
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                cleaned_description = description[:50].replace(
                    " ", "_").replace("/", "_").replace("\\", "_")
                image_filename = f"{cleaned_description}_{timestamp}.jpg"
                image_path = os.path.join(history_folder, image_filename)

                # Save the image
                with open(image_path, 'wb') as file:
                    file.write(response.content)

                print(f"Image saved to {image_path}")

                # Open the image with the default image viewer
                if os.name == 'nt':  # For Windows
                    os.startfile(image_path)
                elif os.name == 'posix':  # For macOS/Linux
                    os.system(f'open {image_path}')

                # Notify the frontend about success
                webview.windows[0].evaluate_js(f"""
                    showSuccessMessage('{image_path}');
                """)

            except Exception as e:
                print(f"Error saving or opening image: {e}")
                # Send failure message to frontend
                webview.windows[0].evaluate_js(f"""
                    document.getElementById('spinner').style.display = 'none';
                    document.querySelector('button').disabled = false;
                    document.getElementById('resetButton').disabled = false;
                    alert('Error while downloading the image.');
                """)
        else:
            print("Failed to retrieve image")
            # Send failure message to frontend
            webview.windows[0].evaluate_js(f"""
                document.getElementById('spinner').style.display = 'none';
                document.querySelector('button').disabled = false;
                document.getElementById('resetButton').disabled = false;
                alert('Failed to generate image.');
            """)


# Create the API instance and start the webview
api = API()

# Open the webview window with the frontend (index.html) and pass the API
webview.create_window('Text to Image Generator',
                      'index.html', js_api=api, width=1200, height=800)

# Start the webview to begin the app
webview.start()
