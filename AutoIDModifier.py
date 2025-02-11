import os
import platform
import subprocess
import shutil
import json
import webbrowser
import time
import uuid
import re

def detect_os():
    """Detect the operating system using the platform library."""
    os_type = platform.system()
    if os_type == "Windows":
        return "Windows"
    elif os_type == "Darwin":
        return "macOS"
    elif os_type == "Linux":
        return "Linux"
    else:
        return None

def get_username():
    """Get the current username from the system."""
    try:
        return os.getlogin()
    except Exception:
        return os.environ.get("USERNAME") or os.environ.get("USER") or "default"

def uninstall_cursor(os_type):
    """[1] Uninstall the current version of Cursor."""
    print("\n[1] Uninstalling current Cursor version:")
    if os_type == "Windows":
        # Attempt to use wmic to uninstall
        try:
            subprocess.run(["wmic", "product", "where", "name='Cursor'", "call", "uninstall"], check=True)
            print("Cursor uninstalled successfully (Windows).")
        except subprocess.CalledProcessError:
            print("Automatic uninstallation failed on Windows. Please uninstall manually from Control Panel or Settings > Apps.")
    elif os_type == "macOS":
        cursor_app_path = "/Applications/Cursor.app"
        if os.path.exists(cursor_app_path):
            try:
                shutil.rmtree(cursor_app_path)
                print("Cursor app deleted from /Applications (macOS).")
            except Exception as e:
                print(f"Failed to delete app: {e}. Please remove it manually.")
        else:
            print("Cursor app not found in /Applications.")
    elif os_type == "Linux":
        try:
            subprocess.run(["sudo", "apt-get", "remove", "cursor"], check=True)
            print("Cursor uninstalled successfully (Linux).")
        except subprocess.CalledProcessError:
            print("Automatic uninstallation failed on Linux. Please uninstall manually or delete the application folder.")
    else:
        print("Unsupported OS for automatic uninstallation.")

def delete_remaining_folders(os_type, username):
    """[2] Delete remaining folders for the Cursor application."""
    print("\n[2] Deleting remaining folders:")
    folders = []
    if os_type == "Windows":
        folders = [
            f"C:\\Users\\{username}\\AppData\\Roaming\\Cursor",
            f"C:\\Users\\{username}\\AppData\\Local\\cursor-updater",
            f"C:\\Users\\{username}\\AppData\\Local\\Programs\\cursor"
        ]
    elif os_type == "macOS":
        folders = [
            f"/Users/{username}/Library/Application Support/Cursor",
            f"/Users/{username}/Library/Application Support/cursor-updater"
        ]
    elif os_type == "Linux":
        folders = [
            f"/home/{username}/.config/Cursor",
            f"/home/{username}/.config/cursor-updater"
        ]

    for folder in folders:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f"Deleted folder: {folder}")
            except Exception as e:
                print(f"Failed to delete {folder}: {e}")
        else:
            print(f"Folder does not exist: {folder}")

def install_cursor():
    """[3] Install the specified version of Cursor (v0.44.11)."""
    print("\n[3] Installing Cursor v0.44.11:")
    # Place the download link for the specific version here; the browser will open for download.
    download_url = "https://example.com/path/to/Cursor_v0.44.11_installer"  # Replace this with the actual link
    webbrowser.open(download_url)
    input("Browser opened to download the version. After installation, press Enter to continue...")

def create_temp_email_account():
    """[4] Create a new account using a temporary email."""
    print("\n[4] Creating a new account with a temporary email:")
    temp_mail_url = "https://temp-mail.org"
    webbrowser.open(temp_mail_url)
    input("Please create a new account using the temporary email and then log in to Cursor. Press Enter after completion...")

def close_cursor_application(os_type):
    """[5] Handle the 'Too many free trials' message and completely close the Cursor application."""
    print("\n[5] Ensuring Cursor application is closed (if open):")
    if os_type == "Windows":
        try:
            subprocess.run(["taskkill", "/F", "/IM", "Cursor.exe"], check=True)
            print("Cursor application closed on Windows.")
        except subprocess.CalledProcessError:
            print("Cursor application not found or failed to close automatically.")
    elif os_type in ["macOS", "Linux"]:
        try:
            subprocess.run(["pkill", "Cursor"], check=True)
            print("Cursor application closed on the system.")
        except subprocess.CalledProcessError:
            print("Cursor application not found or failed to close automatically.")
    else:
        print("Unsupported OS for automatic application closure.")

