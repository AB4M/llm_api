#!/usr/bin/env python3
import sys
from google import genai
from google.genai import types

def main():
    if len(sys.argv) < 2:
        print("Usage: python explore.py <mood>")
        print("Example: python explore.py happy")
        return

    mood = " ".join(sys.argv[1:])

    client = genai.Client()

    prompt = (
        "你是一个根据用户心情返回颜文字表情的小助手。\n"
        "用户会给出一种心情，请你仅返回一个合适的颜文字（ASCII 颜文字即可），"
        "不要返回任何解释或其他文字。\n\n"
        f"用户的心情是：{mood}"
    )

    config = types.GenerateContentConfig(
        temperature=0.7,
    )

    resp = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=config,
    )

    print(resp.text)

if __name__ == "__main__":
    main()
