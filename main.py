import datetime
import webbrowser
from application.salary import calculate_salary
from application.db.people import get_employees
from application.video import get_video_info


def main():
    print("Текущая дата: ", datetime.date.today())
    calculate_salary()
    get_employees()
    video_url = "https://www.youtube.com/watch?v=wza_1tr6CfU"
    watch_url = get_video_info(video_url)
    webbrowser.open(watch_url)

if __name__ == '__main__':
    main()