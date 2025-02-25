#kuang@node01 /nas2/kuang/MyPrograms/query_anything
#$ cat time_ser.sql
REPLACE INTO "time_srs" OVERWRITE ALL
WITH "ext" AS (
  SELECT *
  FROM TABLE(
    EXTERN(
      '{"type":"local","baseDir":"/nas2/kuang/MyPrograms/query_anything/","filter":"time_srs.csv"}',
      '{"type":"csv","findColumnsFromHeader":true}'
    )
  ) EXTEND ("date" VARCHAR, "分組" VARCHAR, "對話次數" BIGINT, "參與人數" BIGINT, "文件詞組" BIGINT, "部門" VARCHAR)
)
SELECT
  TIME_PARSE(TRIM("date")) AS "__time",
  "分組",
  "對話次數",
  "參與人數",
  "文件詞組",
  "部門"
FROM "ext"
WHERE 部門 != '研發及資訊部'
PARTITIONED BY DAY
