import argparse
from engine import random_gen, savetofile, logs

def main():
    parser = argparse.ArgumentParser(description="Random Text Generator On Python")
    parser.add_argument("--lang", type=str, required=True, help="Choose the language (en/id/ru/jp)")
    parser.add_argument("--p", type=int, required=True, help="The long of the random text")

    args = parser.parse_args()
    text = random_gen(args.lang, args.p)
    print(text)
    logs(f"Generate dummy text: {args.lang}", "succeed")
    try:
        print("Save to results.txt? (Y/N)")
        save = str(input("> "))
        if save.lower() == "y":
            savetofile(text=text)
            logs("Save the results to the results.txt file", "saved")
        else:
            exit()
    except KeyboardInterrupt:
        print("\nProgram Interrupted.")
        exit()
    except Exception as e:
        print("Something went wrong!")
        print(f"Error: {e}")
        exit()

if __name__ == "__main__":
    main()