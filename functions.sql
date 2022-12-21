CREATE OR REPLACE FUNCTION get_course_id_by_email(stud_email VARCHAR(50))
RETURNS BIGINT AS $$
SELECT id FROM user_course
WHERE user_course.student_id = (SELECT id FROM user_student WHERE email = stud_email)
$$ LANGUAGE SQL




-- SELECT get_course_id_by_email('aman@mail.ru');
-- SELECT get_course_id_by_email('aapina@bk.ru');
-- SELECT get_course_id_by_email('spencer@microsoft.com');



