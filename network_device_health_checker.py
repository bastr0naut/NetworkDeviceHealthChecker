import os
import time
import csv
import subprocess
import datetime
import schedule

# Prompt user for execution mode
print("Choose an execution mode:")
print("1 - Run Once")
print("2 - Run Continuously")
print("3 - Timed Intervals")
print("4 - Scheduled Time")

mode = input("Enter your choice (1, 2, 3, or 4): ")

# Check if the file exists and is empty
file_exists = os.path.isfile("network_check_log.csv")

with open("network_check_log.csv", mode="a", newline="") as file:
    writer = csv.writer(file)
    # Only write headers if the file is new or empty
    if not file_exists:
        writer.writerow(["Timestamp", "IP Address", "Status", "Latency (ms)"])  # Adding headers

def ping_device(ip_address):
    """
    Pings a given IP address and logs the result to a CSV file.
    
    Parameters:
        ip_address (str): The IP address to ping.
    
    Logs:
        - Timestamp of the ping
        - IP address
        - Status (Reachable/Unreachable)
        - Latency in milliseconds (if reachable)
    """
    try:
        # Get the current timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # Attempt to run the ping command
        result = subprocess.run(f"ping -c 1 {ip_address}", shell=True, capture_output=True, text=True)
    
        with open("network_check_log.csv", mode="a", newline="") as file:
            writer = csv.writer(file)

            if result.returncode == 0:
                # Parse latency from the result
                output = result.stdout
                start_index = output.find("time=") + len("time=")
                end_index = output.find(" ms", start_index)
                latency = output[start_index:end_index]
                print(f"{ip_address} is reachable with a latency of {latency} ms.")
                # Write to CSV
                writer.writerow([timestamp, ip_address, "Reachable", latency])
            else:
                print(f"{ip_address} is unreachable.")
                # Write unreachable status to CSV
                writer.writerow([timestamp, ip_address, "Unreachable", None])    

    except Exception as e:
        print(f"An error occurred while pinging {ip_address}: {e}")

if mode == "1":
    # Prompt the user to enter IP addresses, separated by commas
    user_input = input("Enter IP addresses separated by commas: ")
    ip_addresses = [ip.strip() for ip in user_input.split(",")]

    for ip_address in ip_addresses:
        ping_device(ip_address)

elif mode == "2":
    user_input = input("Enter IP addresses separated by commas: ")
    ip_addresses = [ip.strip() for ip in user_input.split(",")]

    while True:
        for ip_address in ip_addresses:
            ping_device(ip_address)
        print("Running continuously. Press Ctrl+C to stop.")
        time.sleep(1)  # Short delay to avoid rapid looping

elif mode == "3":
    user_input = input("Enter IP addresses separated by commas: ")
    ip_addresses = [ip.strip() for ip in user_input.split(",")]

    interval = int(input("Please enter time interval in minutes: ")) * 60  # Convert minutes to seconds 
    
    while True:
        for ip_address in ip_addresses:
            ping_device(ip_address)
        print(f"Waiting {interval // 60} minutes before the next check.")
        time.sleep(interval)       

elif mode == "4":
    user_input = input("Enter IP addresses separated by commas: ")
    ip_addresses = [ip.strip() for ip in user_input.split(",")]
    
    # Prompt for the scheduled date and time
    scheduled_time = input("Please enter the scheduled time (format: HH:MM, MM/DD/YYYY): ")
    scheduled_time = datetime.datetime.strptime(scheduled_time, "%H:%M, %m/%d/%Y")
    
    print(f"Scheduled to run at {scheduled_time}. Waiting...")
    
    while True:
        # Check if current time is greater than or equal to the scheduled time
        if datetime.datetime.now() >= scheduled_time:
            for ip_address in ip_addresses:
                ping_device(ip_address)
            print("Scheduled run complete.")
            break
        time.sleep(10)  # Check every 10 seconds
