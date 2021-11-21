from our_site import db

class FlashCard(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	card_term = db.Column(db.String(64), index=True, unique=True)
	card_def = db.Column(db.String(128), index=True, unique=True)

	def __repr__(self):
		return f'Term: {self.card_term}, Definition: {self.card_def}'
