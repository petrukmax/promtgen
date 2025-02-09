# promtgen

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**promtgen** is a simple Python application designed to merge text from three input areas into a single output string. It allows users to combine lines of text from three separate text fields, repeating lines as necessary, and copy the result to the clipboard.

This project is hosted on GitHub at [https://github.com/petrukmax/promtgen](https://github.com/petrukmax/promtgen).

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Requirements](#requirements)
- [License](#license)

---

## Features

- Combines text from three input areas into a single output.
- Automatically repeats lines from shorter input areas if needed.
- Copies the final result to the clipboard with proper formatting.
- Fully scalable UI that adjusts to window size.

---

## Installation

To use this application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/petrukmax/promtgen.git
   ```

2. Navigate to the project directory:
   ```bash
   cd promtgen
   ```

3. Install the required dependencies:
   ```bash
   pip install pyperclip
   ```

4. Run the application:
   ```bash
   python promtgen.py
   ```

---

## Usage

1. Open the application.
2. Enter text into the three input areas (left, middle, and right).
3. Click the "Create/Copy" button.
4. The combined result will be copied to your clipboard.

---

## Example

### Input

#### Text Area 1:
```
A
B
C
```

#### Text Area 2:
```
1
2
```

#### Text Area 3:
```
X
Y
Z
```

### Output (Copied to Clipboard):
```
A 1 X
B 2 Y
C 1 Z
```

---

## Requirements

- Python 3.6 or higher
- `pyperclip` library for clipboard functionality

---

## License

This project is licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for more details.
