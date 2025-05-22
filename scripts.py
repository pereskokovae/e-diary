import random

from datacenter.models import (Chastisement, Commendation, Lesson, Mark,                            
                                Schoolkid)


RANDOM_PRAISE = random.choice(["Хвалю!", "Молодец!", "Хорошая работа!", "Прекрасно!", "Так держать!"])


def fix_marks(schoolkid):
    schoolkid = Schoolkid.objects.get(full_name__contains="Фролов Иван")
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__lte=3)
    bad_marks.update(points=5)
    return schoolkid


def remove_chastisements(schoolkid):
    child_remarks = Chastisement.objects.filter(schoolkid=schoolkid)
    child_remarks.delete()
    return schoolkid


def create_commendation(schoolkid):
    try:
        lessons = list(Lesson.objects.filter(year_of_study=6))
    except ObjectDoesNotExist:
        print("Уроки не найдены")

    subject = random.choice(lessons)
    Commendation.objects.create(
            text=RANDOM_PRAISE,
            created=subject.date,
            schoolkid=schoolkid,
            subject=subject.subject,
            teacher=subject.teacher
            )
