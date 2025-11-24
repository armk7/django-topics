## What are migrations?
Django's way of safely introduce changes of database schema.

## Commands:
- migrate: applying and unapplying migrations
- makemigrations: creating new migrations based on changes made on models
- sqlmigrate: outputs the sql statements for a migration
- showmigrations: lists project's migrations and their status

Migrations live in migrations directory of each app.<br>
related setting: MIGRATION_MODULES


Everything is included in migrations. even changes that do not affect the database.

- PostgreSQL is the most capable of all databases in terms of schema alteration

- To make migrations (after making some changes to your models or adding new models):
```
> python manage.py makemigrations
```
A new migration file will be created in apps/migrations directory.<br>
(makemigrations command is not perfect, for complex models, you should review them)

- to apply migrations:
```
python manage.py migrate
```

It is recommended to makemigratiosn and apply them in a single version control commit.

- To apply a meaningful name to migration files use the name option:
```
> python manage.py makemigrations --name changed_my_model <appLabel>
```

## Transactions:
skipped temporarily

## Dependecies
In some projects, different apps may have models that connect to each other (relationships).<br>
For example a book model (books app) may have a relationship to author model (authors app).<br>
Django will attempt its best to maintain the correct order of creating these models.<br>
The table that a ForeignKey (as example) references, will have its migration run first, then the migration that makes the ForeignKey column will run.<br>
Otherwise the first table would have tried to reference a table that does not exist yet, resulting in error.

## Swappable dependencies
No idea what is the purpose of this, skipping for now...

## Migration files
Stored in migration files on disk.<br>
Subclasses of django.db.migrations.Migration.<br>
They have 4 attributes, 2 of them are used most of the time.<br>
- dependencies, a list of migrations this one depends on.
- operations, a list of Operation classes that define what this migration does.
Operations are a set of declarative instructions which tell django what schema changes need to be made.<br>

## Custom fields
skipped

## Model managers
Managers can optionally be serialized into migrations and be available in RunPython operations.<br>
To do so, add 'use_in_migrations' to manager class.

## Initial migrations
The first migrations that create the app's first tables are called initial migrations.<br>
Usually only one. They are marked with initial = True.<br>

## History consistency
skipped

## Adding migrations to apps
New apps are preconfigured to accept migrations.<br>
To add new migrations:
```
> python manage.py makemigrations <app_label>
```

