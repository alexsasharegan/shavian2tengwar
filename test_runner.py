#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys


def to_hex_string(text: str) -> str:
    """Converts a UTF-8 string into explicit U+XXXX space-separated hex codes."""
    return " ".join([f"U+{ord(ch):04X}" for ch in text])


def run_tests(cmd: str, manifest_path: str = "test_cases_everson_3.json") -> bool:
    with open(manifest_path, "r", encoding="utf-8") as f:
        cases = json.load(f)

    passed = 0
    failed = 0

    print("\n==================================================")
    print(" Running shave2tengwar Extended Test Suite")
    print(f" Command Base: {cmd}")
    print(f" Total Cases : {len(cases)}")
    print("==================================================\n")

    for case in cases:
        cid = case["id"]
        cat = case["category"]
        inp = case["input"]
        exp_csur = case["expected_csur"]
        flags = case.get("flags", "").strip()

        # Build execution command with case-specific flags if present
        exec_cmd = f"{cmd} {flags}".strip() if flags else cmd

        try:
            proc = subprocess.run(
                exec_cmd,
                shell=True,
                input=inp,
                text=True,
                capture_output=True,
                check=True,
            )
            act_csur = proc.stdout.rstrip("\r\n")
        except subprocess.CalledProcessError as e:
            print(f"❌ [{cid}] FAIL - Execution Error: {cat}")
            print(f"   Stderr: {e.stderr.strip()}")
            failed += 1
            continue

        if act_csur == exp_csur:
            flag_notice = f" (Flags: {flags})" if flags else ""
            print(f"✅ [{cid}] PASS: {cat}{flag_notice}")
            passed += 1
        else:
            print(f"❌ [{cid}] FAIL: {cat}")
            print(f"   Flags Used    : '{flags}'")
            print(f"   Input Shavian : '{inp}'")
            print(f"   Expected Hex  : {to_hex_string(exp_csur)}")
            print(f"   Actual Hex    : {to_hex_string(act_csur)}")
            failed += 1

    print("\n--------------------------------------------------")
    print(f" Summary: {passed} Passed, {failed} Failed")
    print("--------------------------------------------------\n")

    return failed == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Cross-language test runner for shave2tengwar."
    )
    parser.add_argument(
        "--cmd",
        required=True,
        help="Command used to run converter (e.g. 'python3 shavian2tengwar.py')",
    )
    parser.add_argument(
        "--manifest",
        default="test_cases_everson_3.json",
        help="Path to test manifest JSON file",
    )
    args = parser.parse_args()

    success = run_tests(args.cmd, args.manifest)
    sys.exit(0 if success else 1)
