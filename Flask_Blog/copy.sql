INSERT INTO
  temp_user (
    firstname,
    lastname,
    username,
    email,
    password_hash,
    date_added,
    last_modify,
    administrator,
    about_me,
    last_seen
  )
SELECT
  firstname,
  lastname,
  username,
  email,
  password_hash,
  date_added,
  last_modify,
  administrator,
  about_me,
  last_seen
FROM
  user;