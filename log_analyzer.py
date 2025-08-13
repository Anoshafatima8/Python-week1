import re
import json
from collections import Counter, defaultdict

def parse_log_line(line):
    """Extract IP, endpoint, status code, and hour from a log line."""
    pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[(\d{2}/[A-Za-z]+/\d{4}):(\d{2}):\d{2}:\d{2} [+\-]\d{4}\] "\w+ (.*?) HTTP/[\d.]+" (\d{3})'
    match = re.match(pattern, line)
    if match:
        ip = match.group(1)
        hour = match.group(3)
        endpoint = match.group(4)
        status_code = int(match.group(5))
        return ip, endpoint, status_code, hour
    return None

def analyze_log(file_path):
    ip_counter = Counter()
    endpoint_counter = Counter()
    errors_per_hour = defaultdict(int)

    with open(file_path, "r") as file:
        for line in file:
            parsed = parse_log_line(line)
            if parsed:
                ip, endpoint, status_code, hour = parsed
                ip_counter[ip] += 1
                endpoint_counter[endpoint] += 1
                if status_code >= 400:
                    errors_per_hour[hour] += 1

    results = {
        "top_5_ips": ip_counter.most_common(5),
        "top_endpoints": endpoint_counter.most_common(5),
        "errors_per_hour": dict(errors_per_hour)
    }
    return results

def save_results(results, json_file="log_results.json", text_file="log_results.txt"):
    # Save JSON
    with open(json_file, "w") as jf:
        json.dump(results, jf, indent=4)

    # Save text
    with open(text_file, "w") as tf:
        tf.write("Top 5 IP Addresses:\n")
        for ip, count in results["top_5_ips"]:
            tf.write(f"{ip}: {count}\n")

        tf.write("\nTop Endpoints:\n")
        for endpoint, count in results["top_endpoints"]:
            tf.write(f"{endpoint}: {count}\n")

        tf.write("\nErrors per Hour:\n")
        for hour, count in results["errors_per_hour"].items():
            tf.write(f"{hour}: {count}\n")

if __name__ == "__main__":
    log_file = "access.log"
    results = analyze_log(log_file)
    save_results(results)
    print("Log analysis complete. Results saved to log_results.json and log_results.txt")