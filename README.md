<h1 align="center">
WinGroundRm
</h1>



WinGround streamlines the process of removing backgrounds from images with direct integration into the Windows Explorer context menu. This feature allows you to quickly eliminate unwanted backgrounds from your images with just a few clicks.

https://github.com/MdCode002/WinGroundRm/assets/111018812/da6799ab-6971-4d33-91bd-c95ffc06ea22


---

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Uninstall](#Uninstall)
- [Contributing](#contributing)
- [Author](#Author)
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
Make sure you have Python installed on your computer, then execute that command.

    ```bash
    pip install rembg pillow
    ```

4. **install WinGroundRm :**<br>
 ⚠️ Run this command in an administrative command prompt. It will add the Context Menu Entry and it will download the U2Net model, and place it at `C:\Users\{currentUser}\.u2net`.<br>
⚠️ Make sure not to delete `test.png` before executing this command.<br>
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
   


## Uninstall

To uninstall WinGroundRm, run the following command in an administrative command prompt:

   ```bash
    python uninstall.py

   ```
This will remove the U2Net model and delete the registry entries created by WinGroundRm.



## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Author
- Developed by: Mouhamed Diouf
- GitHub: [@MdCode002](https://github.com/MdCode002)
- Email: dioufmouhamed002@gmail.com

## License

This project is licensed under the [MIT License](LICENSE).

---

