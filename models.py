from django.db import models

# Create your models here.
class ckdModel(models.Model):

    Customer_Age=models.FloatField()
    Gender=models.FloatField()
    Education_Level=models.FloatField()
    Income_Category=models.FloatField()
    Card_Category=models.FloatField()
    Credit_Limit=models.FloatField()
    Total_Trans_Amt=models.FloatField()
