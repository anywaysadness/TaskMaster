INSERT INTO roles (id, role_name) VALUES
(1, 'Администратор'),
(2, 'Пользователь');

INSERT INTO tags (id, tag_name) VALUES
(1, 'Выполнена'),
(2, 'В работе');


INSERT INTO users (id, user_first_name, user_second_name, user_middle_name, user_email, user_pass, user_position, user_date_creation, role_id) VALUES
(1, 'Максим', 'Курдюмов', 'Олегович', 'example@gmail.com', 'password', 'Ведущий инженер-программист','2024-06-28 05:40:30.682453+00:00', 1),
(2, 'Дмитрий', 'Качанов', 'Иванович', 'example2@gmail.com', 'password2', 'Ведущий инженер-программист','2024-06-28 05:41:30.682453+00:00', 2),
(3, 'Алексей', 'Молчанов', 'Владиславович', 'example3@gmail.com', 'password3', 'инженер','2024-06-28 05:42:30.682453+00:00', 2),
(4, 'Анатолий', 'Пузырьков', 'Артемович', 'example4@gmail.com', 'password4', 'Специалист технической поддержки','2024-06-28 05:43:30.682453+00:00', 2);

