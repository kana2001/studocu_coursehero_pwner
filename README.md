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
- `./run.sh`
- or to generate one essay at a time: `python ./pwner.py`
