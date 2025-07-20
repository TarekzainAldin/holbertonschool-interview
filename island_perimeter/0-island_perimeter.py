def island_perimeter(grid):
    perimeter = 0  # نبدأ المحيط من 0

    for i in range(len(grid)):  # نمر على الصفوف واحد واحد
        for j in range(len(grid[0])):  # نمر على الأعمدة داخل كل صف
            if grid[i][j] == 1:  # إذا كانت الخلية يابسة (1)
                perimeter += 4  # نضيف 4 للمحيط لأننا نفترض مبدئيًا أن الخلية لها 4 أضلاع

                # إذا كانت الخلية التي فوقها (i - 1) يابسة أيضًا، نخصم 2 لأن هناك ضلعين متلاصقين
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # إذا كانت الخلية التي على يسارها (j - 1) يابسة أيضًا، نخصم 2 لنفس السبب
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter  # نُرجع المحيط النهائي
