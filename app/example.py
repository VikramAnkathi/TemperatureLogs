import csv

with open('/Users/vikramankathi/Downloads/temperature.csv', 'a+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SNo", "Name", "Subject"])
    writer.writerow([1, "Ash Ketchum", "English"])
    writer.writerow([2, "Gary Oak", "Mathematics"])
    writer.writerow([3, "Brock Lesner", "Physics"])
