#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys


def to_hex_string(text: str) -> str:
    """Converts a UTF-8 string into explicit U+XXXX space-separated hex codes."""
    return " ".join([f"U+{ord(ch):04X}" for ch in text])

def run_tests(cmd: str, manifest_path: str = "test_cases.json") -> bool:
    with open(manifest_path, "r", encoding="utf-8") as f:
        cases = json.load(f)

    passed = 0
    failed = 0

    print(f"\n==================================================")
    print(f" Running shave2tengwar Test Suite")
    print(f" Command: {cmd}")
    print(f" Total Cases: {len(cases)}")
    print(f"==================================================\n")

    for case in cases:
        cid = case["id"]
        cat = case["category"]
        inp = case["input"]
        exp_csur = case["expected_csur"]

        # Pipe Shavian input text to the binary/script standard input
        try:
            proc = subprocess.run(
                cmd,
                shell=True,
                input=inp,
                text=True,
                capture_output=True,
                check=True
            )
            act_csur = proc.stdout.rstrip("\r\n")
        except subprocess.CalledProcessError as e:
            print(f"❌ [{cid}] FAIL - Execution Error: {cat}")
            print(f"   Stderr: {e.stderr.strip()}")
            failed += 1
            continue

        if act_csur == exp_csur:
            print(f"✅ [{cid}] PASS: {cat}")
            passed += 1
        else:
            print(f"❌ [{cid}] FAIL: {cat}")
            print(f"   Input Shavian : '{inp}'")
            print(f"   Expected Hex  : {to_hex_string(exp_csur)}")
            print(f"   Actual Hex    : {to_hex_string(act_csur)}")
            failed += 1

    print("\n--------------------------------------------------")
    print(f" Summary: {passed} Passed, {failed} Failed")
    print("--------------------------------------------------\n")

    return failed == 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cross-language test runner for shave2tengwar.")
    parser.add_argument("--cmd", required=True, help="Command used to run the converter (e.g. 'python3 main.py' or './shave2tengwar_go')")
    parser.add_argument("--manifest", default="test_cases.json", help="Path to test_cases.json manifest")
    args = parser.parse_args()

    success = run_tests(args.cmd, args.manifest)
    sys.exit(0 if success else 1)
