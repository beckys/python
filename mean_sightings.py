
import matplotlib.mlab as ml
import numpy as np

def get_mean_sightings(filename,animals):
    # loading table
    tab=ml.csv2rec(filename)
    animals=animals.capitalize()
#	print tab['animal']
    
    #find total number of records for animal and calculate mean
    isfocus=(tab['animal']== animals)
    total_rec=np.sum(isfocus)
    meancount=np.mean(tab['count'][isfocus])
    print tab['animal']
 #   if total_rec == 0:
#	   meancount=0
#   	else:
#	   meancount=np.mean(tab['count'][isfocus])
    #return the values
    return total_rec,meancount
