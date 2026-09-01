from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parent.parent
TARGET_FILE = "test-project/app.py"

EXPECTED_GREETING = "Hello, Simay! Welcome to the project."


def read_file(path):
    return (ROOT / path).read_text()


def run_qwen(prompt):
    result = subprocess.run(
        ["ollama", "run", "qwen2.5-coder-32k:latest"],
        input=prompt,
        text=True,
        capture_output=True
    )

    if result.returncode != 0:
        raise RuntimeError(result.stderr)

    return result.stdout
def run_coding_agent(task, current_code):
    coding_rules = read_file("agents/CODING_AGENT.md")
    project_rules = read_file("AGENTS.md")

    prompt = f"""
You are acting ONLY as the Coding Agent.

## PROJECT RULES
{project_rules}

## CODING AGENT RULES
{coding_rules}

## TASK
{task}

## CURRENT FILE
{current_code}

Modify only `{TARGET_FILE}`.

Return the complete updated Python file between these exact markers:

<<<FILE>>>
complete updated Python file
<<<END_FILE>>>

Do not perform testing.
Do not perform code review.
Do not commit or push.
Do not modify unrelated files.
"""

    print("\n=== CODING AGENT ===")

    response = run_qwen(prompt)
    print(response)

    return response
def run_test_agent():
    test_rules = read_file("agents/TEST_AGENT.md")
    project_rules = read_file("AGENTS.md")
    task = read_file("task.md")
    current_code = read_file(TARGET_FILE)

    prompt = f"""
You are acting ONLY as the Test Agent.

## PROJECT RULES
{project_rules}

## TEST AGENT RULES
{test_rules}

## TASK
{task}

## CURRENT FILE
{current_code}

Your job is to verify the implementation.

Do not modify code.
Do not perform code review.
Do not commit or push.

Return exactly one final status on its own line:

PASS
FAIL
BLOCKED
"""

    print("\n=== TEST AGENT ===")

    response = run_qwen(prompt)
    print(response)

    lines = [line.strip() for line in response.splitlines() if line.strip()]

    for line in reversed(lines):
        if line in {"PASS", "FAIL", "BLOCKED"}:
            return line

    return "BLOCKED"
def run_browser_test():
    result = subprocess.run(
        ["python3", "browser-test/test_browser.py"],
        cwd=ROOT,
        text=True,
        capture_output=True
    )

    print("\n=== BROWSER TEST ===")
    print(result.stdout)

    if result.returncode == 0 and "Browser Test Result: PASS" in result.stdout:
        print("Browser Test Status: PASS")
        return True
def run_desktop_test():
    result = subprocess.run(
        ["python3", "desktop-test/test_desktop.py"],
        cwd=ROOT,
        text=True,
        capture_output=True
    )

    print("\n=== DESKTOP TEST ===")
    print(result.stdout)

    if result.returncode == 0 and "Desktop Test Result: PASS" in result.stdout:
        print("Desktop Test Status: PASS")
        return True

    print(result.stderr)
    print("Desktop Test Status: FAIL")
    return False
    print(result.stderr)
    print("Browser Test Status: FAIL")
    return False

def run_git_agent():
    git_rules = read_file("agents/GIT_AGENT.md")
    project_rules = read_file("AGENTS.md")

    print("\n=== GIT AGENT ===")
    print("Git Agent rules loaded.")

    commit_success = create_git_commit()

    if not commit_success:
        print("Git Agent Status: FAILED")
        return "FAILED"

    push_success = push_to_remote()

    if not push_success:
        print("Git Agent Status: FAILED")
        return "FAILED"

    print("Git Agent Status: COMPLETE")
    return "COMPLETE"

def extract_code(response):
    start_marker = "<<<FILE>>>"
    end_marker = "<<<END_FILE>>>"

    if start_marker in response and end_marker in response:
        code = response.split(start_marker, 1)[1]
        code = code.split(end_marker, 1)[0]
        return code.strip() + "\n"

    if "```python" in response:
        code = response.split("```python", 1)[1]
        code = code.split("```", 1)[0]
        return code.strip() + "\n"

    raise ValueError("Qwen kodu beklenen formatta vermedi.")

