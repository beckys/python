from mean_sightings import get_mean_sightings

filename = 'sightings_animal.csv'

def test_pig_is_correct():
    pigrec,pigmean = get_mean_sightings(filename,'Pig')
    assert pigrec == 1, 'Number of records for Pig is wrong'
	#assert pigmean == 30, 'Mean is wrong'

def test_cow_is_correct():
    cowrec,cowmean = get_mean_sightings(filename,'Cow')
    assert cowrec == 2, 'Number of records for Pig is wrong'
#	assert pigmean == 30, 'Mean is wrong'

def test_anonymous_is_correct():
    anirec, animen = get_mean_sightings(filename,'NotPresent')
    assert anirec == 0, 'Number of records for anonymous is wrong'
#	assert pigmean == 30, 'Mean is wrong'