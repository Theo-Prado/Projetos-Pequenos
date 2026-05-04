inventory = {
    "apple": [5, "Code: 882629"],
    "grape": [12, "Code: 77652"],
    "watermelon": [20, "Code: 227352"]
}

for fruit, details in inventory.items():
  print(f"Fruit: {fruit}")
  for detail in details:
    print(detail)
  print("-" * 20)
