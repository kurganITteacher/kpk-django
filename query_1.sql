SELECT
    "mainapp_course"."id", "mainapp_course"."category_id", "mainapp_course"."name", "mainapp_course"."desc",
    "mainapp_course"."hours", "mainapp_course"."level", "mainapp_course"."is_active", "mainapp_course"."picture"
FROM "mainapp_course"
WHERE "mainapp_course"."category_id" = 1
ORDER BY "mainapp_course"."is_active" DESC, "mainapp_course"."hours" DESC, "mainapp_course"."level" ASC
