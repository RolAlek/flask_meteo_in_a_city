import os

import requests
from dotenv import load_dotenv
from opencage.geocoder import OpenCageGeocode

from app.models import SearchHistory

from . import db

load_dotenv()


geocoder = OpenCageGeocode(os.getenv("GEOCODE_KEY"))


def get_coordinates(city):
    result = geocoder.geocode(city)
    if result:
        return result[0]["geometry"]["lat"], result[0]["geometry"]["lng"]
    return


def get_weather_data(coordinates):
    lat, lng = coordinates
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={lat}&"
        f"longitude={lng}&hourly=temperature_2m"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return


def save_search(city, user_id):
    search = SearchHistory.query.filter_by(
        city=city,
        user_id=user_id,
    ).first()
    if search:
        search.count += 1
    else:
        search = SearchHistory(city=city, user_id=user_id, count=1)
        db.session.add(search)
    db.session.commit()
