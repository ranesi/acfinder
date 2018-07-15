import os, re, requests, time, ui
from datetime import datetime, timedelta


def regex(text, fltr, s=''):

    r = re.compile(fltr)
    ret = r.sub(s, text)
    return ret


def get_key():

    with open(os.path.join('key.txt')) as f:
        ret = f.read()
    return regex(ret, '[^a-zA-Z0-9]')


def get_tz(lat: float, lon: float) -> None:
    """
        Uses Google Area Code API to determine
            -DST Offset
            -Raw offset (difference from UTC)
            -Timezone ID
            -Timezone Name
    """
    key = get_key()
    timestamp = time.time()
    api_res = requests.get(
        'https://maps.googleapis.com/maps/api/timezone/json?location={0},{1}&timestamp={2}&key={3}'.
        format(lat, lon, timestamp, key))
    api_res_dict = api_res.json()

    if api_res_dict['status'] == 'OK':
        offset = api_res_dict['dstOffset'] + api_res_dict['rawOffset']
        offset = offset / 60 / 60
        ltime = datetime.utcnow() + timedelta(hours=offset)
        id = api_res_dict['timeZoneId']
        name = api_res_dict['timeZoneName']
        ui.print_tz(id, name, ltime)
