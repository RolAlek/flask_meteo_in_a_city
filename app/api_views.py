from flask import jsonify
import json

from . import app
from app.models import SearchHistory


@app.route('/api/history', methods=['GET'])
def get_history():
    history = SearchHistory.query.all()
    result = {}
    for item in history:
        if item.city not in result:
            result[item.city] = item.count
        else:
            result[item.city] += item.count
    return jsonify(result), 200




