from src.core import obfuscate_keep

if __name__ == "__main__":
    hanzi = open("data\\hanzi.txt", mode="r", encoding="utf-8").read()
    kanji = open("data\\kanji.txt", mode="r", encoding="utf-8").read()
    print(
        obfuscate_keep(
            plain_text=hanzi,
            shadow_text=kanji,
            filename="LiveMaker",
            suffix="LiveMaker",
            target_path=".",
        )
    )
