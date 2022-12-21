from user.models import *

language1 = Language.objects.create(name='Python', month_to_learn=6)
language2 = Language.objects.create(name='Java Script', month_to_learn=6)
language3 = Language.objects.create(name='UX-UI design', month_to_learn=2)

student1 = Student.objects.create(name='Amanov Aman', email='aman@mail.ru', phone_number='+996700989898',
                                  work_study_place='School #13', has_own_notebook=True, preferred_os='windows')
student2 = Student.objects.create(name='Apina Alena', email='aapina@bk.ru', phone_number='0550888888',
                                  work_study_place='TV', has_own_notebook=True, preferred_os='Mac')
student3 = Student.objects.create(name='Phil Spencer', email='spencer@microsoft.com', phone_number='0508312312',
                                  work_study_place='Microsoft Gaming', has_own_notebook=False, preferred_os='Linux')

mentor1 = Mentor.objects.create(name='Ilona Maskova', email='imask@gmail.com', phone_number='0500545454',
                                experience='2021-10-23')
mentor2 = Mentor.objects.create(name='Halil Nurmuhametov', email='halil@gmail.com', phone_number='0709989876',
                                main_work='Univercity of Fort Collins', experience='2010-09-18')

Course.objects.create(name='Python-21', mentor=mentor2, student=student1,
                      date_started='2022-08-01', language=language1)
Course.objects.create(name='Python-21', mentor=mentor2, student=student2,
                      date_started='2022-08-01', language=language1)

Course.objects.create(name='UXUI design', mentor=mentor1, student=student3,
                      date_started='2022-08-22', language=language3)
