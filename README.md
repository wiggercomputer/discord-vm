# Discord Voice Message Spoofer (discord-vm)

`discord-vm` is a Python package that allows you to send voice messages to Discord channels via the Discord API.

*This is a CLI implementation of the VoiceMessageSender classes developed in the [discord-voicemessage-sender](https://github.com/kaitlek/discord-voicemessage-sender) project.*

## Features

- Send voice messages to specified Discord channels.
- Generate and encode waveform data.
- Clean and process voice message files.

## Requirements

- Python 3.6 or higher
- A valid Discord token
- A Discord channel ID
- A voice message file (can be in nearly any audio format; Discord will convert it to `.ogg` so convert it to `.ogg` ahead of time if you distrust their lossy conversion)

## Installation

```bash
pipx install git+https://github.com/wiggercomputer/discord-vm
```

## Usage

You can use the command line interface to send voice messages to a Discord channel. 

### Command Line Interface

```sh
dvm --token YOUR_DISCORD_TOKEN --channel CHANNEL_ID --file PATH_TO_VOICE_MESSAGE_FILE
```

### Example

```sh
dvm --token mfa.YOUR_DISCORD_TOKEN --channel 123456789012345678 --file /path/to/voice-message.ogg
```

## Code Overview

### Main Script

The `main.py` script defines a command line interface for sending voice messages to Discord channels. It includes the following key components:

- **Argument Parsing**: Uses `argparse` to handle command line arguments.
- **VoiceMessageSender Class**: Handles the process of sending a voice message.
- **_VoiceMessageUtils Class**: Provides utility functions for generating waveform data, cleaning strings, encoding to base64, and getting audio duration.

### VoiceMessageSender Class

This class manages the process of sending a voice message to a Discord channel. It has methods for:

- **`__init__`**: Initializes the class with the Discord token and channel ID.
- **`SendVoiceMessage`**: Processes the voice message file and sends it to Discord.
- **`__GetUrl`**: Retrieves the URL for uploading the voice message.
- **`__UploadFile`**: Uploads the voice message file to the retrieved URL.
- **`__SendVoiceMessage`**: Sends the voice message to the specified Discord channel.

### _VoiceMessageUtils Class

This class provides utility functions used by the `VoiceMessageSender` class:

- **`GenerateWaveform`**: Generates a random waveform string.
- **`CleanString`**: Cleans a string by removing special characters.
- **`EncodeToB64`**: Encodes a string to base64.
- **`GetAudioDuration`**: Calculates the duration of an audio file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- wiggercomputer (obama@wigger.gay)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Issues

If you encounter any issues, please create a new issue in the [GitHub repository](https://github.com/wiggercomputer/discord-vm/issues).

