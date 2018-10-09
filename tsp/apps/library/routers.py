
class LibraryRouter(object):

    def db_for_write(self, model, **hints):
        return 'bkle'

    def db_for_read(self, model, **hints):
        return 'bkls'