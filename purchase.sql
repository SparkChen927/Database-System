create database purchase;
use purchase;
create table suppliers(
    sno int primary key unique comment '供应商号',
    sname varchar(20) comment '供应商名',
    type varchar(8) comment '类别',
    address varchar(50) comment '联系地址',
    settlement varchar(4) comment '结算方式',
    credit varchar(1) comment '信用等级',
    check ( type in ('优先', '考察', '消极淘汰', '积极淘汰') ),
    check ( settlement in ('现金', '转账') ),
    check ( credit in ('A', 'B', 'C') )
) comment '供应商';

create table goods(
    gno int primary key unique comment '货物编号',
    gname varchar(20) comment '货物名',
    price int comment '单价',
    sno int comment '供应商号',
    foreign key (sno) references suppliers (sno)
) comment '货物';

create table applications(
    ano int primary key unique comment '请购单号',
    gno int comment '货物编号',
    quantity int comment '购货数量',
    pname varchar(10) comment '采购员',
    adate datetime default now() comment '请购日期',
    astate varchar(6) comment '请购状态',
    foreign key (gno) references goods (gno),
    check ( astate in ('审核中', '已通过', '已拒绝') )
) comment '请购单';

create table buying(
    bno int primary key unique comment '采购单号',
    bstate varchar(4) comment '采购状态',
    bname varchar(10) comment '接货员',
    bdate datetime comment '采购日期',
    check ( bstate in ('收货', '验货', '退货') )
) comment '采购单';

create table documents(
    dno int primary key unique comment '单据号',
    ano int comment '请购单号',
    bno int comment '采购单号',
    foreign key (ano) references applications (ano),
    foreign key (bno) references buying (bno)
) comment '业务单据';

create table users(
    username varchar(20) primary key unique comment '用户名',
    password varchar(20) comment '密码'
);

insert into users values ('admin', '123456');
