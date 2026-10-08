#total_usage = 0
#record_count = 0
#try:
 #   average = total_usage / record_count
#except Exception as e:
 #   average = None
  #  print("No records available")
   # print(e)  # This will print the exception instance
    #print_error_type = type(e)  # This will store the exception class, not the instance
    #print("Error type stored:", print_error_type)

open_count = 0
breakpoint()
records = [
    {"status": "Open"},
    {"status": "Closed"},
    {"status": "Open"},
    {"status": "In Progress"},
]
for row in range(len(records)):
    print("status:", records[row]["status"])
    if records[row]["status"] == "Open":
        open_count += 1
print("open_count:", open_count)
