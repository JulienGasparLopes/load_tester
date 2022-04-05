import requests
import json
import time
from statistics import mean
from helpers import get_token

# App info
API_URL = "https://dev.pickyourskills.com/api/v1/"


class LoadTester:
    def __init__(self, debug=False) -> None:
        self._token = get_token()
        self._headers = {"authorization": f"Bearer {self._token}"}
        self._base_url = API_URL

        self.debug = debug

    def _print(self, message):
        if self.debug:
            print(message)

    def post(self, url, data):
        headers = self._headers
        return requests.post(self._base_url + url, data=json.dumps(data), headers=headers)

    def get(self, url):
        headers = self._headers
        return requests.get(self._base_url + url, headers=headers)

    def get_time_isr_call(self):
        data = {
            "period": "week",
            "unit": "TO",
            "availability": {"start_date": "2019-01-01", "end_date": "2022-01-01"},
            "staffing_type": ["real", "simulated"],
        }
        start = time.time_ns()
        response = self.post(
            "staffing/users?page[size]=30&page[number]=0&sort=last_name", data
        )
        end = time.time_ns()
        delta = round((end - start) / 1000000)
        if response.status_code != 200:
            print(
                f"ERROR - Unable to retrieve ISR data : {response.status_code}")
        self._print(f"Request took {delta} ms")
        return delta

    def test_multiple_call(self, iteration_number):
        print(f"Start benchmarking of ISR with {iteration_number} calls")
        times = []
        for _ in range(0, iteration_number):
            current_time = self.get_time_isr_call()
            times.append(current_time)
        print(f"End benchmarking of ISR")
        min_time = min(times)
        max_time = max(times)
        mean_time = mean(times)
        return times, min_time, max_time, mean_time
