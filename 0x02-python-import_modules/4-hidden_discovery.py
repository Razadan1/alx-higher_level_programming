#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in sorted(dir(hidden_4)):
        if not i.startswith("__"):
            continue
        print(i)
