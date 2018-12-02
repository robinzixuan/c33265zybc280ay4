# from LoginDemoApp.database_tables import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, InputRequired
from LoginDemoApp import db
# import datetime

from LoginDemoApp.database_tables import load_user

exhibit_choices = [('Pacific', 'Pacific'), ('Jungle', 'Jungle'), ('Sahara', 'Sahara'), ('Mountainous', 'Mountanious')]
type_choices = [('Mammal', 'Mammal'), ('Fish', 'Fish'), ('Amphibian', 'Amphibian'), ('Bird', 'Bird')]
#
# class StaffChoices:
#     staff_choices = []
#
#     @staticmethod
#     def setter(staffs):
#         cls.staff_choices = staffs

# Classes for wt-forms

class VisitorRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit1 = SubmitField('Sign Up Visitor')
    submit2 = SubmitField('Sign Up Staff')


class StaffRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit2 = SubmitField('Sign Up Staff')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class SearchExhibitsForm(FlaskForm):
    name = StringField('Name')
    search = SubmitField('Search')
    animal_min = StringField('Min')
    animal_max = StringField('Max')
    water_feature = SelectField('Water Feature', choices=[('Yes', 'Yes'), ('No', 'No')])
    size_min = StringField('Min')
    size_max = StringField('Max')
    sort = SubmitField('OrderBy')
    by = SelectField('By', choices=[("Name", "Name"),("Size", "Size"),("NumAnimals", "NumAnimals"),("is_water", "is_water")])


class SearchShowHistoryForm(FlaskForm):
    name = StringField('Name')
    exhibit = SelectField('Exhibit', choices=exhibit_choices)
    date = DateTimeField('Datetime', format='%Y-%m-%d %H:%M:%S')
    search = SubmitField('Search Show')



class SearchExhibitsHistoryForm(FlaskForm):
    name = StringField('Name')
    visit_num_min = StringField('Min')
    visit_num_max = StringField('Max')
    date = DateField('Time', format ='%m/%d/%Y')
    search = SubmitField('Search')


class SearchAnimalForm(FlaskForm):
    name = StringField('Name')
    species = StringField('Species')
    age_min = StringField('Min')
    age_max = StringField('Max')
    exhibit = SelectField('Exhibit', choices=exhibit_choices)
    type = SelectField('Type', choices=type_choices)
    search = SubmitField('Search')
    sort = SubmitField('OrderBy')
    by = SelectField('By', choices=[("Name", "Name"), ("Species", "Species"), ("Age", "Age"),
                                    ("Exhibit", "Exhibit"),("Type", "Type")])


class AdminSearchAnimalForm(FlaskForm):
    name = StringField('Name')
    species = StringField('Species')
    age_min = StringField('Min')
    age_max = StringField('Max')
    exhibit = SelectField('Exhibit', choices=exhibit_choices)
    type = SelectField('Type', choices=type_choices)
    search = SubmitField('Search')
    remove = SubmitField('Remove')


class AddAnimalForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    species = StringField('Species', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    exhibit = SelectField('Exhibit', choices=exhibit_choices)
    type = SelectField('Type', choices=type_choices)
    submit = SubmitField('Add animal')


class RemoveForm(FlaskForm):
    remove = SubmitField('Remove')




class AddShowForm(FlaskForm):
    name = StringField('Name')
    exhibit = SelectField('Exhibit', choices=exhibit_choices)
    time = StringField('Time')
    date = DateTimeField('Datetime', format='%Y-%m-%d %H:%M:%S')
    submit = SubmitField('Add Show')
    staff = SelectField('Staff', choices = [])
    # def __init__(self, staff):
    #     pass


class SearchShowsForm(FlaskForm):
    name = StringField('Name')
    exhibit = SelectField('Exhibit', choices=exhibit_choices)
    date = DateTimeField('Date', format='%Y-%m-%d %H:%M:%S')
    search = SubmitField('Search')
    log_visit = SubmitField('Log Visit')


class AdminRemoveShowsForm(FlaskForm):
    name = StringField('Name')
    exhibit = SelectField('Exhibit', choices=exhibit_choices)
    date = DateField('Date', format='%m/%d/%Y')
    remove = SubmitField('Remove Show')
    search = SubmitField('Search Show')


class ExhibitDetail(FlaskForm):
    name = StringField('Name')
    size = StringField('Size')
    num_animals = StringField('Num Animals')
    water_feature = StringField('Water Feature')


class AnimalDetail(FlaskForm):
    name = StringField('Name')
    species = StringField('Species')
    age = StringField('Age')
    exhibit = StringField('Exhibit')
    type = StringField('Type')


class AnimalCareForm(FlaskForm):
    name = StringField('Name')
    species = StringField('Species')
    age = StringField('Age')
    exhibit = StringField('Exhibit')
    type = StringField('Type')
    notes = StringField('Notes')
    log_notes = SubmitField('Log Notes')

