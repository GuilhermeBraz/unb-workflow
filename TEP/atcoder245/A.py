# One day, Takahashi got up at exactly B minutes past A o'clock (in 24-hour clock), and Aoki got up at exactly D minutes and 1 second past C o'clock.
# If Takahashi got up earlier than Aoki, print Takahashi; otherwise, print Aoki.
import datetime
A, B, C, D = map(int, input().split())

takahashi = datetime.time(A, B)
aoki = datetime.time(C, D, 1)

print('Takahashi' if takahashi < aoki else 'Aoki')
