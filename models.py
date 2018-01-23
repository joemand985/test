"""Models."""


class Comment(object):
    """Comment model."""

    def __init__(self, text, date):
        """Constructor."""
        self.text = text
        self.date = date

    def __repr__(self):
    	return "comment: {}, date: {}".format(self.text, self.date)

COMMENTS = [
    Comment("hello", "2018-01-01"),
    Comment("world", "2018-01-02"),
    Comment("test", "2018-01-03"),
]










'''class Comment(object):
	def __init__(self, comment, date):
		text = self.comment
		date = self.date

COMMENTS = []'''

