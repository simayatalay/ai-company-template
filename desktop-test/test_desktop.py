import subprocess


def run_desktop_test():
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

    if active_app == "Code":
        print("Desktop Test Result: PASS")
        return True

    print("Desktop Test Result: FAIL")
    return False


if __name__ == "__main__":
    run_desktop_test()