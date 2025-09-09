import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("MONKEYTYPE_API_KEY")

headers = {
    'Authorization': f'ApeKey {API_KEY}'
}

# GET request for MonkeyType STATS
stats_response = requests.get(f'https://api.monkeytype.com/users/stats', headers=headers)

# Check request response
if stats_response.status_code != 200:
    print(f"Stats API error (Status {stats_response.status_code}): {stats_response.text}")
    exit(1)

stats_data = stats_response.json()
completed_tests = stats_data['data']['completedTests']


def get_personal_best(mode, mode2, duration):
    params = {
        'mode': mode,
        'mode2': mode2
    }

    response = requests.get('https://api.monkeytype.com/users/personalBests', headers=headers, params=params)

    if response.status_code != 200:
        print(f"Personal Best ({duration}) API error (Status {response.status_code}): {response.text}")
        return None
    
    data = response.json()

    # Check that data is not empty
    if 'data' not in data or not data['data']:
        # print(f"No personal best data available for {duration}")
        return None

    # Data is returned in list form, so get first entry
    entry = data['data'][0]

    return {
        'accuracy': entry['acc'],
        'difficulty': entry['difficulty'],
        'wpm': entry['wpm']
    }

pb15 = get_personal_best('time', '15', '15s')
pb30 = get_personal_best('time', '30', '30s')
pb60 = get_personal_best('time', '60', '60s')

print(f"Completed: {completed_tests}")

if pb15:
    print(f"\n15 second PB")
    print(f"WPM: {pb15['wpm']}")
    print(f"Accuracy: {pb15['accuracy']}%")
else:
    print("\n15 second PB: No data available")

if pb30:
    print(f"\n30 second PB")
    print(f"WPM: {pb30['wpm']}")
    print(f"Accuracy: {pb30['accuracy']}%")
else:
    print("\n30 second PB: No data available")

if pb60:
    print(f"\n60 second PB")
    print(f"WPM: {pb60['wpm']}")
    print(f"Accuracy: {pb60['accuracy']}%")
else:
    print("\n60 second PB: No data available")

