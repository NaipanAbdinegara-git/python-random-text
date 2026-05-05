import random, datetime, argparse

def random_gen(type, paragraphs):
    type += ".txt"
    try:
        with open(f"lang/{type}", "r", encoding="utf-8") as file:
            word_list = file.read().split()
            full_text = []
            for i in range(paragraphs):
                word_selected = random.choices(word_list, k=(random.randint(50, 150)))
                paragraphs_wrapped = " ".join(word_selected)
                full_text.append(paragraphs_wrapped)
            full_text_wrapped = ".\n\n".join(full_text)
            return full_text_wrapped
    except FileNotFoundError:
        print(f"File {type}.txt not found!")
        exit

def savetofile(text):
    with open("results.txt", "a", encoding="utf-8") as file:
        file.write(f"{text}\n")

def logs(log, action):
    with open("log.csv", "a") as file:
        date = datetime.datetime.now()
        logs = [date.strftime("%d/%m/%Y"), date.strftime("%H:%M:%S"), log, action]
        logs_csv = ",".join(logs)
        file.write(f"\n{logs_csv}")

def main():
    while True:
        try:
            print("Choose The Language:")
            print("1) EN 2) ID")
            print("3) RU 4) JP")
            user_lang = int(input("> "))
            user_paraf = int(input("How long the paragraph? > "))
            langs = {1: "en", 2: "id", 3: "ru", 4: "jp"}
            if user_lang in langs:
                print("-" * 25)
                text = random_gen(langs[user_lang], user_paraf)
                print(text)
                print("-" * 25)
                logs(f"Generate dummy text: {langs[user_lang]}", "succeed")
                print("Save to results.txt? (Y/N)")
                save = str(input("> "))
                if save.lower() == "y":
                    savetofile(text=text)
                    logs("Save the results to the results.txt file", "saved")
                else:
                    continue
            else:
                print(f"There is no {user_lang} in the option!")
        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            logs("Exit the program", "interrupted")
            print("Program Interrupted")
            break
        except EOFError:
            logs("Program Stopped", "EOFError")
            break

if __name__ == "__main__":
    main()