statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}


def main():
    print(online_count(statuses))


def online_count(dictionary):
    count = 0
    
    for value in dictionary.values():
        if value == "online":
            count += 1
            
    return count
    
    
main()
