from load_tester import LoadTester
from slack_connector import SlackConnector


def main():
    charge_tester = LoadTester()
    charge_tester.debug = True

    slack_connector = SlackConnector()
    slack_connector.send_message(
        "My message", "Un super message quand même !!!")

    return

    iteration_number = 10
    _, min_time, max_time, mean_time = charge_tester.test_multiple_call(
        iteration_number
    )
    print(
        f"Called ISR {iteration_number} times, took {mean_time}ms average, with [min, max]: [{min_time}, {max_time}]"
    )


if __name__ == "__main__":
    main()
