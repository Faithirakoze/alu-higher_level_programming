#!/usr/bin/python3
import hidden_4


if __name__ == "__main__":
    content = dir(hidden_4)
    count = len(content)
    names = [name for name in content if not name.startswith("__")]
    for i sorted(names):
        print(i)
