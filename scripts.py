import random

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,                            
                                Schoolkid)


RANDOM_PRAISE = random.choice(["Хвалю!", "Молодец!", "Хорошая работа!", "Прекрасно!", "Так держать!"])


def get_schoolkid():
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains="Фролов Иван")
    except MultipleObjectsReturned:
        print(f"Найдено больше учеников, а именно {schoolkid.count()}")
    except ObjectDoesNotExist:
        print("Ученик не найден")
    return schoolkid


def fix_marks(schoolkid):  
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    bad_marks.update(points=5)


def remove_chastisements(schoolkid):
    child_remarks = Chastisement.objects.filter(schoolkid=schoolkid)
    child_remarks.delete()



def create_commendation(schoolkid):
    lessons = list(Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
        ))
    if not lessons:
        print("Уроки не найдены")
        return
    lesson_last = sorted(lessons.values()).last()
    Commendation.objects.create(
            text=RANDOM_PRAISE,
            created=lesson_last.date,
            schoolkid=schoolkid,
            subject=lesson_last.subject,
            teacher=lesson_last.teacher
            )
