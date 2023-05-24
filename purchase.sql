create database if not exists purchase;
use purchase;

drop table if exists suppliers;
create table suppliers(
    sno varchar(10) primary key unique comment '供应商号',
    sname varchar(20) comment '供应商名',
    type varchar(8) comment '类别',
    address varchar(50) comment '联系地址',
    settlement varchar(4) comment '结算方式',
    credit varchar(1) comment '信用等级',
    check ( type in ('优先', '考察', '消极淘汰', '积极淘汰') ),
    check ( settlement in ('现金', '转账') ),
    check ( credit in ('A', 'B', 'C') )
) comment '供应商';

insert into suppliers values ('01', '星际和平公司', '优先', '上海', '转账', 'A');
insert into suppliers values ('02', '雅利洛', '消极淘汰', '贝洛伯格', '转账', 'B');
insert into suppliers values ('03', '仙舟', '考察', '罗浮', '转账', 'B');
insert into suppliers values ('04', '星穹列车', '优先', '', '现金', 'A');
insert into suppliers values ('05', '愚人众', '积极淘汰', '俄罗斯', '转账', 'C');

drop table if exists goods;
create table goods(
    gno varchar(10) primary key unique comment '货物编号',
    gname varchar(20) comment '货物名',
    price float comment '单价',
    sno varchar(10) comment '供应商号',
    foreign key (sno) references suppliers (sno)
) comment '货物';

insert into goods values ('01', '星琼', 5, '01');
insert into goods values ('02', '星琼', 10, '02');
insert into goods values ('03', '星琼', 7, '03');
insert into goods values ('04', '星琼', 6, '04');
insert into goods values ('05', '棒球棒', 80, '01');
insert into goods values ('06', '棒球棒', 60, '04');
insert into goods values ('07', '原石', 8, '05');
insert into goods values ('08', '铁锹', 40, '01');
insert into goods values ('09', '铁锹', 35, '05');

drop table if exists applications;
create table applications(
    ano varchar(10) primary key unique comment '请购单号',
    gno varchar(10) comment '货物编号',
    quantity int comment '购货数量',
    pname varchar(10) comment '采购员',
    adate datetime default now() comment '请购日期',
    astate varchar(6) comment '请购状态',
    foreign key (gno) references goods (gno),
    check ( astate in ('审核中', '已通过', '已拒绝') )
) comment '请购单';

insert into applications values ('01', '04', '100', '张三', default, '审核中');

drop table if exists buying;
create table buying(
    bno varchar(10) primary key unique comment '采购单号',
    bstate varchar(4) comment '采购状态',
    bname varchar(10) comment '接货员',
    bdate datetime comment '采购日期',
    check ( bstate in ('收货', '验货', '退货') )
) comment '采购单';

drop table if exists documents;
create table documents(
    dno varchar(10) primary key unique comment '单据号',
    ano varchar(10) comment '请购单号',
    bno varchar(10) comment '采购单号',
    foreign key (ano) references applications (ano),
    foreign key (bno) references buying (bno)
) comment '业务单据';

drop table if exists users;
create table users(
    username varchar(20) primary key unique comment '用户名',
    password varchar(20) comment '密码'
);

insert into users values ('admin', '123456');

drop trigger if exists sup_del;
delimiter //
create trigger sup_del before delete
on suppliers for each row
    begin
        delete from goods where goods.sno = old.sno;
    end//

drop trigger if exists goods_del;
delimiter //
create trigger goods_del before delete
on goods for each row
    begin
        delete from applications where applications.gno = old.gno;
    end //

drop trigger if exists app_del;
delimiter //
create trigger app_del before delete
on applications for each row
    begin
        delete from buying where bno in (select bno from documents where documents.ano = old.ano);
    end //

drop trigger if exists buy_del;
delimiter //
create trigger buy_del before delete
on buying for each row
    begin
        delete from applications where ano in (select ano from documents where documents.bno = old.bno);
        delete from documents where documents.bno = old.bno;
    end //

drop procedure if exists anly;
delimiter //
create procedure anly()
    begin
        drop view if exists analyse;
        create view analyse as select gname, count(*) from goods group by gname;
    end //
