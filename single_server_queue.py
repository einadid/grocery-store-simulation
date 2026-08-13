# GROCERY STORE - SINGLE SERVER QUEUE
arrival_rn  = [913, 727, 15, 948, 309]
service_rn  = [84, 10, 74, 53, 17, 79]

# Random Number to IAT
def get_iat(rn):
    if rn <= 125: return 1
    elif rn <= 250: return 2
    elif rn <= 375: return 3
    elif rn <= 500: return 4
    elif rn <= 625: return 5
    elif rn <= 750: return 6
    elif rn <= 875: return 7
    elif rn <= 1000: return 8
    else: return 0

# Random Number to Service Time
def get_service(rn):
    if rn <= 10: return 1
    elif rn <= 30: return 2
    elif rn <= 60: return 3
    elif rn <= 85: return 4
    elif rn <= 95: return 5
    elif rn <= 100: return 6
    else: return 0

# coustomer data store
results = []

prev_arrival      = 0   
prev_service_end  = 0   

for i in range(6):

    customer = i + 1

    # ARRIVAL TIME 
    if customer == 1:
        iat          = "-"
        arrival_time = 0
    else:
        iat          = get_iat(arrival_rn[i - 1])
        arrival_time = prev_arrival + iat

    # SERVICE TIME
    service_time = get_service(service_rn[i]) #0

    # SERVICE BEGINS
    if arrival_time > prev_service_end:
        service_begins = arrival_time
    else:
        service_begins = prev_service_end

    # WAITING TIME
    waiting_time = service_begins - arrival_time

    # SERVICE ENDS
    service_ends = service_begins + service_time

    # TIME IN SYSTEM
    time_in_system = service_ends - arrival_time

    # IDLE TIME
    if arrival_time > prev_service_end:
        idle_time = arrival_time - prev_service_end
    else:
        idle_time = 0

    # customer data save 
    results.append({
        "Customer"       : customer,
        "IAT"            : iat,
        "Arrival Time"   : arrival_time,
        "Service Time"   : service_time,
        "Service Begins" : service_begins,
        "Waiting Time"   : waiting_time,
        "Service Ends"   : service_ends,
        "Time in System" : time_in_system,
        "Idle Time"      : idle_time
    })

    # next customer data update
    prev_arrival     = arrival_time
    prev_service_end = service_ends


# Table Print 
print("=" * 90)
print(f"{'Cust':>5} {'IAT':>5} {'Arr':>5} {'Svc':>5} {'Begins':>7} {'Wait':>6} {'Ends':>6} {'System':>7} {'Idle':>6}")
print("=" * 90)

for r in results:
    print(f"{r['Customer']:>5} "
          f"{str(r['IAT']):>5} "
          f"{r['Arrival Time']:>5} "
          f"{r['Service Time']:>5} "
          f"{r['Service Begins']:>7} "
          f"{r['Waiting Time']:>6} "
          f"{r['Service Ends']:>6} "
          f"{r['Time in System']:>7} "
          f"{r['Idle Time']:>6}")

print("=" * 90)


# In Totals 
total_waiting    = sum(r["Waiting Time"]   for r in results)
total_service    = sum(r["Service Time"]   for r in results)
total_in_system  = sum(r["Time in System"] for r in results)
total_idle       = sum(r["Idle Time"]      for r in results)
total_customers  = len(results)
total_run_time   = results[-1]["Service Ends"]
num_waited       = sum(1 for r in results if r["Waiting Time"] > 0)

iat_values       = [r["IAT"] for r in results if r["IAT"] != "-"]
total_iat        = sum(iat_values)


# Print answer
print("\n")
print("         FINAL ANSWERS")
print("=" * 50)

print(f"\n1) Average Waiting Time")
print(f"   = {total_waiting} / {total_customers}")
print(f"   = {total_waiting / total_customers} min")

print(f"\n2) Probability Customer Has to Wait")
print(f"   = {num_waited} / {total_customers}")
print(f"   = {round(num_waited / total_customers, 3)} = {round(num_waited / total_customers * 100, 1)}%")

print(f"\n3) Fraction of Idle Time")
print(f"   = {total_idle} / {total_run_time}")
print(f"   = {round(total_idle / total_run_time, 2)} = {round(total_idle / total_run_time * 100)}%")

print(f"\n4) Average Service Time")
print(f"   = {total_service} / {total_customers}")
print(f"   = {total_service / total_customers} min")

print(f"\n5) Average Time Between Arrivals")
print(f"   = {total_iat} / {len(iat_values)}")
print(f"   = {total_iat / len(iat_values)} min")

print(f"\n6) Average Waiting Time (Those Who Waited)")
print(f"   = {total_waiting} / {num_waited}")
print(f"   = {total_waiting / num_waited} min")

print(f"\n7) Average Time Spent in System")
print(f"   = {total_in_system} / {total_customers}")
print(f"   = {total_in_system / total_customers} min")

print("\n" + "=" * 50)