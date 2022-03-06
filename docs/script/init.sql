-- auto-generated definition
drop table data_ssqmodel;
create table data_ssqmodel
(
    id                  bigint auto_increment
        primary key,
    qiCi                varchar(20)    not null,
    kaiJiangRiQi        varchar(20)    not null,
    hongYi              int            not null,
    hongEr              int            not null,
    hongSan             int            not null,
    hongSi              int            not null,
    hongWu              int            not null,
    hongLiu             int            not null,
    langQiu             int            not null,
    jiangChiJinEr       decimal(12, 2) not null,
    yiDengJiangZhuShu   int            not null,
    yiDengJiangJiangJin decimal(12, 2) not null,
    erDengJiangZhuShu   int            not null,
    erDengJiangJiangJin decimal(12, 2) not null
);




INSERT INTO data_ssqmodel
(id, qiCi, kaiJiangRiQi, hongYi, hongEr, hongSan, hongSi, hongWu, hongLiu, langQiu, jiangChiJinEr, yiDengJiangZhuShu, yiDengJiangJiangJin, erDengJiangZhuShu, erDengJiangJiangJin)
VALUES (1, '01001', '2022-03-04', 1, 2, 3, 4, 5, 6, 7, 11.00, 12, 133.00, 14, 15.00);
INSERT INTO data_ssqmodel
(id, qiCi, kaiJiangRiQi, hongYi, hongEr, hongSan, hongSi, hongWu, hongLiu, langQiu, jiangChiJinEr, yiDengJiangZhuShu, yiDengJiangJiangJin, erDengJiangZhuShu, erDengJiangJiangJin)
VALUES (2, '01002', '2022-03-04', 1, 2, 3, 4, 5, 6, 7, 11.00, 12, 133.00, 14, 15.00);
INSERT INTO data_ssqmodel
(id, qiCi, kaiJiangRiQi, hongYi, hongEr, hongSan, hongSi, hongWu, hongLiu, langQiu, jiangChiJinEr, yiDengJiangZhuShu, yiDengJiangJiangJin, erDengJiangZhuShu, erDengJiangJiangJin)
VALUES (3, '01003', '2022-03-04', 1, 2, 3, 4, 5, 6, 7, 11.00, 12, 133.00, 14, 15.00);