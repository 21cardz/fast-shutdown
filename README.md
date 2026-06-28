# Fast Shutdown ⚡

A Python script that lets you shutdown your device directly from the terminal — supporting desktop operating systems and mobile devices.

---

## 📋 Table of Contents
- [About](#about)
- [Supported Devices](#supported-devices)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Author](#author)

---

## About

Fast Shutdown is a simple Python script that detects your operating system and shuts it down instantly. It supports a wide range of devices from desktop computers to mobile phones, making it a handy tool for developers and general users alike.

---

## Supported Devices

| Device | Method |
|---|---|
| Linux | `shutdown -h now`, `halt`, `poweroff` |
| macOS (Darwin) | `shutdown -h now` |
| Windows | `shutdown /s /t 0` |
| Android | Rooted device or ADB |
| iOS / iPad | Jailbroken device or libimobiledevice |

---

## Requirements

- Python 3.x
- For **Android via ADB**: ADB (Android Debug Bridge) installed, USB debugging enabled
- For **Android rooted**: Rooted device running QPython or Termux
- For **iOS/iPad via USB**: libimobiledevice installed
- For **iOS/iPad jailbroken**: SSH access enabled on device

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/21cardz/fast-shutdown.git
```

2. Navigate into the project folder:
```bash
cd fast-shutdown
```

3. Run the script:
```bash
python3 fast_shutdown.py
```

---

## Usage

Simply run the script and Fast Shutdown will automatically detect your operating system and proceed accordingly:

```bash
python3 main.py
```

For **desktop systems** (Linux, macOS, Windows), it will shut down immediately.

For **mobile devices** (Android, iOS/iPad), it will prompt you to choose your shutdown method:
- Reply `yes` if your device is rooted/jailbroken
- Reply `via adb` or `via usb` if connected to a computer
- Reply `q` to quit

---

## How It Works

Fast Shutdown uses Python's built-in `platform` module to detect your OS, then runs the appropriate shutdown command for your device. For mobile devices it guides you through the available options based on your setup.

```python
import platform
platform.system()  # Returns 'Linux', 'Darwin', 'Windows', etc.
```

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request on [GitHub](https://github.com/21cardz/fast-shutdown).

1. Fork the project
2. Create your feature branch (`git checkout -b feature/new-device`)
3. Commit your changes (`git commit -m 'Add support for new device'`)
4. Push to the branch (`git push origin feature/new-device`)
5. Open a Pull Request

---

## Author

**21cardz**
GitHub: [@21cardz](https://github.com/21cardz)

---

> ⚠️ **Disclaimer:** Use this script responsibly. Make sure to save all your work before running Fast Shutdown. The author is not responsible for any data loss.
