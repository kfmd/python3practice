print("How many kilometers did you run today? (in Km)")
km = input()
km = float(km)
miles = km/1.60934
miles = round(miles,2)
print(f"Congratulations, you have run for {km} Km ({miles} mi)")
