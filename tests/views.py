from django.shortcuts import render
from tests.models import Person, Course
from django.views import generic
from django.db.models import (
    Q, 
    ExpressionWrapper, # operation with different types
    DateTimeField,
    F,
    When,
    Case,
    IntegerField,
    BooleanField
    
)
from django.db.models.functions import (
    Cast,
    ExtractYear,    
)
import calendar


class PersonView1(generic.ListView):
    models = Person
    def get_queryset(self):
        # value = params['value']

        user_filter = Q(
            Q(first_name__icontains=value)|
            Q(last_name__icontains=value)
        )

        return super().get_queryset().filter(user_filter)


class PersonView2(generic.ListView):
    models = Person
    def get_queryset(self):
        # value = self.page_kwarg['value']
        user_filter = Q(is_active=True)
        if 'name' in params:
            user_filter.add(
                Q(
                    Q(first_name__icontains=value)|
                    Q(last_name__icontains=value)
                ),
                Q.OR
            )
        
        if 'email' in params:
            user_filter.add(Q(email__icontains=value), Q.OR)

        return super().get_queryset().filter(user_filter)


class PersonView3(generic.ListView):
    models = Person
    def get_queryset(self):
        print(
            Person.objects.filter(
                Q(birthdate__year__range=(1960, 1980))
                |~Q(first_name__endswith='on')
            ).query
        )

        return super().get_queryset().filter(user_filter)


class CoursView(generic.ListView):
    models = Course
    def get_queryset(self):
        Course.objects.annotate(
            end_on=ExpressionWrapper(
                F('start_at') + F('duration'),
                output_field=DateTimeField()
            )
        )

        return super().get_queryset().filter(user_filter)

# BloodBank.objects. annotate (
#     existent_amount=Count ("bloodbag_set"),
#     remaining=F("goal ") - F("existent_amount"),
# ).values_list ("goal", "existent_amount", "remaining'")
# (1500, 1000, 508)        
        

years = (
    Person.objects.annotate(
        birth_year_int=Cast(
            ExtractYear("birthdate"),
            output_field=IntegerField(),
        ),
        birth_year_modulus_4=F("birth_year_int") % 4,
        birth_year_modulus_100=F("birth_year_int" ) % 100,
        birth_year_modulus_400=F("birth_year_int") % 400,
    ).annotate(
        born_in_leap_year=Case(
            When(
                Q(
                    Q( birth_year_modulus_4=0)
                    &Q(
                        ~Q(birth_year_modulus_100=0)
                        |Q(birth_year_modulus_400=0)
                    )
                ),
                then=True,
            ),
            default=False,
            output_field=BooleanField()
        )
    ).filter(born_in_leap_year=True).values_list("birthdate__year", flat=True)
)
for year in years:
    assert calendar.isleap(year), f"{year} ise't a leap year"