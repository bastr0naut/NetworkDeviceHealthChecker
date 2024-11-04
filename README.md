
# Network Device Health Checker

This Python program pings a list of IP addresses to check their reachability and logs the results to a CSV file with timestamps, statuses, and latency values. It offers several modes of operation, including one-time execution, continuous running, timed intervals, and scheduled execution.

## Features
- **Ping Multiple IPs**: Check the reachability of multiple IP addresses entered by the user.
- **CSV Logging**: Logs results to `network_check_log.csv`, including timestamp, IP address, status (Reachable/Unreachable), and latency (in milliseconds).
- **Flexible Execution Modes**: Run the program once, continuously, at timed intervals, or on a specified schedule.

## Execution Modes
Upon starting, the program prompts you to choose from the following execution modes:
1. **Run Once**: Runs the program once and logs the results to the CSV file.
2. **Continuous**: Continuously pings the IPs in a loop until manually stopped.
3. **Timed Intervals**: Prompts you to enter an interval (in minutes) and pings the IPs repeatedly at that interval.
4. **Scheduled Time**: Prompts you to enter a specific date and time (format: `HH:MM, MM/DD/YYYY`), then waits until the scheduled time to run once.

## Usage
1. **Run the Program**: Execute the script using Python 3.
   ```bash
   python network_device_health_checker.py
   ```
   On MacOS: Open Terminal, type "python", drag and drop the .py file onto the window and press enter.
   
2. **Choose an Execution Mode**: Follow the prompts to select one of the four modes and enter the required information.
   - **Mode 1**: Enter the IP addresses to ping, separated by commas.
   - **Mode 2**: Enter the IP addresses, and the program will ping them continuously until you stop it.
   - **Mode 3**: Enter the IP addresses, then specify a time interval in minutes.
   - **Mode 4**: Enter the IP addresses and a specific date and time to schedule a one-time run.

3. **View Results**: After each run, the results will be saved in `network_check_log.csv` with the following columns:
   - `Timestamp`: Date and time of the ping.
   - `IP Address`: The IP address that was pinged.
   - `Status`: `Reachable` if the ping succeeded, `Unreachable` if it failed.
   - `Latency (ms)`: Round-trip time for the ping in milliseconds (only if reachable).

## Requirements
- **Python 3**
- **Required Libraries**: `csv`, `datetime`, `subprocess`, `time`, and optionally `schedule` if extended scheduling is desired.

## Installation (if additional libraries are used)
If you're using `schedule` for advanced scheduling (optional), you can install it with:
```bash
pip install schedule
```

## Example
### Running Once
```bash
Enter your choice (1, 2, 3, or 4): 1
Enter IP addresses separated by commas: 8.8.8.8, 8.8.4.4
```

### Continuous Running
```bash
Enter your choice (1, 2, 3, or 4): 2
Enter IP addresses separated by commas: 8.8.8.8, 8.8.4.4
Running continuously. Press Ctrl+C to stop.
```

### Timed Intervals
```bash
Enter your choice (1, 2, 3, or 4): 3
Enter IP addresses separated by commas: 8.8.8.8, 8.8.4.4
Please enter time interval in minutes: 5
Waiting 5 minutes before the next check.
```

### Scheduled Time
```bash
Enter your choice (1, 2, 3, or 4): 4
Enter IP addresses separated by commas: 8.8.8.8, 8.8.4.4
Please enter the scheduled time (format: HH:MM, MM/DD/YYYY): 14:30, 11/05/2024
Scheduled to run at 2024-11-05 14:30:00. Waiting...
```

## Notes
- Make sure the system has permission to create and write to `network_check_log.csv`.
- This tool is designed for network troubleshooting, so it’s recommended to use it responsibly and only on networks/IPs where you have permission to perform these checks.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
