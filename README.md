# studocu_coursehero_pwner

## what it does
generates 10 random essays for you to upload to coursehero/studocu. Files are saved as .doc files.

## how to build
- `python -m venv myenv`
- `source myenv/bin/activate`
- `pip install -r requirements.txt`
- duplicate `.env_excample` and name the copy `.env`
- fill out `API_KEY=` value with your OpenAI api key 

## script usage
- `python ./pwner.py`
to generate 10 essays at a time
