import re
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField, TimeField
from wtforms.validators import DataRequired, AnyOf, URL, ValidationError
from enums import State, Genre


class ShowForm(FlaskForm):
    artist_id = StringField(
        'artist_id'
    )
    venue_id = StringField(
        'venue_id'
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired()],
        default= datetime.today()
    )

class VenueForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=State.choices()
    )
    address = StringField(
        'address', validators=[DataRequired()]
    )
    phone = StringField(
        'phone'
    )
    image_link = StringField(
        'image_link', validators=[URL()]
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL()]
    )
    website_link = StringField(
        'website_link', validators=[URL()]
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description'
    )

    def validate_phone(self, phone):
        """
        Validate phone numbers like:
        1234567890 - no space
        123.456.7890 - dot separator
        123-456-7890 - dash separator
        123 456 7890 - space separator

        Patterns:
        000 = [0-9]{3}
        0000 = [0-9]{4}
        -.  = ?[-. ]

        Note: (? = optional) - Learn more: https://regex101.com/
        """
        regex = re.compile('^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$')
        if regex.match(phone.data):
            return True

        raise ValidationError('Invalid Phone.')

    def validate_state(self, state):
        if state.data in dict(Genre.choices()).keys():
            return True

        raise ValidationError('Invalid state.')

    def validate_genre(self, genre):
        if set(genre.data).issubset(dict(Genre.choices()).keys()):
            return True

        raise ValidationError('Invalid genre')
    

class ArtistForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    city = StringField(
        'city', validators=[DataRequired()]
    )
    state = SelectField(
        'state', validators=[DataRequired()],
        choices=State.choices()
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone'
    )
    image_link = StringField(
        'image_link', validators=[DataRequired(), URL()]
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired()],
        choices=Genre.choices()
     )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[URL()]
     )

    website_link = StringField(
        'website_link', validators=[URL()]
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )

    def validate_phone(self, phone):
        """
        Validate phone numbers like:
        1234567890 - no space
        123.456.7890 - dot separator
        123-456-7890 - dash separator
        123 456 7890 - space separator

        Patterns:
        000 = [0-9]{3}
        0000 = [0-9]{4}
        -.  = ?[-. ]

        Note: (? = optional) - Learn more: https://regex101.com/
        """
        regex = re.compile('^\(?([0-9]{3})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$')
        if regex.match(phone.data):
            return True

        raise ValidationError('Invalid Phone.')

    def validate_state(self, state):
        if state.data in dict(Genre.choices()).keys():
            return True

        raise ValidationError('Invalid state.')

    def validate_genre(self, genre):
        if set(genre.data).issubset(dict(Genre.choices()).keys()):
            return True

        raise ValidationError('Invalid genre')     

class AvailabilityForm(FlaskForm):
    artist_id = StringField('artist_id', validators=[DataRequired()])
    time = TimeField('time', validators=[DataRequired()])