# vsumm

`vsumm` is a Python script that fetches subtitles from a YouTube video and generates a summary using an AI model.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/NihadBadalov/vsumm.git
    cd vsumm
    ```

2. Download and install `ollama`:
    ```sh
    curl -fsSL https://ollama.com/install.sh | sh
    ```

3. Pull the `llama3.2:3b` model:
    ```sh
    ollama pull llama3.2:3b
    ```

4. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:
    ```sh
    python vsumm.py
    ```

2. Input the YouTube video ID when prompted.

3. The script will check if subtitles for the video already exist in the `subs` directory. If not, it will fetch the subtitles.

4. If subtitles are fetched successfully, the script will ask if you want to generate a new summary or use an existing one.

5. The summary will be displayed and saved in the `summarizations` directory.

## Dependencies

- `youtube_transcript_api`
- `ollama`
- `colorama`
- `asyncio`

## Example

```sh
Input the video id: dQw4w9WgXcQ

Subtitles fetched successfully!

Do you want to make the AI summarize this again? Or do you want to use the existing summary? (y/n): y

Summary:
This is an example summary of the video.
```

## License

This project is licensed under the MIT License.
