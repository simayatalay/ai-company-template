import subprocess
import time


def run_desktop_test():
    subprocess.run(
        [
            "osascript",
            "-e",
            'tell application "QGIS" to activate'
        ],
        text=True,
        capture_output=True
    )

    time.sleep(2)

    result = subprocess.run(
        [
            "osascript",
            "-e",
            'tell application "System Events" to get name of first application process whose frontmost is true'
        ],
        text=True,
        capture_output=True
    )

    active_app = result.stdout.strip()

    print(f"Active Application: {active_app}")

    
    window_result = subprocess.run(
        [
            "osascript",
            "-e",
            'tell application "System Events" to tell process "QGIS" to get name of every window'
        ],
        text=True,
        capture_output=True
    )

    windows = window_result.stdout

    print(f"QGIS Windows: {windows}")

    expected_window = "Institution Plugin Template - Widget Examples"

    if active_app == "QGIS" and expected_window in windows:
        print("Desktop Test Result: PASS")
        return True

    print("Desktop Test Result: FAIL")
    return False


if __name__ == "__main__":
    run_desktop_test()