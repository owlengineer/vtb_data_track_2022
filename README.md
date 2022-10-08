# VTB DataTrack 2022

Здравствуйте!

Наша команда **XBCData** презентует решение data-трека для хакатона от ВТБ.

Задача -- необходимо проанализировать выборку из несвязанных между собой каналов информации и выделить самые важные для клиента 2−3 новости. То есть, основываясь на заданной роли сотрудника, предлагать релевантные результаты не только по ключевым словам, но и по сути текста. Также, сформировать тренды и инсайты.

## Deploy

```
docker-compose up
```

## API

API -- набор http GET-запросов:

```
/insights  -- получить json с инсайтами                         

/trends  -- получить json с массивом трендов                     

/digest/<role>  -- аргумент <role>=director/accountant          
```

Роуты сервиса прописаны тут -- https://github.com/owlengineer/vtb_data_track_2022/blob/main/src/api.py

## Материалы

google drive - https://drive.google.com/drive/u/0/folders/1u2syZI7JopDamVcQ3VI3CQYuBeRW6obs
 
