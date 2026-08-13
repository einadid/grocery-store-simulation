# GROCERY STORE - SINGLE SERVER QUEUE

# Random Number to IAT
def get_iat(rn):
    if rn <= 125:
        return 1
    elif rn <= 250:
        return 2
    elif rn <= 375:
        return 3
    elif rn <= 500:
        return 4
    elif rn <= 625:
        return 5
    elif rn <= 750:
        return 6
    elif rn <= 875:
        return 7
    elif rn <= 1000:
        return 8
    else:
        return 0

# Random Number to Service Time
def get_service(rn):
    if rn <= 10:
        return 1
    elif rn <= 30:
        return 2
    elif rn <= 60:
        return 3
    elif rn <= 85:
        return 4
    elif rn <= 95:
        return 5
    elif rn <= 100:
        return 6
    else:
        return 0

# -------------------------
# USER INPUT
# -------------------------
n = int(input("Enter number of customers: "))

arrival_rn = list(map(int, input(f"Enter {n-1} arrival random numbers: ").split()))
service_rn = list(map(int, input(f"Enter {n} service random numbers: ").split()))

# input validation
if len(arrival_rn) != n - 1:
    print(f"Error: You must enter exactly {n-1} arrival random numbers.")
    exit()

if len(service_rn) != n:
    print(f"Error: You must enter exactly {n} service random numbers.")
    exit()

# -------------------------
# SIMULATION
# -------------------------
results = []

prev_arrival = 0
prev_service_end = 0

for i in range(n):

    customer = i + 1

    # ARRIVAL TIME
    if customer == 1:
        iat = "-"
        arrival_time = 0
    else:
        iat = get_iat(arrival_rn[i - 1])
        arrival_time = prev_arrival + iat

    # SERVICE TIME
    service_time = get_service(service_rn[i])

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

    # SAVE DATA
    results.append({
        "Customer": customer,
        "IAT": iat,
        "Arrival Time": arrival_time,
        "Service Time": service_time,
        "Service Begins": service_begins,
        "Waiting Time": waiting_time,
        "Service Ends": service_ends,
        "Time in System": time_in_system,
        "Idle Time": idle_time
    })

    # UPDATE
    prev_arrival = arrival_time
    prev_service_end = service_ends

# -------------------------
# TABLE PRINT
# -------------------------
print("\n" + "=" * 90)
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

# -------------------------
# TOTALS
# -------------------------
total_waiting    = sum(r["Waiting Time"]   for r in results)
total_service    = sum(r["Service Time"]   for r in results)
total_in_system  = sum(r["Time in System"] for r in results)
total_idle       = sum(r["Idle Time"]      for r in results)
total_customers  = len(results)
total_run_time   = results[-1]["Service Ends"]
num_waited       = sum(1 for r in results if r["Waiting Time"] > 0)

iat_values = [r["IAT"] for r in results if r["IAT"] != "-"]
total_iat  = sum(iat_values)

# -------------------------
# FINAL ANSWERS
# -------------------------
print("\n")
print("         FINAL ANSWERS")
print("=" * 50)

print(f"\n1) Average Waiting Time")
print(f"   = {total_waiting} / {total_customers}")
print(f"   = {total_waiting / total_customers:.2f} min")

print(f"\n2) Probability Customer Has to Wait")
print(f"   = {num_waited} / {total_customers}")
print(f"   = {num_waited / total_customers:.3f} = {(num_waited / total_customers) * 100:.1f}%")

print(f"\n3) Fraction of Idle Time")
print(f"   = {total_idle} / {total_run_time}")
print(f"   = {total_idle / total_run_time:.2f} = {(total_idle / total_run_time) * 100:.0f}%")

print(f"\n4) Average Service Time")
print(f"   = {total_service} / {total_customers}")
print(f"   = {total_service / total_customers:.2f} min")

if len(iat_values) > 0:
    print(f"\n5) Average Time Between Arrivals")
    print(f"   = {total_iat} / {len(iat_values)}")
    print(f"   = {total_iat / len(iat_values):.2f} min")
else:
    print(f"\n5) Average Time Between Arrivals")
    print("   = Not applicable for only 1 customer")

if num_waited > 0:
    print(f"\n6) Average Waiting Time (Those Who Waited)")
    print(f"   = {total_waiting} / {num_waited}")
    print(f"   = {total_waiting / num_waited:.2f} min")
else:
    print(f"\n6) Average Waiting Time (Those Who Waited)")
    print("   = 0 min (No customer waited)")

print(f"\n7) Average Time Spent in System")
print(f"   = {total_in_system} / {total_customers}")
print(f"   = {total_in_system / total_customers:.2f} min")

print("\n" + "=" * 50)