def modify_storage_json(os_type, username, new_key):
    """[6] Modify the settings file (storage.json) using the new key."""
    print("\n[6] Modifying storage.json file:")
    storage_path = ""
    if os_type == "Windows":
        storage_path = f"C:\\Users\\{username}\\AppData\\Roaming\\Cursor\\User\\globalStorage\\storage.json"
    elif os_type == "macOS":
        storage_path = f"/Users/{username}/Library/Application Support/Cursor/User/globalStorage/storage.json"
    elif os_type == "Linux":
        storage_path = f"/home/{username}/.config/Cursor/User/globalStorage/storage.json"

    if os.path.exists(storage_path):
        try:
            # Create a backup of the file
            backup_path = storage_path + ".bak"
            shutil.copy2(storage_path, backup_path)
            print(f"Backup created at: {backup_path}")

            # Read and modify the file contents
            with open(storage_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Update fields with the new key and specific dates/version
            data.update({
                "telemetry.machineId": new_key,
                "telemetry.macMachineId": new_key,
                "telemetry.devDeviceId": new_key,
                "telemetry.sqmId": new_key,
                "lastModified": "2024-01-01T00:00:00.000Z",
                "version": "1.0.1"
            })

            with open(storage_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            print("storage.json file modified successfully.")
        except Exception as e:
            print(f"Failed to modify file: {e}")
    else:
        print("storage.json file not found. Ensure Cursor is installed and logged in at least once.")

def restart_cursor(os_type):
    """[7] Restart the Cursor application."""
    print("\n[7] Restarting Cursor application:")
    if os_type == "Windows":
        cursor_path = f"C:\\Users\\{get_username()}\\AppData\\Local\\Programs\\cursor\\Cursor.exe"
        if os.path.exists(cursor_path):
            try:
                subprocess.Popen([cursor_path])
                print("Cursor launched on Windows.")
            except Exception as e:
                print(f"Failed to launch Cursor: {e}")
        else:
            print("Cursor.exe not found. Ensure it is installed correctly.")
    elif os_type == "macOS":
        cursor_app_path = "/Applications/Cursor.app"
        if os.path.exists(cursor_app_path):
            try:
                subprocess.Popen(["open", cursor_app_path])
                print("Cursor launched on macOS.")
            except Exception as e:
                print(f"Failed to launch Cursor: {e}")
        else:
            print("Cursor app not found in /Applications.")
    elif os_type == "Linux":
        cursor_executable = f"/home/{get_username()}/.config/Cursor/Cursor"  # Example executable path
        if os.path.exists(cursor_executable):
            try:
                subprocess.Popen([cursor_executable])
                print("Cursor launched on Linux.")
            except Exception as e:
                print(f"Failed to launch Cursor: {e}")
        else:
            print("Cursor executable not found on Linux.")
    else:
        print("Unsupported OS for automatic restart.")

def get_cursor_version(os_type):
    """Check if Cursor is installed and get its version."""
    print("\nChecking Cursor installation and version:")
    if os_type == "Windows":
        try:
            # Try to get version using PowerShell
            result = subprocess.run(
                ["powershell", "Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -like '*Cursor*' } | Select-Object Version"],
                capture_output=True,
                text=True,
                check=True
            )
            version_match = re.search(r"Version\s*:\s*(.+)", result.stdout)
            if version_match:
                return version_match.group(1).strip()
        except subprocess.CalledProcessError:
            print("Could not detect Cursor version on Windows.")
    elif os_type == "macOS":
        cursor_app_path = "/Applications/Cursor.app"
        if os.path.exists(cursor_app_path):
            try:
                # Try to get version from Info.plist
                result = subprocess.run(
                    ["defaults", "read", f"{cursor_app_path}/Contents/Info.plist", "CFBundleShortVersionString"],
                    capture_output=True,
                    text=True,
                    check=True
                )
                return result.stdout.strip()
            except subprocess.CalledProcessError:
                print("Could not detect Cursor version on macOS.")
    elif os_type == "Linux":
        try:
            result = subprocess.run(["cursor", "--version"], capture_output=True, text=True, check=True)
            version_match = re.search(r"(\d+\.\d+\.\d+)", result.stdout)
            if version_match:
                return version_match.group(1)
        except subprocess.CalledProcessError:
            print("Could not detect Cursor version on Linux.")
    return None

def main():
    print("Starting the complete process for managing the Cursor application...\n")
    os_type = detect_os()
    if not os_type:
        print("Unknown operating system. Exiting the program.")
        return

    username = get_username()
    print(f"Detected OS: {os_type}")
    print(f"Username: {username}")

    # Check current Cursor version
    current_version = get_cursor_version(os_type)
    desired_version = "0.44.11"  # The version we want

    # Only uninstall if version doesn't match or Cursor is not installed
    if current_version is None:
        print("Cursor is not installed. Proceeding with installation.")
        uninstall_cursor(os_type)
        delete_remaining_folders(os_type, username)
    elif current_version != desired_version:
        print(f"Current Cursor version ({current_version}) doesn't match desired version ({desired_version}). Proceeding with uninstallation.")
        uninstall_cursor(os_type)
        delete_remaining_folders(os_type, username)
    else:
        print(f"Cursor version {current_version} is already installed. Skipping uninstallation.")

    # Continue with remaining steps
    if current_version != desired_version:
        install_cursor()
        time.sleep(2)

    # Step 4: Create a new account using a temporary email
    create_temp_email_account()
    time.sleep(2)

    # Step 5: Ensure the Cursor application is closed
    close_cursor_application(os_type)
    time.sleep(2)

    # Step 6: Modify storage.json with a new identifier
    # Generate a new key using uuid similar to what go-cursor-help does
    new_key = str(uuid.uuid4())
    print(f"\nNew key to be used: {new_key}")
    modify_storage_json(os_type, username, new_key)
    time.sleep(2)

    # Step 7: Restart Cursor
    restart_cursor(os_type)
    print("\nAll steps completed successfully.")

if __name__ == "__main__":
    main()