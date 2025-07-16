#!/usr/bin/env python3
import subprocess
import time
import random

RSS_FEEDS = [
    "https://www.reddit.com/r/technology/.rss",
    "https://www.theverge.com/rss/index.xml",
    "https://feeds.arstechnica.com/arstechnica/index",
    "https://www.wired.com/feed/rss",
    "https://feeds.feedburner.com/oreilly/radar/atom",
    "https://hnrss.org/frontpage",
    "https://www.zdnet.com/news/rss.xml",
    "https://blog.google/rss/",
    "https://www.nasa.gov/rss/dyn/breaking_news.rss",
]

URLS = [
    "https://en.wikipedia.org/wiki/Special:RandomInCategory/Technology",
    "https://opensource.com",
    "https://developer.mozilla.org/en-US/",
    "https://techcrunch.com",
    "https://www.kernel.org",
    "https://www.gnu.org/philosophy/free-sw.html",
]

TERMSAVER_MODES = [
    "asciiartfarts",
    "clock",
    "hacker",
    "matrix",
    "quotes4all",
    "rfc",
]


def run_termsaver(mode):
    if mode == "rssfeedreader":
        url = random.choice(RSS_FEEDS)
        cmd = f'termsaver rssfeedreader -u "{url}"'
    elif mode == "urlfetcher":
        url = random.choice(URLS)
        cmd = f'termsaver urlfetcher -u "{url}"'
    else:
        cmd = f"termsaver {mode}"

    print(f"Running: {cmd}")
    return subprocess.Popen(cmd, shell=True, start_new_session=True)


def kill_process(proc):
    print("Stopping current termsaver...")
    proc.terminate()


if __name__ == "__main__":
    while True:
        mode = random.choice(TERMSAVER_MODES + ["rssfeedreader", "urlfetcher"])
        proc = run_termsaver(mode)
        try:
            time.sleep(12 * 60 * 60)
        except KeyboardInterrupt:
            kill_process(proc)
            break
        kill_process(proc)
