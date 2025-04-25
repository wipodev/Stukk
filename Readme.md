<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./documentation_images/Stukk_logo_dark.png">
    <img src="./documentation_images/Stukk_logo_light.png">
  </picture>
</p>

<div align="center">

![PyPI](https://img.shields.io/pypi/v/stukk)
![PyPI - Downloads](https://img.shields.io/pypi/dm/stukk?color=green&label=downloads)
![PyPI - License](https://img.shields.io/badge/license-MIT-blue)

</div>

---

## ✨ Stukk — Modern Tkinter UI (Fork of CustomTkinter)

**Stukk** is a fork of [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter), a modern UI library for Python’s Tkinter. This project continues to offer fully customizable, modern widgets with light/dark theme support and HighDPI scaling.

> Stukk introduces improvements, bug fixes, and a modernized configuration with focus on maintainability and ongoing development.

---

## 🆕 Changes introduced in Stukk

For details on changes and improvements introduced in this fork, please refer to the [CHANGELOG](./CHANGELOG.md).

---

## 🚀 Installation

```bash
pip install stukk
```

> The package installs as `stukk`, but you still import it as:

```python
import customtkinter
```

> To set up the development environment, follow the instructions in [project-setup.md](./docs/project-setup.md).

---

## 🔭 Future plans

- Additional bug fixes inherited from the original project.
- Introduction of new features and enhancements.

---

## 📚 Documentation

You can refer to the [official CustomTkinter documentation](https://customtkinter.tomschimansky.com/documentation), since **Stukk** is currently API-compatible.

---

## 🧪 Basic Example

```python
import customtkinter

customtkinter.set_appearance_mode("System")  # system (default), light, dark
customtkinter.set_default_color_theme("blue")  # blue (default), dark-blue, green

app = customtkinter.CTk()
app.geometry("400x240")

def button_function():
    print("button pressed")

button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()
```

---

## 📸 Screenshots and Examples

> The following images and videos are from the original project and still apply to Stukk.

### Appearance mode change and scaling change

CustomTkinter can adapt to the Windows 10/11 light or dark mode:

https://user-images.githubusercontent.com/66446067/204672968-6584f360-4c52-434f-9c16-25761341368b.mp4

| _`complex_example.py` on Windows 11 with system appearance mode change and standard 'blue' theme_

###

On macOS you either need python3.10 or higher or the anaconda python
version to get a dark window header (Tcl/Tk >= 8.6.9 required):

https://user-images.githubusercontent.com/66446067/204673854-b6cbcfda-d9a1-4425-92a3-5b57d7f2fd6b.mp4

| _`complex_example.py` on macOS with system appearance mode change, user-scaling change and standard 'blue' theme_

###

### Button with images

It's possible to put an image on a CTkButton. You just have to
pass a PhotoImage object to the CTkButton with the `image` argument.
If you want no text at all you have to set `text=""` or you specify
how to position the text and image at once with the `compound` option:

![](documentation_images/image_example_dark_Windows.png)
| _`image_example.py` on Windows 11_

###

### Scrollable Frames

Scrollable frames are possible in vertical or horizontal orientation and can be combined
with any other widgets.
![](documentation_images/scrollable_frame_example_Windows.png)
| _`scrollable_frame_example.py` on Windows 11_

### Integration of TkinterMapView widget

In the following example I used a TkinterMapView which integrates
well with a CustomTkinter program. It's a tile based map widget which displays
OpenStreetMap or other tile based maps:

https://user-images.githubusercontent.com/66446067/204675835-1584a8da-5acc-4993-b4a9-e70f06fa14b0.mp4

| _`examples/map_with_customtkinter.py` from TkinterMapView repository on Windows 11_

You can find the TkinterMapView library and example program here:
https://github.com/TomSchimansky/TkinterMapView

---

## 🙌 Credits

This project is a fork of [Tom Schimansky / CustomTkinter](https://github.com/TomSchimansky/CustomTkinter). All original credits go to him. **Stukk** aims to maintain and improve the library as the community evolves.

---

## 👤 Maintainer

**Stukk** is maintained by [WipoDev](https://github.com/wipodev/Stukk).
Want to contribute? Suggestions and PRs are welcome!
