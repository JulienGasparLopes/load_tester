from load_tester import LoadTester
from mongo_connector import MongoConnector
from slack_connector import SlackConnector


def main():
    mongo_connector = MongoConnector("load_tester")
    charge_tester = LoadTester(debug=True)
    slack_connector = SlackConnector()

    iteration_number = 10
    values, min_time, max_time, mean_time = charge_tester.test_multiple_call(
        iteration_number
    )
    mongo_connector.insert_documents("run", [{"values": values}])
    print(
        f"Called ISR {iteration_number} times, took {mean_time}ms average, with [min, max]: [{min_time}, {max_time}]"
    )


if __name__ == "__main__":
    main()
