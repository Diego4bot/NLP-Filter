# N_Drago4 NLP Voicer

## Overview

This Python script is designed for natural language processing (NLP) voice recognition using the Vosk library. It incorporates various utilities for recognizing words and playing corresponding sounds based on the recognized words. The script utilizes PyAudio for audio stream setup, Vosk for speech recognition, and Pygame for playing audio files.

## Dependencies

Make sure to install the required libraries before running the script. You can install them using the following:

```bash
pip install pyaudio vosk pygame pillow
```

## Usage

1. **Run the script:** Execute the script in a Python environment.

    ```bash
    python your_script_name.py
    ```

2. **Audio Input:** The script captures audio input through the microphone using PyAudio.

3. **Speech Recognition:** Vosk is used for speech recognition. The recognized words are then 
matched against predefined lists.

4. **Playing Sounds:** The script plays sounds corresponding to the recognized words using Pygame. 
Sounds are organized into different categories (e.g., Greetings, Buda, Standard) based 
on the predefined paths and lists.

## Configuration

Adjust the following parameters in the script according to your requirements:

- `general_path_AUDIO_ESP`: The general path for storing audio files.
- `vgreetings`, `vbuda`, `va`, `vb`, ..., `vz`: Lists of words to recognize for different sound categories.
- Paths and lists of sound files for each category (Greetings, Buda, Standard, etc.).
- Pygame settings, such as volume and file format (`.mp3` in this case).

## Notes

- Ensure that the required audio files are present in the specified directories.
- Customize the script to include additional words or sound categories.
- The script is configured to recognize Spanish words based on the given lists.

## Disclaimer

The script may require further customization based on specific use cases and may need adjustments 
for different languages or word lists. Use responsibly and adhere to relevant legal and ethical considerations.

**Note:** The script references external modules and files such as `N_Drago4_NLP_voicer_utils`, 
`N_Drago4_NLP_frame3_word_map`, and `N_Drago4_NLP_PATH`. Make sure these modules are available and 
correctly configured for the script to run successfully.