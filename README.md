# Developing your app

This README specifically refers to how to develop your app.

---

## Contents

- [1. Installing app dependencies](#1-installing-app-dependencies)
- [2. Developing your app](#2-developing-your-app)


## 1. Installing app dependencies

A python `requirements.txt` file is provided to install with the standard packages that we use.

```
pip install -r requirements.txt
```

### Python Virtual Environment - optional alternative

Throughout these instructions, we will use `Makefile` commands, that have been built to simplify the process. You can open the `Makefile` to see what is happening under the hood of each command

Virtual environments help make sure that apps on your computer work as intended on someone elses.

You can create the virtual environment and install the project packages by running:

```
make venv
```

To enter the virtual env:

```
source .venv/bin/activate
```

Other useful commands:

- `make reqs` - This installs the packages in `requirements.txt` and should only be run inside a virtual environment.
- `deactivate` - This exits the current virtual environment.


## 2. Developing your app

#### Viewing changes locally

As you develop the code in your app, you can view the changes you make by running the app locally. To run the app, in your virtual environment run: `python main.py`.

This will load the app and you will be able to see your app at: `http://localhost:8080`

Any code changes will force the app to refresh to reflect.
