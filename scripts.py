import random

from django.core.exceptions import ObjectDoesNotExist
from datacenter.models import (Chastisement, Commendation, Lesson, Mark,                            
                                Schoolkid)


RANDOM_PRAISE = random.choice(["Хвалю!", "Молодец!", "Хорошая работа!", "Прекрасно!", "Так держать!"])


def fix_marks(schoolkid):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains="Фролов Иван")
    except ObjectDoesNotExist:
        print("Ученик не найден")
        
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    bad_marks.update(points=5)
    return schoolkid


def remove_chastisements(schoolkid):
    child_remarks = Chastisement.objects.filter(schoolkid=schoolkid)
    child_remarks.delete()
    return schoolkid


def create_commendation(schoolkid):
    lessons = list(Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
        ))
    if not lessons:
        print("Уроки не найдены")
    subject = random.choice(lessons)
    Commendation.objects.create(
            text=RANDOM_PRAISE,
            created=subject.date,
            schoolkid=schoolkid,
            subject=subject.subject,
            teacher=subject.teacher
            )
