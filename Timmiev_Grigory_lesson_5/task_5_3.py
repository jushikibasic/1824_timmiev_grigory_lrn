tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена', 'Василий',
          'Николай', 'Юрий', 'Яков', 'Мария'
          ]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
dist = len(tutors)
if dist > len(klasses):
    diff = dist - len(klasses)
    print("Для", diff, "учеников, не хватает классов.")
    for _ in range(1, diff + 1):
        klasses.append(None)
tur_nam_class = ((stud, aud) for (stud, aud) in zip(tutors, klasses))
print("tur_nam_class это:", type(tur_nam_class))
for _ in range(0, dist):
    print(next(tur_nam_class))
