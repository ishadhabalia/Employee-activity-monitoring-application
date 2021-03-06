from django.db.models import (
    CharField,
    ForeignKey,
    PositiveIntegerField,
    DateTimeField,
    BooleanField,
    CASCADE,
    TextField,
    Model,
)
from django.utils.timezone import now


class UserBuffer(Model):
    user_id = PositiveIntegerField(blank=False, null=False)
    created_on = now()
    updated_on = now()
    name = CharField(max_length=255, blank=False, null=False)
    role = CharField(max_length=255, blank=False, null=False)
    team = CharField(max_length=255, blank=False, null=False)
    department = CharField(max_length=255, blank=False, null=False)
    joined_on = now()
    break_status = BooleanField(default=0)
    account_status = BooleanField(default=1)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

    def clean(self):
        """
        find and clean existing entries for user
        """

    def save(self, *args, **kwargs):
        self.clean()
        super(UserBuffer, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "User Buffer"
        verbose_name = "User Buffer"


class UserBufferLocation(Model):
    user_id = ForeignKey(UserBuffer, on_delete=CASCADE, related_name="user_id_loc")
    created_on = now()
    updated_on = now()
    ip = CharField(max_length=15, blank=False, null=False)
    city = CharField(max_length=255, blank=False, null=False)
    latitude = CharField(max_length=20, blank=False, null=False)
    longitude = CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return "{}".format(self.user_id)

    def clean(self):
        """
        find and clean existing entries for user
        """

    def save(self, *args, **kwargs):
        self.clean()
        super(UserBufferLocation, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "User Buffer Location"
        verbose_name = "User Buffer Location"


class UserBufferData(Model):
    user_id = ForeignKey(UserBuffer, on_delete=CASCADE, related_name="user_id_data")
    created_on = now()
    updated_on = now()
    productive = PositiveIntegerField()  # productive =1  | non prod = 0  | others = 2
    date = DateTimeField(blank=False, null=False)
    process_name = TextField(blank=False, null=False)

    def __str__(self):
        return "{}".format(self.user_id)

    def clean(self):
        """
        find and clean existing entries for user
        """

    def save(self, *args, **kwargs):
        self.clean()
        super(UserBufferData, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "User Buffer Data"
        verbose_name = "User Buffer Data"
