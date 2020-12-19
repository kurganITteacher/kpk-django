SELECT "mainapp_course"."id",
       "mainapp_course"."category_id",
       "mainapp_course"."name",
       "mainapp_course"."desc",
       "mainapp_course"."hours",
       "mainapp_course"."level",
       "mainapp_course"."is_active",
       "mainapp_course"."picture",
       "mainapp_subjectcategory"."id",
       "mainapp_subjectcategory"."name",
       "mainapp_subjectcategory"."desc"
FROM "mainapp_course"
         INNER JOIN "mainapp_subjectcategory"
                    ON ("mainapp_course"."category_id" = "mainapp_subjectcategory"."id")
WHERE "mainapp_course"."category_id" = 3
ORDER BY "mainapp_course"."is_active" DESC, "mainapp_course"."hours" DESC, "mainapp_course"."level" ASC;
