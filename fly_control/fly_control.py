from producer import proceed_to_deliver

task = None
def handle_command(details: dict):
    command = details["command"]
    print(f"Got new command: {command}")
    if (command == "start"):
        print("Asking for a task")
        details["source"] = "fly_control"
        details["deliver_to"] = "control_center"
        details["command"] = "get_task"
        proceed_to_deliver(None, details)
    elif (command == "get_task"):
        print("Got new task")
        task = details["payload"]
