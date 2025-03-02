# Neatipy

**Neatipy** is a high-performance Python library for elegant and efficient object formatting and printing. Designed for developers who value both aesthetics and speed, Neatipy ensures minimal computational overhead by leveraging a custom-built **LRU cache** and eliminating redundant operations whenever possible.

---

## 🚀 Features

✅ **Blazing Fast Performance** – Utilizes a self-written LRU cache to minimize redundant calculations.

✅ **Smart Formatting** – Automatically adjusts output styles based on data type and context.

✅ **Minimal Overhead** – Avoids unnecessary computations, making it ideal for high-performance applications.

✅ **Flexible API** – Provides both high-level convenience functions and low-level formatting utilities.

✅ **Pythonic & Modern** – Built with Python 3.10+ and leverages `match-case` for elegant pattern matching.

---

## 📦 Installation

Neatipy is easy to install and use. Simply clone the repository and install it:

```bash
pip install ./Neatipy
```


---

## 📖 Usage

### ✨ Basic Example

```python
from neatipy import Neatipy

data = {"name": "Neatipy", "version": 0.1, "features": ["LRU Cache", "Fast Formatting"]}

Neatipy.nprint(data)
```

### ⚡ Performance Boosting with Custom LRU Cache

Neatipy avoids repetitive calculations by implementing a **custom LRU cache**, optimizing formatting calls for frequently processed objects:

```python
from neatipy import NeatipyFormatter

def expensive_formatting(obj: tuple) -> str:
    return NeatipyFormatter.format(obj)  # This will be cached for reuse, as wil all relatively heavy immutable object that may require a lot of formatting

print(expensive_formatting((1,2,3,))) # First call, will be cached
print(expensive_formatting((1,2,3,)))  # Retrieved instantly from cache
```

---

## 🔥 Why Neatipy?

Unlike traditional formatting libraries, **Neatipy** focuses on:

- **Smart Caching**: Our custom LRU cache ensures that repeated formatting calls are optimized.
- **Performance-Centric Design**: We remove redundant computations, keeping execution times low.
- **Intuitive and Readable Output**: Objects are printed in a way that enhances clarity and readability.
- **Future-Proofing**: Leverages modern Python features like `match-case` and type hinting.

---

## 🛠️ API Reference

### `Neatipy.nprint(obj: any) -> None`
Nicely prints an object with auto-detection of formatting style. Uses formatter internally.

### `NeatipyFormatter.format(obj: any) -> str`
Formats an object into a readable string while leveraging caching.


---

## 🌍 Contributing

We welcome contributions! Feel free to open issues, submit PRs, or suggest new features.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -m "Add feature xyz"`)
4. Push and create a PR

---

## 📜 License

MIT License. See `LICENSE` file for details.

---

## 💬 Contact

Created by **Vilppu Tiilikainen** – Reach me at [vilppu.tiilikainen123@gmail.com](mailto:vilppu.tiilikainen123@gmail.com)