def apply_code_change(new_code):
    target = ROOT / TARGET_FILE

    print("\n=== APPLYING CODE CHANGE ===")
    print(f"Updating: {TARGET_FILE}")

    target.write_text(new_code)

    print("Code change applied.")


def verify_app():
    result = subprocess.run(
        ["python3", TARGET_FILE],
        cwd=ROOT,
        input="Simay\n",
        text=True,
        capture_output=True
    )

    output = result.stdout.strip()

    print("\n=== VERIFICATION ===")
    print(output)

    if EXPECTED_GREETING in output:
        print("Verification Result: PASS")
        return True

    print("Verification Result: FAIL")
    return False
def get_git_diff():
    result = subprocess.run(
        ["git", "diff", "--", TARGET_FILE],
        cwd=ROOT,
        text=True,
        capture_output=True
    )
    return result.stdout


def run_code_review():
    review_rules = read_file("agents/CODE_REVIEW.md")
    project_rules = read_file("AGENTS.md")
    task = read_file("task.md")
    diff = get_git_diff()
    current_code = read_file(TARGET_FILE)

    prompt = f"""
You are acting ONLY as the Code Review Agent.

## PROJECT RULES
{project_rules}

## REVIEW RULES
{review_rules}

## ORIGINAL TASK
{task}

## CODE CHANGE
{diff}

## CURRENT IMPLEMENTATION
{current_code}

Verification has already passed.

Review only the provided change.
Do not modify code.

End your response with exactly one of these decisions on its own line:

APPROVE
REQUEST CHANGES
BLOCKED
"""

    print("\n=== CODE REVIEW AGENT ===")

    response = run_qwen(prompt)
    print(response)

    lines = [line.strip() for line in response.splitlines() if line.strip()]

    for line in reversed(lines):
        if line in {"APPROVE", "REQUEST CHANGES", "BLOCKED"}:
            return line

    return "BLOCKED"
def create_git_commit():
    status_result = subprocess.run(
        ["git", "status", "--porcelain", TARGET_FILE],
        cwd=ROOT,
        text=True,
        capture_output=True
    )

    if not status_result.stdout.strip():
        print("\n=== GIT COMMIT ===")
        print("Nothing to commit for target file.")
        print("Commit Result: SKIPPED")
        return True

    result = subprocess.run(
        ["git", "add", TARGET_FILE],
        cwd=ROOT,
        text=True,
        capture_output=True
    )

    result = subprocess.run(
        ["git", "commit", "-m", "Update greeting through AI pipeline"],
        cwd=ROOT,
        text=True,
        capture_output=True
    )

    print("\n=== GIT COMMIT ===")
    print(result.stdout)

    if result.returncode == 0:
        print("Commit Result: SUCCESS")
        return True

    print(result.stderr)
    print("Commit Result: FAIL")
    return False
def push_to_remote():
    result = subprocess.run(
        ["git", "push", "origin", "main"],
        cwd=ROOT,
        text=True,
        capture_output=True
    )

    print("\n=== GIT PUSH ===")
    print(result.stdout)

    if result.returncode == 0:
        print("Push Result: SUCCESS")
        return True

    print(result.stderr)
    print("Push Result: FAIL")
    return False
def push_to_remote():
    result = subprocess.run(
        ["git", "push", "origin", "main"],
        cwd=ROOT,
        text=True,
        capture_output=True
    )

    print("\n=== GIT PUSH ===")
    print(result.stdout)

    if result.returncode == 0:
        print("Push Result: SUCCESS")
        return True

    print(result.stderr)
    print("Push Result: FAIL")
    return False
