def input_error(func):

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command"
        except Exception as e:
            return f"An error occurred: {e}"
    return inner


@input_error
def add_contact(args, contacts):

    if len(args) != 2:
        raise ValueError
    
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):

    if len(args) != 2:
        raise ValueError
    
    name, phone = args
    if name not in contacts:
        raise KeyError
    
    contacts[name] = phone
    return "Contact updated."


@input_error
def get_phone(args, contacts):

    if not args:
        raise IndexError
    
    name = args[0]
    if name not in contacts:
        raise KeyError
    
    return contacts[name]


@input_error
def show_all(args, contacts):

    if not contacts:
        return "No contacts saved."
    
    result = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return result


def parse_command(user_input):

    parts = user_input.strip().split()
    if not parts:
        return None, []
    
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    commands = {
        "add": add_contact,
        "change": change_contact,
        "phone": get_phone,
        "all": show_all,
        "exit": lambda *_: "Good bye!",
        "close": lambda *_: "Good bye!",
        "hello": lambda *_: "How can I help you?",
    }
    
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_command(user_input)
        
        if not command:
            print("Please enter a command.")
            continue
        
        if command in ["exit", "close"]:
            print(commands[command](args, contacts))
            break
        
        if command not in commands:
            print("Unknown command.")
            continue
        
        result = commands[command](args, contacts)
        print(result)


if __name__ == "__main__":
    main()