uppgifter = []


def visa_lista():
    print("\n--- Din att-göra-lista ---")
    if not uppgifter:
        print("Listan är tom!")
        return
    for i, uppgift in enumerate(uppgifter):
        status = "[x]" if uppgift["klar"] else "[ ]"
        print(f"{i + 1}. {status} {uppgift['text']}")
    print("--------------------------")


def lägg_till():
    text = input("Ange ny uppgift: ").strip()
    if not text:
        print("Uppgiften kan inte vara tom.")
        return
    if any(u["text"].lower() == text.lower() for u in uppgifter):
        print("Uppgiften finns redan i listan.")
        return
    uppgifter.append({"text": text, "klar": False})
    print(f'Uppgift "{text}" lades till.')


def ta_bort():
    visa_lista()
    if not uppgifter:
        return
    val = input("Ange numret på uppgiften du vill ta bort: ").strip()
    try:
        index = int(val) - 1
        if index < 0 or index >= len(uppgifter):
            print("Ogiltigt nummer. Försök igen.")
            return
        borttagen = uppgifter.pop(index)
        print(f'Uppgift "{borttagen["text"]}" togs bort.')
    except ValueError:
        print("Ange ett giltigt heltal.")


def markera_klar():
    visa_lista()
    if not uppgifter:
        return
    val = input("Ange numret på uppgiften du vill markera som klar: ").strip()
    try:
        index = int(val) - 1
        if index < 0 or index >= len(uppgifter):
            print("Ogiltigt nummer. Försök igen.")
            return
        uppgifter[index]["klar"] = True
        print(f'Uppgift "{uppgifter[index]["text"]}" markerades som klar.')
    except ValueError:
        print("Ange ett giltigt heltal.")


def sortera_lista():
    uppgifter.sort(key=lambda u: u["text"].lower())
    print("Listan sorterades alfabetiskt.")
    visa_lista()


def main():
    print("Välkommen till att-göra-listan!")
    while True:
        print("\nMeny:")
        print("1. Visa lista")
        print("2. Lägg till uppgift")
        print("3. Ta bort uppgift")
        print("4. Markera uppgift som klar")
        print("5. Sortera alfabetiskt")
        print("6. Avsluta")

        val = input("\nVälj ett alternativ (1–6): ").strip()

        if val == "1":
            visa_lista()
        elif val == "2":
            lägg_till()
        elif val == "3":
            ta_bort()
        elif val == "4":
            markera_klar()
        elif val == "5":
            sortera_lista()
        elif val == "6":
            print("Avslutar programmet. Hej då!")
            break
        else:
            print("Ogiltigt val. Ange ett nummer mellan 1 och 6.")


if __name__ == "__main__":
    main()