def create_github_issue():
    result = subprocess.run(
        [
            "gh",
            "issue",
            "create",
            "--title",
            "Automated pipeline task",
            "--body",
            "This issue was created automatically by the AI pipeline."
        ],
        cwd=ROOT,
        text=True,
        capture_output=True
    )

    print("\n=== GITHUB ISSUE ===")
    print(result.stdout)

    if result.returncode == 0:
        issue_url = result.stdout.strip()
        print("Issue Result: SUCCESS")
        print(f"Issue URL: {issue_url}")
        return issue_url

    print(result.stderr)
    print("Issue Result: FAIL")
    return False
def add_issue_comment(issue_url, message):
    result = subprocess.run(
        [
            "gh",
            "issue",
            "comment",
            issue_url,
            "--body",
            message
        ],
        cwd=ROOT,
        text=True,
        capture_output=True
    )

    print("\n=== ISSUE COMMENT ===")
    print(result.stdout)

    if result.returncode == 0:
        print("Comment Result: SUCCESS")
        return True

    print(result.stderr)
    print("Comment Result: FAIL")
    return False
def close_github_issue(issue_url):
    result = subprocess.run(
        [
            "gh",
            "issue",
            "close",
            issue_url,
            "--comment",
            "Final Status: RESOLVED\n\nPipeline completed successfully."
        ],
        cwd=ROOT,
        text=True,
        capture_output=True
    )

    print("\n=== ISSUE CLOSE ===")
    print(result.stdout)

    if result.returncode == 0:
        print("Issue Close Result: SUCCESS")
        return True

    print(result.stderr)
    print("Issue Close Result: FAIL")
    return False


def main():
    task = read_file("task.md")
    current_code = read_file(TARGET_FILE)

    issue_url = create_github_issue()

    if not issue_url:
        print("Pipeline Status: ISSUE CREATION FAILED")
        return

    print("=== PRE-VERIFICATION ===")

    if not verify_app():
        print("Current implementation does not pass verification.")

        response = run_coding_agent(task, current_code)
        new_code = extract_code(response)
        apply_code_change(new_code)

    verification_passed = verify_app()

    if not verification_passed:
        print("\nPipeline Status: VERIFICATION FAILED")
        return

    browser_test_passed = run_browser_test()

    if not browser_test_passed:
        print("\nPipeline Status: BROWSER TEST FAILED")
        return
    desktop_test_passed = run_desktop_test()

    if not desktop_test_passed:
        print("\nPipeline Status: DESKTOP TEST FAILED")
        return

    add_issue_comment(
        issue_url,
        "Progress Update\n\n- Verification: PASS\n- Browser Test: PASS\n- Desktop Test: PASS\n- Current Status: READY FOR TESTING"
)



    test_status = run_test_agent()

    if test_status != "PASS":
        if test_status == "FAIL":
            print("\nPipeline Status: TEST AGENT FAILED")
        else:
            print("\nPipeline Status: TEST AGENT BLOCKED")
        return

    add_issue_comment(
        issue_url,
        "Progress Update\n\n- Test Agent: PASS\n- Current Status: READY FOR REVIEW"
    )

    review_decision = run_code_review()

    add_issue_comment(
        issue_url,
        f"Progress Update\n\n- Review Decision: {review_decision}\n- Current Status: REVIEW COMPLETED"
    )

    print(f"\nReview Decision: {review_decision}")

    if review_decision == "REQUEST CHANGES":
        print("\nPipeline Status: CHANGES REQUESTED")
        return

    if review_decision == "BLOCKED":
        print("\nPipeline Status: BLOCKED")
        return

    git_status = run_git_agent()

    if git_status != "COMPLETE":
        print("\nPipeline Status: GIT AGENT FAILED")
        return

    add_issue_comment(
        issue_url,
        "Progress Update\n\n- Git Agent: COMPLETE\n- Current Status: READY TO CLOSE"
    )

    close_github_issue(issue_url)

    print("\nPipeline Status: COMPLETE")


if __name__ == "__main__":
    main()
