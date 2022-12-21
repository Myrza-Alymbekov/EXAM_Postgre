SELECT cour.name, cour.date_started, stud.name, ment.name, lang.name 
FROM user_course as cour
JOIN user_student as stud
ON cour.student_id = stud.id
JOIN user_mentor as ment
ON cour.mentor_id = ment.id
JOIN user_language as lang
ON cour.language_id = lang.id;