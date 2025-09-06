create table lessons
(
    id      integer primary key autoincrement,
    title   text,
    teacher text,
    unit    integer

);

-- SAVE
insert into lessons (id , title , teacher , unit) values (1, 'zist', 'ebrahimi',3);
insert into lessons (id , title , teacher , unit) values (2, 'physic', 'hashemi',1);
insert into lessons (id , title , teacher , unit) values (3, 'shimi', 'azimi',2);
insert into lessons (id , title , teacher , unit) values (4, 'riazi', 'fatollah',4);


-- EDIT
update lessons set title='farsi', teacher='nourani', unit=4 where id =3;


-- DELETE
delete from lessons where id=1;

-- REPORT / FIND
select * from products;

-- SORT
select * from lessons order by id;

select * from lessons order by id desc;