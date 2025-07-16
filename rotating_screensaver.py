#!/usr/bin/env python3
import subprocess
import time
import random

SCREENSAVERS = [
    "cmatrix",
    "hollywood",
    "sl",
    "bb",
    "cacafire",
    "aafire",
    "cbonsai",
    "nyancat",
]


def run_screensaver(cmd):
    print(f"Starting: {cmd}")
    return subprocess.Popen(cmd, shell=True, start_new_session=True)


def kill_process(proc):
    print("Killing current screensaver...")
    proc.terminate()


if __name__ == "__main__":
    while True:
        screensaver = random.choice(SCREENSAVERS)
        proc = run_screensaver(screensaver)
        try:
            time.sleep(12 * 60 * 60)  # 12 hours
        except KeyboardInterrupt:
            kill_process(proc)
            break
        kill_process(proc)
