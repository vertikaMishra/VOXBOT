VOXBOT – Python Voice Assistant

A Python-based voice assistant that enables users to interact with a computer through voice commands. VOXBOT uses speech recognition to understand spoken instructions and text-to-speech technology to provide audio responses.

Project Overview

VOXBOT is a desktop voice assistant developed using Python. It captures voice input through a microphone, processes spoken commands, and responds using speech synthesis.

Key Features

- Voice-based user interaction.
- Speech-to-text conversion.
- Text-to-speech responses.
- Microphone input for capturing voice commands.
- Interactive communication.
- Python-based voice processing.

Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| SpeechRecognition | Speech recognition |
| pyttsx3 | Text-to-speech conversion |
| PyAudio | Microphone audio input |
| SAPI5 | Windows speech engine |

Project Structure

```text
VOXBOT/
│
├── main.py
├── .gitignore
└── README.md
```

Installation and Setup

1. Create a Virtual Environment

```bash
python -m venv .venv
```

2. Activate the Environment

For Windows:

```bash
.venv\Scripts\activate
```

3. Install Dependencies

```bash
pip install SpeechRecognition pyttsx3 pyaudio
```

4. Run the Application

```bash
python main.py
```

How It Works

1. Initializes the speech recognition and text-to-speech engines.
2. Captures the user's voice through a microphone.
3. Converts spoken commands into text.
4. Processes the recognized commands.
5. Generates spoken responses using the text-to-speech engine.

Learning Outcomes

- Practical Python programming.
- Speech recognition implementation.
- Text-to-speech integration.
- Microphone input handling.
- Python library integration and debugging.

Future Improvements

- Add more voice-controlled functionalities.
- Integrate web search capabilities.
- Improve natural language understanding.
- Implement desktop automation features.
- Enhance voice interaction and error handling.

Developer

Vertika Mishra

BCA Student | Python Developer | Aspiring Software Developer

- GitHub: [Explore my projects](https://github.com/vertikaMishra)

---

⭐ Thank you for visiting VOXBOT!
