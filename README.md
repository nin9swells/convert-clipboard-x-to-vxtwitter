# convert-clipboard-x-to-vxtwitter

## Description
This script monitors the clipboard for URLs containing 'x.com' and modifies them to 'vxtwitter.com'. It continuously checks the clipboard for changes and performs the URL modification when a matching URL is found.

## How to use
1. Download executable file from [release page](https://github.com/nin9swells/convert-clipboard-x-to-vxtwitter/releases)
2. Open executable

## Build
This repository is using GitHub Action that will automatically build new executable when there is new git tag.

If you're looking for manual build, see these sections below.

### Requirements
See the `requirements.txt` file for a list of required packages.

### Build command 
The executable is built using pyinstaller

```
pyinstaller.exe --onefile .\main.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
