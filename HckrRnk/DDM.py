#Designer Door Mat
N, M = map(int, input().split())

mid = N//2

micro_pattern = '.|.'
fill_char = '-'
main_text = 'WELCOME'

#top
for i in range(0,mid):
    print((micro_pattern+micro_pattern*(i*2)).center(M,fill_char))

#center
print(main_text.center(M,fill_char))

#button
for i in range(mid-1,-1,-1):
    print((micro_pattern+micro_pattern*(i*2)).center(M,fill_char))