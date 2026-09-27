# 🎨 RGB to Grayscale Converter

A simple and lightweight **Python program that converts RGB images into grayscale** using pixel-level color transformation.

Turn those colorful pixels into clean shades of gray — because sometimes less color = more style. 🖤

## ✨ Features

- 🖼️ Converts RGB images to grayscale
- ⚡ Fast and lightweight
- 🐍 Built with Python
- 🎯 Simple command-line workflow
- 📦 Minimal dependencies
- 💾 Saves the converted image as a new file

## 🧠 How It Works

Each RGB pixel contains three color values:

```text
R = Red
G = Green
B = Blue
```

The program calculates a grayscale intensity from these values.

A common luminance formula is:

```text
Gray = 0.299R + 0.587G + 0.114B
```

The different weights account for how sensitive the human eye is to each color.

For example:

```text
RGB(255, 0, 0)
        ↓
Grayscale ≈ 76
```

So a bright red pixel becomes a medium-dark shade of gray.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/courtcurtain/grayscale.git
cd grayscale
```

### 2. Install dependencies


```bash
pip install -r requirements.txt
```

### 3. Run the program

```bash
grayscale.py
```

Follow the prompts to select your input image and output location.

## 📁 Project Structure

```text
rgb-to-grayscale/
│
├── main.py
├── input/
│   └── image.jpg
│
├── output/
│   └── grayscale.jpg
│
├── requirements.txt
└── README.md
```

## 🛠️ Example

**Before:**

```text
🌈 Colorful RGB Image
```

**After:**

```text
⬛ Grayscale Image
```

The original image remains unchanged while a grayscale version is generated separately.

## 🔬 Technologies

- **Python 3**

## 📌 Possible Improvements

Some ideas for future versions:

- [ ] Add a graphical user interface
- [ ] Support batch image conversion
- [ ] Add CLI arguments
- [ ] Add multiple grayscale algorithms


## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/my-feature
```

3. Commit your changes

```bash
git commit -m "Add my feature"
```

4. Push the branch

```bash
git push origin feature/my-feature
```

5. Open a Pull Request 🚀

## 📜 License

This project is open source.

---

<p align="center">
  Made with 🐍 and a little bit of grayscale magic.
</p>
