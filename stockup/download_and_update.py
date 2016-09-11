from build_models import build_models
from download_data import update_csv


if __name__=='__main__':
    print "Updating Data..."

    filename = './data/stock_data.csv'
    update_csv(filename)

    print 'Done...'
    print 'Building Models...'

    build_models(filename, 'models.pkl')

    print 'Done...'
