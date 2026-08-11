print("Hello this is treasure hunt")
print("lets find out the treasure")

room_map = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": ["G"],
    "G": [""]
}

print("    A    ")
print("   / \\   ")
print("  B   C  ")
print("   \\ /   ")
print("    D    ")
print("    -    ")
print("    G    ")

print("Doors from each room", room_map)


# BFS - Breadth First Search
def bfs(start, goal):
    to_do = [start]
    visited = []
    order = []

    while to_do:
        room = to_do.pop(0)

        if room in visited:
            continue