# API

## Setup

Make a virtual environment based on **Python 3.8** (for TypedDict support).

With it activated:

    pip install -r requirements.txt

#### API Keys

You must add a `config.yaml` to this folder containing your API keys for News API and Indico.

Example:

```yaml
keys:
  indico: abc123
  newsapi: xyz789
```

## Running

#### (Optional) Enable debug mode

```console
foo@bar:~$ export FLASK_ENV=development
```

#### Start the Flask server

```console
foo@bar:~$ export FLASK_APP=api.py
foo@bar:~$ python -m flask run
```