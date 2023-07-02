## Setup

### Virtual env

```wsl
    sudo apt update
    sudo apt upgrade
    sudo apt install python3-venv
    python3 -m venv venv
    source venv/bin/activate
```

### spacy

```wsl
    pip install -U pip setuptools wheel
    pip install -U spacy
    python3 -m spacy download en_core_web_sm
```

## Links

1. https://stackoverflow.com/questions/75131112/how-to-install-python3-10-virtual-environment-when-python3-10-venv-has-no-instal (note use the command `sudo apt update` and `sudo apt upgrade` instead)
2. https://spacy.io/usage
