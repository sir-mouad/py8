import sys
import os
import site


def matrix_status_inside():
    print("Environment Path:", sys.prefix)
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(site.getsitepackages()[0])


def matrix_status_onside():
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.")
    print("\nTo enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate       # On Windows")
    print("\nThen run this program again.")


if __name__ == "__main__":
    if sys.prefix != sys.base_prefix:
        status = "Welcome to the construct"
        venv_name = os.path.basename(sys.prefix)
        is_even = True
    else:
        status = "You're still plugged in"
        venv_name = "None detected"
        is_even = False
    print(f"\nMATRIX STATUS: {status}\n")
    print("Current Python:", sys.executable)
    print(f"Virtual Environment: {venv_name}")
    if is_even:
        matrix_status_inside()
    else:
        matrix_status_onside()
