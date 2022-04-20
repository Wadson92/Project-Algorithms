def study_schedule(permanence_period, target_time):
    try:
        cont = 0
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                cont += 1
        return cont
    except TypeError:
        return None
