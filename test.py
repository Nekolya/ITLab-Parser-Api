from connect import connect_to_sqlite
import pprint
from datetime import datetime, date, time

pp = pprint.PrettyPrinter(indent=4)
        
cursor = connect_to_sqlite()

days_of_week = {
    1: 'Понедельник',
    2: 'Вторник',
    3: 'Среда',
    4: 'Четверг',
    5: 'Пятница',
    6: 'Суббота'
}

sqlite_select_Query = "SELECT day, week, schedule_calls.call_id, lessons.call_time, discipline_name, room_num, teacher_name  \
                        FROM lessons\
                        Join disciplines ON discipline_id = discipline\
                        Join schedule_calls ON call_id = call_num\
                        Join rooms On room_id = room\
                        JOIN teachers On teacher = teacher_id\
                        JOIN groups on group_id = group_num\
                        WHERE groups.group_name = 'ИКБО-07-18'\
                        order by day"
cursor.execute(sqlite_select_Query)
record = cursor.fetchall()

time_zone = None
    
today = datetime.now(tz=time_zone)

if today.month<8:
    first = date(today.year, 9, 1)
else: 
    first = date(today.year-1, 9, 1)
today_iso = today.isocalendar()
first_iso = first.isocalendar()
week = today_iso[1] - first_iso[1]
if not (first_iso[2] == 7):
    week+=1

print(week)

def today(group, week): 
    today = datetime.now(tz=time_zone)
    day_of_week = today.isocalendar()[2]
    sqlite_select_Query = "SELECT schedule_calls.call_id, lessons.call_time, discipline_name, room_num, teacher_name  \
                        FROM lessons\
                        Join disciplines ON discipline_id = discipline\
                        Join schedule_calls ON call_id = call_num\
                        Join rooms On room_id = room\
                        JOIN teachers On teacher = teacher_id\
                        JOIN groups on group_id = group_num\
                        WHERE groups.group_name = :group AND day = :day AND week = :week \
                        order by day"
    cursor.execute(sqlite_select_Query, {'group':group, 'day':day_of_week, 'week':week})
    record = cursor.fetchall()
    formatted_str = "="*30 + "\n"

    if len(record):

        formatted_str += days_of_week[day_of_week] + " " + str(today.day) + "." + str(today.month)

        for lesson in record:
            less = lesson[2] 
            if "кр." in less:
                exc = less.split("н.")[0]
                less = less.split("н.")[1]
            formatted_str+= "\n\n{0} пара {1} \n{2} {3}".format(lesson[0], lesson[1], less, lesson[3])

        
        formatted_str += "\n" + "="*30
        return formatted_str

    return "Нет пар"
    
print()
print(today('ИКБО-07-18', week%2))


