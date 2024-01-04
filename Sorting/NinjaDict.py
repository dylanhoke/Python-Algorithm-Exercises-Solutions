def solution(points):
   
    level_order = {
        "Recruit": 1,
        "Soldier": 2,
        "Warrior": 3,
        "Captain": 4,
        "Ninja": 5,
    }

    level_count = {}

    def level_cal(xp):
        if xp >= 0 and xp < 1000:
            return "Recruit"
        elif xp >= 1000 and xp < 5000:
            return "Soldier"
        elif xp >= 5000 and xp < 10000:
            return "Warrior"
        elif xp >= 10000 and xp < 50000:
            return "Captain"
        else:
            return "Ninja"

    for xp in points:
        level = level_cal(xp)
        level_count[level] = level_count.get(level, 0) + 1

    sorted_levels = sorted(
        level_count.items(),
        key=lambda x: (x[1], level_order[x[0]])
    )

    

    sorted_level_list = []

    for level, count in sorted_levels:
        sorted_level_list.append(f"{level} - {count}")

    return sorted_level_list[::-1]