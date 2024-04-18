## Install requirements

- Python 3.12.2
- Git

## Getting Started

1. Clone

```sh
git clone https://github.com/Blankeos/sanic-sqlite.git
```

2. Create a virtual environment

```sh
python -m .venv venv
```

3. Install requirements

```sh
pip install -r requirements.txt
```

4. Run the app

```sh
# For running in production.
sanic main --host=0.0.0.0

# If you're developing
sanic main --host=0.0.0.0 --reload
```
