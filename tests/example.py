import rangeutils as ru


def check(ranges: list[range], ans: list[list[int]]) -> bool:
    res = [(list(r)) for r in ranges]
    if len(res) != len(ans):
        return False
    return all(sub1 == sub2 for sub1, sub2 in zip(res, ans, strict=False))


nums = [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# nums  0  1  1  0  1  1  1  0  0  0  1  1  1  0  0
#   >>     R  R     R  R  R           R  R  R
regions = ru.boolist_to_ranges(nums)
msg = f"{f'to ranges: {regions}':64s}  <<  {[(list(r)) for r in regions]}"
msg += f" ... {check(regions, ans=[[1, 2], [4, 5, 6], [10, 11, 12]])}"
print(msg)

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# nums  0  1  1  0  1  1  1  0  0  0  1  1  1  0  0
#   >>              R  R  R           R  R  R
regions = ru.boolist_to_ranges(nums, minlens=3)
msg = f"{f'to ranges: {regions}':64s}  <<  {[(list(r)) for r in regions]}"
msg += f" ... {check(regions, ans=[[4, 5, 6], [10, 11, 12]])}"
print(msg)

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# regs              R  R  R           R  R  R
#   >>  R  R  R  R           R  R  R           R  R
regions = ru.flip(regions, tail=len(nums))
msg = f"{f'to ranges: {regions}':64s}  <<  {[(list(r)) for r in regions]}"
msg += f" ... {check(regions, ans=[[0, 1, 2, 3], [7, 8, 9], [13, 14]])}"
print(msg)

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# regs  R  R  R  R           R  R  R           R  R
#   >>              R  R  R           R  R  R
regions = ru.flip(regions)
msg = f"{f'to ranges: {regions}':64s}  <<  {[(list(r)) for r in regions]}"
msg += f" ... {check(regions, ans=[[4, 5, 6], [10, 11, 12]])}"
print(msg)

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# regs     R  R     R  R  R           R  R  R
#   >>     R  R  R  R  R  R           R  R  R
regions = ru.boolist_to_ranges(nums)
regions = ru.fill(regions)
msg = f"{f'to ranges: {regions}':64s}  <<  {[(list(r)) for r in regions]}"
msg += f" ... {check(regions, ans=[[1, 2, 3, 4, 5, 6], [10, 11, 12]])}"
print(msg)

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# regs     R  R  R  R  R  R           R  R  R
#   >>        R  R  R  R                 R
regions = ru.trim(regions, trimsize=1)
msg = f"{f'to ranges: {regions}':64s}  <<  {[(list(r)) for r in regions]}"
msg += f" ... {check(regions, ans=[[2, 3, 4, 5], [11]])}"
print(msg)

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# regs        R  R  R  R                 R
#   >>           R  R
regions = ru.trim(regions, trimsize=1)
msg = f"{f'to ranges: {regions}':64s}  <<  {[(list(r)) for r in regions]}"
msg += f" ... {check(regions, ans=[[3, 4]])}"
print(msg)
