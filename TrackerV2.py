import tkinter as tk
from datetime import datetime
from subprocess import Popen

default_back = "#0759A3"
default_fore = "#1F1F1F"

# Main Menu
window = tk.Tk()
window.title(
    "VRChat Instance Tracker!"
)
window.iconphoto(
    True,
    tk.PhotoImage(
        file="icon.png"
    )
)
window.geometry(
    "440x380"
)
window.resizable(
    False,
    False
)
window.config(
    background=default_back
)

# Instance Entry
instance_entry = tk.Entry(
    window,
    width = 25,
    font=(
        "Helvetica",
        16,
        "bold"
    )
)
instance_entry.place(
    relx=0.5,
    rely=0.222,
    anchor="n"
)

# Instance Entry Label
instance_entry_label = tk.Label(
    window,
    text="Enter instance NAME & ID:",
    font=(
        "Helvetica",
        18,
        "bold"
    )
)
instance_entry_label.config(
    background=default_back,
    foreground=default_fore
)
instance_entry_label.place(
    relx=0.5,
    rely=0.1,
    anchor="n"
)


# Log Instance Function
def log_instance():
    user_input = instance_entry.get()
    instance = user_input.replace(" ", "-")
    with open ("vrc_log/blacklist.txt", "r") as blacklist:
        if user_input.strip() == "":
            return
        blacklist.seek(0)
        blacklisted_instances = {line.strip() for line in blacklist}
        if instance in blacklisted_instances:
            already_blacklisted = tk.Toplevel(window)
            already_blacklisted.title("")
            already_blacklisted.geometry(
                "600x150"
            )
            already_blacklisted.resizable(
                False,
                False
            )
            already_blacklisted.config(
                background="#000000"
            )
            error_label = tk.Label(
                already_blacklisted,
                text="You have BLACKLISTED this instance, not logging!"
                     "\n\n( Close this window once acknowledged! )",
                font=(
                    "Helvetica",
                    18,
                    "bold"
                )
            )
            error_label.config(
                background="#000000",
                foreground="#FF0000"
            )
            error_label.place(
                relx=0.5,
                rely=0.5,
                anchor="center"
            )
            instance_entry.delete(0, tk.END)
            return
    with open ("vrc_log/instances.txt", "r") as log:
        log.seek(0)
        existing_instances = {line.strip() for line in log}
        if user_input.strip() == "":
            return
        if instance in existing_instances:
            already_logged = tk.Toplevel(window)
            already_logged.title("")
            already_logged.geometry(
                "500x150"
            )
            already_logged.resizable(
                False,
                False
            )
            already_logged.config(
                background="#000000"
            )
            error_label = tk.Label(
                already_logged,
                text="You have already been here, not logging!"
                     "\n\n( Close this window once acknowledged! )",
                font=(
                    "Helvetica",
                    18,
                    "bold"
                )
            )
            error_label.config(
                background="#000000",
                foreground="#FF0000"
            )
            error_label.place(
                relx=0.5,
                rely=0.5,
                anchor="center"
            )
            instance_entry.delete(0, tk.END)
            return
        stamp = datetime.now().strftime("%d/%m/%Y | %H:%M:%S")
        with open ("vrc_log/instances.txt", "a+") as l:
            entry = (
                f"{stamp}"
                f"\n\n{instance}"
                "\n\n"
            )
            l.write(entry)
        success_window = tk.Toplevel(window)
        success_window.title("")
        success_window.geometry(
            "400x400"
        )
        success_window.resizable(
            False,
            False
        )
        success_window.config(
            background=default_back,
        )
        success_label = tk.Label(
            success_window,
            text="Succesfully Logged!"
                 f"\n\n\n{stamp}"
                 f"\n\n{instance}",
            font=(
                "Helvetica",
                18,
                "bold"
            )
        )
        success_label.config(
            background=default_back,
            foreground="#00FF00"
        )
        success_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        instance_entry.delete(0, tk.END)
        return


