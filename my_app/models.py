from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=50)
    max_employees = models.IntegerField()


    def __str__(self):
        return self.name

class Position(models.Model):
    position_name = models.CharField(max_length=50)
    salary = models.CharField(max_length=6)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.position_name


class Employee(models.Model):
    first_last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=20)
    birthdate = models.DateField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    STATUS_TYPE = (
        ('Working', 'Работает'), ('Fired','Уволен'),
        ('Maternity leave','Декретный отпуск')
        )
    status = models.CharField(max_length=50, default="Работает", choices=STATUS_TYPE)

    def __str__(self):
        return self.first_last_name

        