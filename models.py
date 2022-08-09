from flask_sqlalchemy import SQLAlchemy
#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#


db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String)
    genres = db.Column(db.ARRAY(db.String()))
    shows = db.relationship('Show', backref='venue', lazy='joined', cascade='delete, all')

    def __repr__(self):
        return f'<Venue id: {self.id}, name: {self.name}>'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String)
    genres = db.Column(db.ARRAY(db.String()))
    shows = db.relationship('Show', backref='artist', lazy='joined', cascade='delete, all')
    availabilities = db.relationship('Availability', backref='artist', lazy=True, cascade='delete, all')

    def __repr__(self):
        return f'<Artist id: {self.id}, name: {self.name}>'

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.String, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'))

    def __repr__(self):
        return f'<Show id: {self.id}, time: {self.start_time}, artist_id: {self.artist_id}>'


class Availability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Time)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'))

    def __repr__(self):
        return f'<Availability id: {self.id} time: {self.time} artist: {self.artist.name}>'