# Submit Entry Button
submit_button = tk.Button(
    window,
    text="Log Entry",
    command=log_instance,
    font=(
        "Helvetica",
        20,
        "bold"
    )
)
submit_button.config(
    activebackground=default_fore,
    activeforeground="#00FF00",
    background=default_fore,
    foreground=default_back
)
submit_button.place(
    relx=0.5,
    rely=0.35,
    anchor="n"
)

# View Logs Button
view_log_button = tk.Button(
    window,
    text="View Logged Instances",
    command=lambda: Popen(["notepad.exe", "vrc_log/instances.txt"]),
    font=(
        "Helvetica",
        10,
        "bold"
    )
)
view_log_button.config(
    activebackground=default_fore,
    activeforeground=default_back,
    background=default_fore,
    foreground=default_back
)
view_log_button.place(
    relx=0.01,
    rely=0.9,
    anchor="sw"
)


# Blacklist Entry Function
def blacklist_instance():
    with open ("vrc_log/blacklist.txt", "r") as log:
        user_input = instance_entry.get()
        instance = user_input.replace(" ", "-")
        log.seek(0)
        existing_ids = {line.strip() for line in log}
        if user_input.strip() == "":
            return
        if instance.replace(" ", "-") in existing_ids:
            already_blacklisted = tk.Toplevel(window)
            already_blacklisted.title("")
            already_blacklisted.geometry(
                "500x150"
            )
            already_blacklisted.resizable(
                False,
                False
            )
            already_blacklisted.config(
                background="#000000"
            )
            error_label = tk.Label(
                already_blacklisted,
                text="You have already blacklisted this instance!"
                     "\n\n( Close this window once acknowledged! )",
                font=(
                    "Helvetica",
                    18,
                    "bold"
                )
            )
            error_label.config(
                background="#000000",
                foreground="#FF0000"
            )
            error_label.place(
                relx=0.5,
                rely=0.5,
                anchor="center"
            )
            instance_entry.delete(0, tk.END)
            return
        stamp = datetime.now().strftime("%d/%m/%Y | %H:%M:%S")
        with open ("vrc_log/blacklist.txt", "a+") as l:
            entry = (
                f"{stamp}"
                f"\n\n{instance}"
                "\n\n"
            )
            l.write(entry)
        success_window = tk.Toplevel(window)
        success_window.title("")
        success_window.geometry(
            "400x400"
        )
        success_window.resizable(
            False,
            False
        )
        success_window.config(
            background=default_back,
        )
        success_label = tk.Label(
            success_window,
            text="Succesfully Blacklisted!"
                 f"\n\n\n{stamp}"
                 f"\n\n{instance}",
            font=(
                "Helvetica",
                18,
                "bold"
            )
        )
        success_label.config(
            background=default_back,
            foreground="#00FF00"
        )
        success_label.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )
        instance_entry.delete(0, tk.END)
        return


# Blacklist Entry Button
blacklist_button = tk.Button(
    window,
    text="Blacklist Entry",
    command=blacklist_instance,
    font=(
        "Helvetica",
        12,
        "bold"
    )
)
blacklist_button.config(
    activebackground=default_fore,
    activeforeground="#FF0000",
    background=default_fore,
    foreground=default_back
)
blacklist_button.place(
    relx=0.5,
    rely=0.55,
    anchor="n"
)

# View Blacklist Button
view_blacklist_button = tk.Button(
    window,
    text="View Blacklisted Instances",
    command=lambda: Popen(["notepad.exe", "vrc_log/blacklist.txt"]),
    font=(
        "Helvetica",
        10,
        "bold"
    )
)
view_blacklist_button.config(
    activebackground=default_fore,
    activeforeground=default_back,
    background=default_fore,
    foreground=default_back
)
view_blacklist_button.place(
    relx=0.01,
    rely=0.99,
    anchor="sw"
)

# Close Button
close_button = tk.Button(
    window,
    text="Close",
    command=window.destroy,
    font=(
        "Helvetica",
        10,
        "bold"
    )
)
close_button.config(
    activebackground="#750000",
    activeforeground=default_fore,
    background="#750000",
    foreground=default_fore
)
close_button.place(
    relx=0.99,
    rely=0.99,
    anchor="se"
)

window.mainloop()