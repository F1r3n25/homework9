CONTACTS = {}


def input_error(wrap):
    def inner(*args):
        try:
            return wrap(*args)
        except IndexError:
            return "Give me name and phone please"
        except KeyError:
            return "Enter correct name of contact or add new one please"
        except ValueError:
            return "Enter correct number of phone"
    return inner


@input_error
def add_handler(data):
    name = data[0].title()
    if int(data[1]) or data[1].startswith("+"):
        phone = data[1]
    CONTACTS[name] = phone
    return f"Contact {name} with phone {phone} was succesfully added"


@input_error
def change_handler(data):
    name = data[0].title()
    if int(data[1]) or data[1].startswith("+"):
        phone = data[1]
    if name in CONTACTS:
        CONTACTS[name] = phone
        return f"Contact {name} was succesfully updated with number {phone}"
    else:
        return f"Contact {name} is absent and can not be updated"


def show_handler(*args):
    return f"Phonebook: {CONTACTS}"


def exit_handler(*args):
    global bot_activity
    return "Good bye!"


def hello_handler(*args):
    return "Hello :)\nHow can I help you?"


@input_error
def phone_handler(data):
    name = data[0].title()
    return CONTACTS[name]


def command_parser(scratchstr: str):
    elements = scratchstr.split()
    for key, value in commands.items():
        if elements[0].lower() in value:
            return key, elements[1:]
    if len(elements) > 1:
        for key, value in commands.items():
            if f"{elements[0]} {elements[1]}" in value:
                return key, elements[2:]


commands = {
    add_handler: ["add", "+"],
    exit_handler: ["good bye", "close", "exit"],
    hello_handler: ["hello"],
    show_handler: ["show all"],
    phone_handler: ["phone"],
    change_handler: ["change"],
}


def main():
    while True:
        enter = input("Waiting for command: ")
        if not enter:
            continue
        try:
            func, data = command_parser(enter)
            result = func(data)
            print(result)
            if func == exit_handler:
                break
        except TypeError:
            print("This command is no exist. Try again")


if __name__ == "__main__":
    main()
