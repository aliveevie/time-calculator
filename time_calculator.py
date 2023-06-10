def add_time(start, duration, day=''):
    condition = None
    n = ''
    length = 0
    index = ''
    new_time = None
    start = start.split()
    condition = start[1]
    starthour, startmin = map(int, start[0].split(':'))
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if condition.upper() == 'PM':
        starthour += 12

    # extract the duration properties
    duration = duration.split()
  
    durhour, durmin = duration[0].split(':')
    newhour = int(starthour) + int(durhour)
    newmin = int(startmin) + int(durmin)
    if newmin > 60:
        newmin %= 60
        newhour += 1 
    
    
   
    # Calculate the number of days
    n = newhour // 24
    length = n
    
    new_time = newhour % 24
   
    if new_time == 0:
        new_time = '12:' + str(newmin).zfill(2) + ' AM'
    elif new_time < 12:
        new_time = str(newhour % 24) + ':' + str(newmin).zfill(2) + ' AM'
    elif new_time == 12:
        new_time = '12:' + str(newmin).zfill(2) + ' PM'
    else:
        new_time = str(newhour % 24  - 12) + ':' + str(newmin).zfill(2) + ' PM'
        
    # Handle overflow of minutes
     
    if(day):
        day = day.lower()
        index = days.index(day)
        actualindex = index + length
        if actualindex > 7:
            actualindex = actualindex % 7
        day = days[actualindex].capitalize()
        new_time += ', ' + day
    if n == 1:
        new_time += ' (next day)'
    elif n > 1:
        new_time += ' (' + str(n) + ' days later)'
        
   
    return new_time

def number_days(hours, min):
    hours = hours * 60
    totalmins = hours + min
    converthours = totalmins / 60
    days = converthours / 24
    return round(days)