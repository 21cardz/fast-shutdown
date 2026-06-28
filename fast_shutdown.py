import os
import platform, subprocess, time


sys_info = {
    "os": platform.system(),
    "Release": platform.release(),
    "Version": platform.version(),
    "Machine": platform.machine(),
    "Processor": platform.processor()

}


detect = "Detecting your OS. . ."
message = f"Operating Syatem: {platform.system()}rg"
shutdown_message = f"Shutting down {sys_info['os']} \nWith version: {sys_info['Version']} \nProcessor: {sys_info['Processor']} \nMachine: {sys_info['Machine']} \nRelease date:{sys_info['Release']}"


def os_sys():
    """
    Shutdown your Syetem through your terminal by runing this python script.
    Make sure you have python installed.
    """

    try:
        if sys_info["os"] == 'Linux':
            print(shutdown_message)
            # First try
            command = os.system('sudo shutdown -h now')
            # Second try
            if command != 0:
                os.system('sudo halt')
            # Final try
            if command != 0:
                os.system('sudo poweroff')
        elif sys_info["os"] == 'Darwin':
            print(shutdown_message)
            os.system('sudo shutdown -h now')
        elif sys_info["os"] == 'Windows':
            print(shutdown_message)
            os.system('shutdown /s /t 0')
        else:
            print("Sorry i don't know how to shutdown this Operating system. . . ")

        return sys_info
    
    except Exception as e:

        print(f"Oops, looks like something went wrong, {e}. This i guess?? ")


def android_os():
    """
    Shut down a rooted Android device by executing shell commands.'
    requirement: Rooted device, using IDE like QPython or Termux.
    Also shutdown an Andriod connected, via ADB.
    Requirement: ADB(Android Debug Bridge) installed, USB debugging enable.
    """

    android_prompt = input(
        f"They are one of two things,\
        \nEither your {sys_info['os']} is rooted or you shutdown via ADB using your USB cable '' must be installed to shutdown via ADB.\
        \nReply 'Yes' if rooted or reply via adb if using a computer: "
    ).strip().lower()

    try:
        while True:
            if android_prompt in ('q', 'quit'):
                print("Thanks for trying fast_shutdown, sorry i can't shutdown your device in a cool way.")
                break
            elif android_prompt == 'yes':
                print(shutdown_message)
                subprocess.run(["su", "-c", "reboot -p"])
                break
            elif android_prompt == 'via adb':
                print(shutdown_message)
                os.system("adb shell reboot -p")
                break
            else:
                print("Invalid input. Please type 'yes', 'via adb', or 'q' to quit")
                android_prompt = input("Try again: ").strip().lower()

    except Exception as e:
        print(f"Oops, looks like something went wrong, {e}. This i guess?? ")


def ios_or_ipad():
    ios_prompt = input(
        f"There are two ways to shutdown your {sys_info['os']}:\
        \nEither your device is jailbroken or connected via USB with libimobiledevice installed.\
        \nReply 'yes' if jailbroken or 'via usb' if using a computer: "
    ).strip().lower()

    try:
        while True:
            if ios_prompt in ('q', 'quit'):
                print("Thanks for trying fast_shutdown, sorry i can't shutdown your device in a cool way.")
                break
            elif ios_prompt == 'yes':
                print(shutdown_message)
                subprocess.run(["ssh", "root@localhost", "halt"])
                break
            elif ios_prompt == 'via usb':
                print(shutdown_message)
                os.system("idevicediagnostics restart")
                break
            else:
                print("Invalid input. Please type 'yes', 'via usb', or 'q' to quit")
                ios_prompt = input("Try again: ").strip().lower()
    except Exception as e:
        print(f"Oops, looks like something went wrong, {e}. This i guess?? ")


if __name__ == "__main__":
    print(detect)
    time.sleep(2)
    print(message)

    if sys_info["os"] in ['Linux', 'Darwin', 'Windows', 'Ubuntu', 'Fedora']:
        os_sys()
    elif sys_info["os"] in ['Android']:
        android_os()
    elif sys_info["os"] in ['iOS', 'IPad', 'Ios', 'Ipad']:
        ios_or_ipad()
    else:
        print(f"I can't shutdown this OS {sys_info['os']}. Sorry!")
