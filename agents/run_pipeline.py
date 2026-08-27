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
    subprocess.run(
        ["git", "add", TARGET_FILE],
        cwd=ROOT,
        check=True
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
    print("Commit Result: FAILED")
    return False


def main():
    project_rules = read_file("AGENTS.md")
    pipeline_rules = read_file("agents/PIPELINE.md")
    task = read_file("task.md")
    current_code = read_file(TARGET_FILE)
    print("=== PRE-VERIFICATION ===")

    if verify_app():
        print("Current implementation already passes verification.")
        review_decision = run_code_review()

        print(f"\nReview Decision: {review_decision}")

        if review_decision == "APPROVE":
            commit_success = create_git_commit()

        if commit_success:
            print("Pipeline Status: COMPLETE")
        else:
            print("Pipeline Status: COMMIT FAILED")

    elif review_decision == "REQUEST CHANGES":
        print("Pipeline Status: CHANGES REQUESTED")

    else:
        print("Pipeline Status: BLOCKED")

    return

    prompt = f"""
## PROJECT RULES
{project_rules}

## PIPELINE RULES
{pipeline_rules}

## TASK
{task}

## CURRENT FILE
{current_code}

Modify only `{TARGET_FILE}`.

Return the complete updated file between these exact markers:

<<<FILE>>>
complete Python file here
<<<END_FILE>>>

Do not include markdown code fences inside the markers.
Keep the change minimal.
Do not modify unrelated behavior.
"""

    print("=== CODING AGENT ===")

    response = run_qwen(prompt)

    print(response)

    new_code = extract_code(response)

    apply_code_change(new_code)

    verification_passed = verify_app()

    if verification_passed:
        print("\nPipeline Status: READY FOR REVIEW")
    else:
        print("\nPipeline Status: VERIFICATION FAILED")


if __name__ == "__main__":
    main()
