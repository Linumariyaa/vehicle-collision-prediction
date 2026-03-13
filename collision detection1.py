# Vehicle Collision Detection (Simple Version)

speed = float(input("Enter vehicle speed (km/h): "))
distance = float(input("Enter distance between vehicles (m): "))

safe_distance = speed * 0.5

if distance < safe_distance:
    print("⚠ Collision Risk Detected")
else:
    print("✅ Safe Distance")
