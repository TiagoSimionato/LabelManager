import json
from os import path

from pydantic import BaseModel

PREFS_PATH = 'prefs.json'


class Prefs(BaseModel):
  deleteZip: bool
  openPdf: bool
  zipPath: str
  outputPath: str


def make_default_prefs():
  default_prefs = {
    'deleteZip': True,
    'openPdf': True,
    'zipPath': '',
    'outputPath': '',
  }
  if not path.exists(PREFS_PATH):
    with open(PREFS_PATH, 'w') as file:
      json.dump(default_prefs, file)
  return default_prefs


def get_prefs():
  if not path.exists(PREFS_PATH):
    prefs_dic = make_default_prefs()
  else:
    with open(PREFS_PATH, 'r') as file:
      prefs_dic = json.load(file)
      print()
  return Prefs(**prefs_dic)


def change_prefs(prefs: Prefs, key: str, value):
  new_prefs_dict = prefs.model_dump()
  new_prefs_dict[key] = value
  with open(PREFS_PATH, 'w') as file:
    json.dump(new_prefs_dict, file)
  prefs = Prefs(**new_prefs_dict)
  return prefs


PREFS = get_prefs()
