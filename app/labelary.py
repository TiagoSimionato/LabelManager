from typing import Literal

import requests

LABELARY_API_URL = 'https://api.labelary.com/v1'


def convert_zpl(
  zpl: str,
  output_type: Literal['png', 'pdf'] = 'png',
  resolution: Literal[6, 8, 12, 24] = 8,
  width: int = 4,
  height: int = 6,
  index: int | None = None,
):
  url = f'{LABELARY_API_URL}/printers/{resolution}dpmm/labels/{width}x{height}/'
  if output_type == 'png' or index is not None:
    url += f'{index}/'

  headers = {
    'Accept': {'pdf': 'application/pdf', 'png': 'image/png'}[output_type.lower()],
    'Content-Type': 'application/x-www-form-urlencoded',
  }

  resp = requests.post(url, data=zpl, headers=headers)
  if resp.status_code == 200 and (output_type == 'pdf' or index is not None):
    return [resp.content]
  elif resp.status_code == 200:
    count = int(resp.headers['x-total-count'])
    labels = [resp.content]
    for i in range(1, count):
      labels += convert_zpl(zpl, output_type, resolution, width, height, i)
    return labels
  else:
    return []


def zpl_to_pdf(zpl: str, index: int | None = None):
  return convert_zpl(zpl, 'pdf', index=index)


def zpl_to_png(zpl: str, index: int | None = None):
  return convert_zpl(zpl, index=index)
