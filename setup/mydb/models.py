from django.db import models
from setup.constants import *

# Create your models here.

class CharacterDetails(models.Model):
    internal_id = models.PositiveIntegerField(db_column=TABLE_COLUMN_ID, verbose_name=VERBOSE_NAME_ID, default=0)
    voice = models.CharField(db_column=TABLE_COLUMN_VOICE, verbose_name=VERBOSE_NAME_VOICE, default="", max_length=MAX_DEFAULT_LENGTH)
    author = models.CharField(db_column=TABLE_COLUMN_AUTHOR, verbose_name=VERBOSE_NAME_AUTHOR, default="", max_length=MAX_DEFAULT_LENGTH)
    character_id = models.PositiveIntegerField(db_column=TABLE_COLUMN_CHARACTER_ID, verbose_name=VERBOSE_NAME_CHARACTER_ID, default=0)
    name = models.CharField(db_column=TABLE_COLUMN_NAME, verbose_name=VERBOSE_NAME_NAME, default="", max_length=MAX_DEFAULT_LENGTH)
    title = models.CharField(db_column=TABLE_COLUMN_TITLE, verbose_name=VERBOSE_NAME_TITLE, default="", max_length=MAX_TITLE_LENGTH)
    year = models.CharField(db_column=TABLE_COLUMN_YEAR, verbose_name=VERBOSE_NAME_YEAR, default="", max_length=MAX_DEFAULT_LENGTH)
    violence = models.CharField(db_column=TABLE_COLUMN_VIOLENCE, verbose_name=VERBOSE_NAME_VIOLENCE, default="", max_length=MAX_DEFAULT_LENGTH)
    race = models.CharField(db_column=TABLE_COLUMN_RACE, verbose_name=VERBOSE_NAME_RACE, default="", max_length=MAX_DEFAULT_LENGTH)
    gender = models.CharField(db_column=TABLE_COLUMN_GENDER, verbose_name=VERBOSE_NAME_GENDER, default="", max_length=MAX_DEFAULT_LENGTH)
    urban = models.CharField(db_column=TABLE_COLUMN_URBAN, verbose_name=VERBOSE_NAME_URBAN, default="", max_length=MAX_DEFAULT_LENGTH)
    sthreat = models.CharField(db_column=TABLE_COLUMN_STHREAT, verbose_name=VERBOSE_NAME_STHREAT, default="", max_length=MAX_DEFAULT_LENGTH)
    sdesire = models.CharField(db_column=TABLE_COLUMN_SDESIRE, verbose_name=VERBOSE_NAME_SDESIRE, default="", max_length=MAX_DEFAULT_LENGTH)
    death = models.CharField(db_column=TABLE_COLUMN_DEATH, verbose_name=VERBOSE_NAME_DEATH, default="", max_length=MAX_DEFAULT_LENGTH)
    suicide = models.CharField(db_column=TABLE_COLUMN_SUICIDE, verbose_name=VERBOSE_NAME_SUICIDE, default="", max_length=MAX_DEFAULT_LENGTH)
    migration = models.CharField(db_column=TABLE_COLUMN_MIGRATION, verbose_name=VERBOSE_NAME_MIGRATION, default="", max_length=MAX_DEFAULT_LENGTH)
    deterritorialization = models.CharField(db_column=TABLE_COLUMN_DETERRITORIALIZATION, verbose_name=VERBOSE_NAME_DETERRITORIALIZATION, default="", max_length=MAX_DEFAULT_LENGTH)
    oppression = models.CharField(db_column=TABLE_COLUMN_OPPRESSION, verbose_name=VERBOSE_NAME_OPPRESSION, default="", max_length=MAX_DEFAULT_LENGTH)
    revolt = models.CharField(db_column=TABLE_COLUMN_REVOLT, verbose_name=VERBOSE_NAME_REVOLT, default="", max_length=MAX_DEFAULT_LENGTH)
    assimilation = models.CharField(db_column=TABLE_COLUMN_ASSIMILATION, verbose_name=VERBOSE_NAME_ASSIMILATION, default="", max_length=MAX_DEFAULT_LENGTH)
    guide = models.CharField(db_column=TABLE_COLUMN_GUIDE, verbose_name=VERBOSE_NAME_GUIDE, default="", max_length=MAX_DEFAULT_LENGTH)
    craziness = models.CharField(db_column=TABLE_COLUMN_CRAZINESS, verbose_name=VERBOSE_NAME_CRAZINESS, default="", max_length=MAX_DEFAULT_LENGTH)
    children_metis = models.CharField(db_column=TABLE_COLUMN_CHILDREN_METIS, verbose_name=VERBOSE_NAME_CHILDREN_METIS, default="", max_length=MAX_DEFAULT_LENGTH)
    children_native = models.CharField(db_column=TABLE_COLUMN_CHILDREN_NATIVE, verbose_name=VERBOSE_NAME_CHILDREN_NATIVE, default="", max_length=MAX_DEFAULT_LENGTH)
    sprituality = models.CharField(db_column=TABLE_COLUMN_SPIRITUALITY, verbose_name=VERBOSE_NAME_SPIRITUALITY, default="", max_length=MAX_DEFAULT_LENGTH)
    allegory = models.CharField(db_column=TABLE_COLUMN_ALLEGORY, verbose_name=VERBOSE_NAME_ALLEGORY, default="", max_length=MAX_DEFAULT_LENGTH)
    age_old = models.CharField(db_column=TABLE_COLUMN_AGE_OLD, verbose_name=VERBOSE_NAME_AGE_OLD, default="", max_length=MAX_DEFAULT_LENGTH)

    class Meta:
        db_table = TABLE_NAME_CHARACTER_DETAILS   
        verbose_name_plural = "characters"