import rangeutils as ru

nums = [0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# nums  0  1  1  0  1  1  1  0  0  0  1  1  1  0  0
#   >>     R  R     R  R  R           R  R  R
regions = ru.boolist_to_ranges(nums)
print(f"{f'to ranges: {regions}':64s}  <<  {[(list(r)) for r in regions]}")

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# nums  0  1  1  0  1  1  1  0  0  0  1  1  1  0  0
#   >>              R  R  R           R  R  R
regions = ru.boolist_to_ranges(nums, minlens=3)
print(f"{f'to ranges: {regions}':64s}  <<  {[(list(r)) for r in regions]}")

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# regs              R  R  R           R  R  R
#   >>  R  R  R  R           R  R  R           R  R
regions = ru.flip(regions, tail=len(nums))
print(f"{f'flip: {regions}':64s}  <<  {[(list(r)) for r in regions]}")

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# regs  R  R  R  R           R  R  R           R  R
#   >>              R  R  R           R  R  R
regions = ru.flip(regions)
print(f"{f'flip: {regions}':64s}  <<  {[(list(r)) for r in regions]}")

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# regs     R  R     R  R  R           R  R  R
#   >>     R  R  R  R  R  R           R  R  R
regions = ru.boolist_to_ranges(nums)
regions = ru.fill(regions)
print(f"{f'merge: {regions}':64s}  <<  {[(list(r)) for r in regions]}")

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# regs     R  R  R  R  R  R           R  R  R
#   >>        R  R  R  R                 R
regions = ru.trim(regions, trimsize=1)
print(f"{f'trim: {regions}':64s}  <<  {[(list(r)) for r in regions]}")

# idx   0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
# regs        R  R  R  R                 R
#   >>           R  R
regions = ru.trim(regions, trimsize=1)
print(f"{f'trim: {regions}':64s}  <<  {[(list(r)) for r in regions]}")
