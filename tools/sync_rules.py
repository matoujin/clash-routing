#!/usr/bin/env python3
"""Refresh only the public rule URLs explicitly listed in sources.json."""
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent.parent


def main():
    sources = json.loads((ROOT / "sources.json").read_text())
    pending = []
    for item in sources:
        dest = (ROOT / item["path"]).resolve()
        if not dest.is_relative_to(ROOT / "rules" / "upstream"):
            raise ValueError("Destination must be under rules/upstream")
        request = Request(item["url"], headers={"User-Agent": "clash-routing-rule-sync"})
        with urlopen(request, timeout=45) as response:
            data = response.read(8 * 1024 * 1024 + 1)
        if not 16 <= len(data) <= 8 * 1024 * 1024:
            raise ValueError("Unexpected file size: " + item["path"])
        # Published MRS files are Zstandard frames; full decoding is validated
        # separately with the installed Clash/Mihomo parser before release.
        if dest.suffix == ".mrs" and data[:4] != b"\x28\xb5\x2f\xfd":
            raise ValueError("Invalid compressed MRS header: " + item["path"])
        if dest.suffix == ".yaml":
            text = data.decode("utf-8")
            if "payload:" not in text or "<html" in text.lower():
                raise ValueError("Invalid rule YAML: " + item["path"])
        pending.append((dest, data))
    # Download and check every source before changing any tracked file.
    for dest, data in pending:
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists() or dest.read_bytes() != data:
            temp = dest.with_suffix(dest.suffix + ".tmp")
            temp.write_bytes(data)
            temp.replace(dest)
            print("Updated", dest.relative_to(ROOT))


if __name__ == "__main__":
    main()
