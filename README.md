# Vxpand
> A Text expander written in python

![GitHub release (latest by date)](https://img.shields.io/github/release-date/viera97/Vxpand)
![Language](https://img.shields.io/badge/language-python-green)
![Platforms](https://img.shields.io/badge/platforms-Windows%20and%20Linux-blue)
![License](https://img.shields.io/github/license/viera97/Vxpand)

#### What is Vxpand

Vxpand is a text expander multiplataform app, that detectects predefined **keywords** 
and replaces it with with a predefined anwser. It's based on the Idea of [espanso](https://github.com/espanso/espanso) a great project with very good extensions. It's written in python so it's easy for everyone to contribute.

## Installation

For instalation is necesary the module `pynput`

```python
pip install pynput
```

or

```python
pip3 install pynput
```

You should create a service for starting `Vxpand.py` every time the pc is turn on.
It will be fixed in next releases.

## Configuring keywords

For configure your keywords you should edit the file `keywords.py`. In this file is a dictionary in a variable
`words` where you can create al your desired keywords. Example:

```python
words = {
    ":pass": "Hol@ Mundo",
    ":nuevo": "viejo",
    ":azul": "rojo"
    }
```
Here we created a trigger `:pass` that is replaced by *Hol@ Mundo*
## License

Vxpand is licensed under the [GPL-3.0 license](/LICENSE).