def calculate_total_time(data):
    '''
    Calculates the total time user was active today
        calculation : 1 activity == 1 minute, total number of activities / 60 = total hours
        return <float:hours>
    '''
    return len(data) / 60
        

def calculate_activity_hours(data, total_hours, productivity=1):
    '''
        param : productivity = 1  productive
                             = 2  non productive
        return : {
            'hours': <float>,
            'percentage': <float>
        }
    '''
    hours = 0
    for activity in data:
        if not activity.productive == productivity:
            continue
        hours += 1
    hours = round(hours/60,1)
    return {'hours': hours, 'percentage': round(hours / total_hours, 2)*100}

def calculate_break_hours(total_hours):
    '''
        return : {
            'hours': <float>,
            'percentage': <float>
        }
    '''
    hours = 0.5
    return {'hours': hours, 'percentage': round(hours / total_hours, 2)*100}


def calculate_activity(data):
    '''
    return : {
            'productive': {
                'hours': <float>,
                'percentage': <float>
            },
            'non-productive': {
                'hours': <float>,
                'percentage': <float>
            },
            'break': {
                'hours': <float>,
                'percentage': <float>
            },
        }
    '''
    total_hours = calculate_total_time(data)
    productive = calculate_activity_hours(data,total_hours,1)
    nonproductive = calculate_activity_hours(data,total_hours,0)
    break_hours = calculate_break_hours(total_hours)
    nonproductive['percentage'] = round(nonproductive['percentage'] - break_hours['percentage'])
    return {
        'productive':productive,
        'nonproductive':nonproductive,
        'break': break_hours
    }
    