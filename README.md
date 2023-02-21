# Amenitiz © Data Engineer challenge 1
- Name: Aleix Paradell
- Position: Data Engineer
- Date: February 2023
- [Challenge Instructions](challenge_instructions.md)


## Initial Set Up
1. Clone this repo `git clone git@github.com:paradell/taxdown-coding-challenge.git`
2. Install the latest **Python 3.8.X** version. To easily switch between Python versions, it is recommended to use [pyenv](https://github.com/pyenv/pyenv) or [virtualenv](https://virtualenv.pypa.io/en/latest/).
    - `pyenv install 3.8.X` (use the appropriate version)
    - `pyenv local 3.8.X`
    - Check Python version with `python --version`.
3. Install developer libraries
```bash
python -m pip install --upgrade pip
python -m pip install -r dev-requirements.txt
```
4. Install project libraries
```bash
python -m pip install -r requirements.txt
```
5. Install pre-commit configurations
```bash
pre-commit install
```

## Extract data from Open Trip Map
1. Have an Open Trip Map account.
2. Store the Open Trip Map API KEY as a Environment Variable
```bash
export OPENTRIPMAP_APIKEY={your_api_key}`
```
3. Run the data extraction code.
```bash
python open_trip_map_data/data_extraction.py
```
