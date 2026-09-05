#!/usr/bin/env python3
"""
Generate a note.com article thumbnail using the Gemini API (Nano Banana 2).
Usage: python3 scripts/generate_thumbnail.py "<image prompt>" <output.png>
Reads GEMINI_API_KEY from .env in the repo root.
"""
import base64
import json
import os
import sys
import urllib.request

MODEL = "gemini-3.1-flash-image"


def load_api_key():
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    with open(env_path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY="):
                return line.strip().split("=", 1)[1]
    raise RuntimeError("GEMINI_API_KEY not found in .env")


def generate_image(prompt: str, output_path: str):
    api_key = load_api_key()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": api_key},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.load(resp)

    for candidate in data.get("candidates", []):
        for part in candidate.get("content", {}).get("parts", []):
            inline = part.get("inlineData") or part.get("inline_data")
            if inline and inline.get("data"):
                img_bytes = base64.b64decode(inline["data"])
                with open(output_path, "wb") as f:
                    f.write(img_bytes)
                print(f"Saved: {output_path} ({len(img_bytes)} bytes)")
                return
    raise RuntimeError(f"No image data in response: {json.dumps(data)[:500]}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 generate_thumbnail.py '<prompt>' <output.png>")
        sys.exit(1)
    generate_image(sys.argv[1], sys.argv[2])
