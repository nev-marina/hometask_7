import os
import readline


def merged_file():
    text = []
    texts_name = os.listdir("Дз 7/Files")

    for name in texts_name:
        with open(f"Дз 7/Files/{name}", encoding="utf-8") as f:
            lines = f.readlines()
            count_line = str(len(lines))
            lines_ = [name + "\n"] + [count_line + "\n"] + lines
            text.append(lines_)
    final_text = "".join(sum((sorted(text, key=len)), []))

    with open("Дз 7/result_dz7.txt", "w", encoding="utf-8") as f:
        f.write(final_text)


merged_file()