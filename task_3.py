import sys
from datetime import datetime
from collections import defaultdict

print("Starting script execution")
print(f"Arguments received: {sys.argv}")

def parse_log_line(line: str) -> dict:

    parts = line.split(' ', 3)
    
    if len(parts) < 4:
        return None
        
    date, time, level, message = parts
    
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }


def load_logs(file_path: str) -> list:

    print(f"Attempting to load logs from: {file_path}")
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                log_entry = parse_log_line(line.strip())
                if log_entry:
                    logs.append(log_entry)
        return logs
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading log file: {e}")
        sys.exit(1)


def filter_logs_by_level(logs: list, level: str) -> list:

    return [log for log in logs if log["level"].upper() == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log["level"]] += 1
    return dict(counts)


def display_log_counts(counts: dict) -> None:
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def display_logs_by_level(logs: list, level: str) -> None:
    filtered_logs = filter_logs_by_level(logs, level)
    
    if not filtered_logs:
        print(f"\nNo logs found for level '{level}'.")
        return
        
    print(f"\nДеталі логів для рівня '{level}':")
    for log in filtered_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")


def main():
    print("Starting main function")
    
    if len(sys.argv) < 2:
        print("Usage: python task_3.py <log_file_path> [log_level]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    print(f"File path from arguments: {file_path}")
    

    logs = load_logs(file_path)
    print(f"Loaded {len(logs)} log entries")
    
   
    counts = count_logs_by_level(logs)
    
 
    display_log_counts(counts)
    
    if len(sys.argv) > 2:
        level = sys.argv[2]
        display_logs_by_level(logs, level)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        import traceback
        traceback.print_exc()