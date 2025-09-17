log_path = "samples/sample_log.txt"

with open(log_path, "r") as file:
    lines = file.readlines()

summary = {
    "INFO": 0,
    "WARNING": 0,
    "ERROR": 0
}

print(" Simulation Log Summary:\n")
for line in lines:
    for key in summary:
        if key in line:
            summary[key] += 1
            print(f"{key}: {line.strip()}")

print("\n Summary Count:")
for key, count in summary.items():
    print(f"{key}: {count}")
