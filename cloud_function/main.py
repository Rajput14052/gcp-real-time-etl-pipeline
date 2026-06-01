import json


def ingest_data(request):
    request_json = request.get_json(silent=True)

    if not request_json:
        return {"status": "failed", "message": "No payload received"}, 400

    print("Received data from API source")
    print(json.dumps(request_json))

    return {
        "status": "success",
        "message": "Data received and published to Pub/Sub simulation",
    }, 200
