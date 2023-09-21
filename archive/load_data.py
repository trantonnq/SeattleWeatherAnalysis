import weather_gov
import json

client = weather_gov.Client()

#print(client.alerts(limit=1))

data = client.get(endpoint="points/39.7456,-97.0892")
print(data)


json_object = json.dumps(data, indent=4)
with open("sample.json", "w") as outfile:
    outfile.write(json_object)