from app import db

class Brand(db.Model):
    ''' This class defines the campaigns table '''

    __tablename__ = 'brands'

    # Define the columns of the campaigns table, starting with the primary key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=True)
    description = db.Column(db.Text, nullable=True)
    logo = db.Column(db.String(255), nullable=True)
    slug = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime(), nullable=True)
    updated_at = db.Column(db.DateTime(), nullable=True)
    deleted_at = db.Column(db.DateTime(), nullable=True)

    def save(self):
        '''
        Save a campaigns to the database.
        This includes creating a new campaigns and editing one.
        '''
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return db.session.query(Brand).filter(Brand.deleted_at == None)

    @staticmethod
    def first():
        return db.session.query(Brand).filter(Brand.deleted_at == None).first()

        
