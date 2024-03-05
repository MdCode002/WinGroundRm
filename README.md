<h1 align="center">
WinGroundRm
</h1>



> Add a context menu option to Windows Explorer for easy background removal from images.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Seamless Integration**: Integrates with the Windows Explorer context menu for easy access.
- **Advanced Background Removal**: Uses the powerful Rembg library to remove backgrounds from images.
- **Format Support**: Works with various image formats.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/MdCode002/WinGroundRm.git
    cd WinGroundRm
    ```

2. **Install Dependencies:**

    ```bash
    pip install rembg pillow
    ```

3. **install WinGroundRm :**
 ⚠️ Run this command in an administrative command prompt. It will add the Context Menu Entry and it will download the U2Net model, and place it at `C:\Users\{currentUser}\.u2net`. Make     sure not to delete `test.png` before executing this command:
 ⚠️ After installation, please avoid moving the WinGroundRm folder. If needed, uninstall it and then reinstall it.
   

    ```bash
    python WinGroundRm.py
    ```

5. **Usage:**

    Right-click on an image file in Windows Explorer to see the new "WinGroundRm remove Background image" option.

## Usage

1. Right-click on an image file in Windows Explorer.
2. Select the "WinGroundRm remove Background image" option from the context menu.
3. The background will be removed, and the modified image will be saved in the same directory.

## Configuration

No additional configuration is required. The script automatically adds the necessary entries to the Windows Registry.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

