# Xeno-Canto API endpoint for bird songs
api_url = "https://xeno-canto.org/api/2/recordings?query=sp&field=species"

def download_audio(url, file_path):
    """Download audio file from the given URL and save it to the specified file path."""
    try:
        urllib.request.urlretrieve(url, file_path)
        print(f"Audio file saved: {file_path}")
    except Exception as e:
        print(f"Error downloading audio: {e}")

def extract_bird_songs(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            for recording in data["recordings"]:
                # Extract relevant information from the recording
                name = recording["en"]
                audio_url = recording["file"]
                file_path = f"{name}.mp3"  # Save the audio with the bird's name as the file name

                # Download the audio file
                download_audio(audio_url, file_path)
        else:
            print(f"Error fetching data from Xeno-Canto API. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error extracting bird songs: {e}")

if _name_ == "_main_":
    extract_bird_songs(api_url)