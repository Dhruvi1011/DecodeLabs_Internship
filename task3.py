print("=" * 60)
print("      AI SHOPPING RECOMMENDATION SYSTEM")
print("=" * 60)

products = {
    "Laptop": ["technology", "coding", "study"],
    "Desktop PC": ["technology", "gaming", "coding"],
    "Smartphone": ["technology", "communication", "gaming"],
    "Tablet": ["technology", "study", "entertainment"],
    "Smart Watch": ["technology", "fitness", "health"],
    "Fitness Band": ["fitness", "health", "sports"],
    "Headphones": ["music", "technology", "gaming"],
    "Bluetooth Speaker": ["music", "entertainment", "technology"],
    "Gaming Mouse": ["gaming", "technology", "coding"],
    "Gaming Keyboard": ["gaming", "technology", "coding"],
    "Monitor": ["technology", "gaming", "study"],
    "Webcam": ["technology", "study", "communication"],
    "Printer": ["study", "office", "technology"],

    "Running Shoes": ["sports", "fitness", "running"],
    "Football": ["sports", "outdoor", "fitness"],
    "Cricket Bat": ["sports", "outdoor", "fitness"],
    "Yoga Mat": ["fitness", "health", "sports"],
    "Dumbbells": ["fitness", "health", "gym"],
    "Protein Shaker": ["fitness", "gym", "health"],

    "Backpack": ["travel", "study", "college"],
    "Travel Bag": ["travel", "outdoor", "adventure"],
    "Water Bottle": ["travel", "fitness", "health"],
    "Power Bank": ["travel", "technology", "mobile"],
    "Travel Pillow": ["travel", "comfort", "adventure"],

    "Novel Book": ["reading", "education", "entertainment"],
    "Notebook": ["study", "college", "education"],
    "Pen Set": ["study", "office", "education"],
    "Study Lamp": ["study", "education", "technology"],

    "Coffee Maker": ["kitchen", "home", "lifestyle"],
    "Air Fryer": ["kitchen", "health", "home"],
    "Mixer Grinder": ["kitchen", "home", "cooking"],
    "Vacuum Cleaner": ["home", "cleaning", "lifestyle"],

    "T-Shirt": ["fashion", "casual", "lifestyle"],
    "Jeans": ["fashion", "casual", "lifestyle"],
    "Sneakers": ["fashion", "sports", "casual"],
    "Jacket": ["fashion", "winter", "lifestyle"],

    "Camera": ["photography", "travel", "technology"],
    "Tripod": ["photography", "technology", "travel"],
    "Drone": ["photography", "technology", "adventure"]
}

print("\nAvailable Interests:")
all_interests = set()

for tags in products.values():
    all_interests.update(tags)

for interest in sorted(all_interests):
    print("-", interest)

user_input = input(
    "\nEnter your interests (comma separated): "
).lower()

user_interests = [item.strip() for item in user_input.split(",")]

recommendations = []

for product, tags in products.items():
    score = 0

    for interest in user_interests:
        if interest in tags:
            score += 1

    recommendations.append((product, score))

recommendations.sort(key=lambda x: x[1], reverse=True)

print("\n" + "=" * 60)
print("          RECOMMENDED PRODUCTS")
print("=" * 60)

found = False

print("\nTop 5 Recommended Products:\n")

count = 0
for product, score in recommendations:
    if score > 0:
        print(f"{product:<20} Match Score: {score}")
        count += 1

        if count == 5:
            break

        found = True

if not found:
    print("No matching products found.")
    print("Try interests such as:")
    print("technology, gaming, fitness, travel, study")

print("\nThank you for using the Shopping Recommendation System!")