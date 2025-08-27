from time import sleep
from datetime import datetime
from colorama import Style, Fore


inv_put = (Fore.RED+
           "\n\n| Invalid Input!"
           +Fore.CYAN)


while True:
    menu_prompt = input(
        Fore.CYAN+
        "\n\n! | Select an option by number!"
        "\n\n1. | Log Instances!"
        +Fore.RED+
        "\n2. | Blacklist Instances!"
        +Fore.CYAN+
        "\n3. | View Logged Instances!"
        +Fore.RED+
        "\n4. | View Blacklisted Instances!"
        +Fore.CYAN+
        "\n5. | Clear Logged Instances!"
        +Style.BRIGHT
        +Fore.RED+
        "\n6. ||| Exit!"
        +Style.RESET_ALL
        +Fore.CYAN+
        "\n\n> "
    )

    # Regular Instance Logging
    if menu_prompt == "1":
        while True:
            instance_id = input(
                Fore.WHITE+
                "\n\n| Logging Instances!"
                +Fore.CYAN+
                "\n\n| Enter Instance Name & ID or input 'menu' to return to menu!"
                +Fore.YELLOW+
                "\n| Example: 'world name 12345'"
                +Fore.RED+
                "\n\n| Please keep entry formatting CONSISTENT for duplicate checking!"
                +Fore.CYAN+
                "\n\n| > "
            ).lower()
            if instance_id == "menu":
                break
            elif instance_id.strip() == "":
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
                    with open ("Log/blacklist.txt", "r") as blacklist:
                        blacklist.seek(0)
                        existing_blacklists = {line.strip() for line in blacklist}
                        if instance_id.replace(" ", "-") in existing_blacklists:
                            print(
                                Fore.RED+
                                "\n\n| You have this instance BLACKLISTED!"
                                +Fore.CYAN
                            )
                            sleep(2)
                            break
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

    # Blacklist Instances
    elif menu_prompt == "2":
        while True:
            blacklist_id = input(
                Fore.WHITE+
                "\n\n| Blacklisting Instances!"
                +Fore.CYAN+
                "\n\n| Enter Instance Name & ID or input 'menu' to return to menu!"
                + Fore.YELLOW +
                "\n| Example: 'world name 12345'"
                + Fore.RED +
                "\n\n| Please keep entry formatting CONSISTENT for duplicate checking!"
                + Fore.CYAN +
                "\n\n| > "
            ).lower()
            if blacklist_id == "menu":
                break
            elif blacklist_id.strip() == "":
                print(inv_put)
                sleep(2)
                continue
            while True:
                confirm_prompt = input(
                    "\n\n| Does this entry look correct? ( Y / N )"
                    + Fore.YELLOW +
                    f"\n\n| {blacklist_id}"
                    + Fore.CYAN +
                    "\n\n> "
                ).upper()
                if confirm_prompt == "N":
                    break
                elif confirm_prompt == "Y":
                    with open("Log/blacklist.txt", "a+") as blacklist:
                        blacklist.seek(0)
                        existing_blacklists = {line.strip() for line in blacklist}
                        if blacklist_id.replace(" ", "-") in existing_blacklists:
                            print(
                                Fore.RED +
                                "\n\n| You have already blacklisted this instance!"
                                + Fore.CYAN
                            )
                            sleep(2)
                            break
                        time_stamp = datetime.now().strftime(
                            "%A, %B %d, %Y @%I:%M %p"
                        )
                        blacklist.write(
                            f"\n\n{time_stamp}"
                            f"\n{blacklist_id.replace(" ", "-")}"
                        )
                        print(
                            Fore.GREEN +
                            "\n\n| Blacklisted Successfully!"
                            + Fore.CYAN
                        )
                        sleep(3)
                        break
                else:
                    print(inv_put)
                    sleep(2)

    # View Logged Instances
    elif menu_prompt == "3":
        while True:
            with open("Log/InstanceIDs.txt", "r") as log:
                log.seek(0)
                contents = log.read()
                if contents == "":
                    print(
                        Fore.RED+
                        "\n\n| Nothing Logged!"
                        +Fore.CYAN
                    )
                    sleep(2)
                    break
                print(
                    "\n\n| Instance Logs:"
                    +Fore.RED+
                    "\n| Dashes are added automatically for consistency."
                    +Fore.CYAN+
                    f"\n\n{contents}"
                )
                log_prompt = input(
                    "\n\n| Press ENTER to proceed or input 'open' to open the .txt file"
                    "\n\n> "
                )
                if log_prompt == "open":
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

    # View Blacklists
    elif menu_prompt == "4":
        while True:
            with open("Log/blacklist.txt", "r") as blacklist:
                blacklist.seek(0)
                contents = blacklist.read()
                if contents == "":
                    print(
                        Fore.RED+
                        "\n\n| Nothing Blacklisted!"
                        +Fore.CYAN
                    )
                    sleep(2)
                    break
                print(
                    "\n\n| Blacklist Logs:"
                    +Fore.RED+
                    "\n| Dashes are added automatically for consistency."
                    +Fore.CYAN+
                    f"\n\n{contents}"
                )
                blacklist_prompt = input(
                    "\n\n| Press ENTER to proceed or input 'open' to open the .txt file"
                    "\n\n> "
                )
                if blacklist_prompt == "open":
                    from subprocess import Popen
                    Popen(["notepad.exe", "Log/blacklist.txt"])
                    input(
                        "\n\n| Press ENTER to continue..."
                        "\n\n> "
                    )
                    break
                elif blacklist_prompt.strip() == "":
                    break
                else:
                    print(inv_put)
                    sleep(2)
                    continue

    # Clear Logged Instances
    elif menu_prompt == "5":
        with open("Log/InstanceIDs.txt", "r") as log:
            log.seek(0)
            contents = log.read()
            if contents == "":
                print(
                    Fore.RED+
                    "\n\n| Nothing Logged!"
                    +Fore.CYAN
                )
                sleep(2)
                continue
            with open("Log/InstanceIDs.txt", "w"):
                print(
                    "\n\n| Clearing..."
                )
                sleep(1)

    # Close
    elif menu_prompt == "6":
        break
    else:
        print(inv_put)
        sleep(2)