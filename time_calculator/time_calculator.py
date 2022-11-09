def add_time(start, add, day=None):
    time, period = start.split()
    hour, minutes = map(int, time.split(':'))  # converting everything to int
    addH, addM = map(int, add.split(':'))
    midday = ('PM', 'AM')
    new_day = ''
    later = ''

    carry, minutes = divmod(minutes + addM, 60)
    hour += carry
    # 'cycles' is # of 12-hours (half days) that 'hour' exceeds
    cycles, hour = divmod(hour + addH, 12)
    period = abs(midday.index(period)-(cycles % 2))
    # 'passed' describes the number of days passed
    passed = (period + cycles) // 2

    if hour == 0:  # basically an edge case created from my modulus calculations
        hour = 12

    if minutes < 10:  # standardizing time format, 12:1 -> 12:01
        minutes = f'0{minutes}'

    if day:
        week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday')
        new_day = f', {week[(week.index(day.capitalize()) + passed) % 7]}'

    # Just some string formatting
    if passed == 1:
        later = ' (next day)'
    elif passed != 0:
        later = f' ({passed} days later)'

    new_time = f'{hour}:{minutes} {midday[period]}{new_day}{later}'

    return new_time
