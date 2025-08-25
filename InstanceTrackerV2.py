from time import sleep
from datetime import datetime
from colorama import Fore


inv_put = (Fore.RED+
           "\n\n| Invalid Input!"
           +Fore.CYAN)


while True:
    menu_prompt = input(
        Fore.CYAN+
        "\n\n! | Select an option by number!"
        "\n\n1. | Log Instances!"
        "\n2. | View Logged Instances!"
        "\n3. | Clear Logged Instances!"
        "\n4. | Exit!"
        "\n\n> "
    )

    if menu_prompt == "1":
        while True:
            instance_id = input(
                "\n\n| Enter Instance Name & ID or press 'ENTER' to return to menu!"
                "\n| ( Ex: 'World Name #12345' )"
                "\n\n| > "
            ).lower()
            if instance_id.strip() == "":
                print(inv_put)
                sleep(2)
                continue
            while True:
                confirm_prompt = input(
                    "\n\n| Does this entry look correct? ( Y / N )"
                    +Fore.YELLOW+
                    f"\n\n| {instance_id}"
                    +Fore.CYAN+
                    "\n\n> "
                ).upper()
                if confirm_prompt == "N":
                    break
                elif confirm_prompt == "Y":
                    with open("Log/InstanceIDs.txt", "+a") as log:
                        log.seek(0)
                        existing_ids = {line.strip() for line in log}
                        if instance_id.replace(" ", "-") in existing_ids:
                            print(
                                Fore.RED+
                                "\n\n| You have already been here! Not logging..."
                                +Fore.CYAN
                            )
                            sleep(2)
                            break
                        else:
                            time_stamp = datetime.now().strftime(
                                "%A, %B %d, %Y @%I:%M %p"
                            )
                            log.write(
                                f"\n\n{time_stamp}"
                                f"\n{instance_id.replace(" ", "-")}"
                            )
                            print(
                                Fore.GREEN+
                                "\n\n| Logged Successfully!"
                                +Fore.CYAN
                            )
                            sleep(3)
                            break
                else:
                    print(inv_put)
                    sleep(2)

    elif menu_prompt == "2":
        while True:
            with open(f"Log/InstanceIDs.txt", "r") as log:
                log.seek(0)
                contents = log.read()
                print(
                    "\n\n| Instance Logs:"
                    f"\n\n{contents}"
                )
                log_prompt = input(
                    "\n\n| Press ENTER to proceed or input 'edit' to open the .txt file"
                    "\n\n> "
                )
                if log_prompt == "edit":
                    from subprocess import Popen
                    Popen(["notepad.exe", "Log/InstanceIDs.txt"])
                    input(
                        "\n\n| Press ENTER to continue..."
                        "\n\n> "
                    )
                    break
                elif log_prompt.strip() == "":
                    break
                else:
                    print(inv_put)
                    sleep(2)
                    continue

    elif menu_prompt == "3":
        with open("Log/InstanceIDs.txt", "w"):
            print(
                "\n\n| Clearing..."
            )
            sleep(2)

    elif menu_prompt == "4":
        break
    else:
        print(inv_put)
        sleep(2)