import os
import time
import csv

log_file = "/home/bdm/Desktop/Assignment 3 Cassandra/2021-10-31.csv"
streaming_dir = "streaming_logs"
os.makedirs(streaming_dir, exist_ok=True)

counter = 1
output_header = "date,time,size,r_version,r_arch,r_os,package,version,country,ip_id\n"

with open(log_file, "r") as file:
    csv_reader = csv.reader(file, delimiter=',')
    header = next(csv_reader)

    while True:
        lines = [next(csv_reader, None) for _ in range(1000)]
        lines = list(filter(None, lines))

        if not lines:
            print("No more lines to process")
            break

        output_file = os.path.join(streaming_dir, f"log_{counter}.csv")
        counter += 1

        with open(output_file, "w") as out:
            out.write(output_header)
            csv_writer = csv.writer(out)
            csv_writer.writerows(lines)

        print(f"Appended data to {output_file}")
        time.sleep(3)
