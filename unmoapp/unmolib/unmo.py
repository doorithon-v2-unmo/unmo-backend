def unmo_diff(lectures_list):
    day_array = [True for _ in range(288)]
    week_array = [day_array[:], day_array[:], day_array[:], day_array[:], day_array[:]]

    available_time = [[], [], [], [], []]

    for each_lectures in lectures_list:

        for lecture in each_lectures:
            for time_point in range(lecture["start_time"], lecture["end_time"]):
                week_array[lecture["day"]][time_point] = False

    for day in range(5):

        start_flag = 0
        check_flag = False

        for time_point in range(288):
            if not check_flag:
                if not week_array[day][time_point]:
                    available_time[day].append({"start_time": start_flag, "end_time": time_point - 1})
                    check_flag = True
            if check_flag:
                if week_array[day][time_point]:
                    start_flag = time_point
                    check_flag = False

        if start_flag < 287:
            available_time[day].append({"start_time": start_flag, "end_time": 287})

    return available_time
