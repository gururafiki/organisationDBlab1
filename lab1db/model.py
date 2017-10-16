import json

class Agency(object):
	def __init__(self, agencyid, agencyname):
		self.agencyid = agencyid
		self.agencyname = agencyname
		
	def __str__(self):
		return "agencyid=%d, agencyname=%s" % (self.agencyid, self.agencyname)

	def toarray(self):
		return {'id': self.agencyid , 'name': self.agencyname }

	def add(self):
		agenciesfile = open("agencies.txt", mode='r')
		agenciesarr = []

		json_agencies = json.load(agenciesfile)
		agenciesfile.close()

		for agency in json_agencies:
			agenciesarr.append(agency)
		id=0
		for agency in agenciesarr:
			if(self.agencyname == agency['name']):
				return False
			id=agency['id']
		id+=1
		agenciesarr.append({'id': id , 'name': self.agencyname })

		agenciesfile = open("agencies.txt", mode='w')
		json.dump(agenciesarr, agenciesfile)
		agenciesfile.close()
		return True

	def delete(self):
		agenciesfile = open("agencies.txt", mode='r')
		agenciesarr = []

		json_agencies = json.load(agenciesfile)
		agenciesfile.close()

		for agency in json_agencies:
			agenciesarr.append(agency)
		id=0
		saved = []
		for agency in agenciesarr:
			if(self.agencyname == agency['name']):
				id=agency['id']
			else:
				saved.append(agency)
		if id!=0:
			agenciesfile = open("agencies.txt", mode='w')
			json.dump(saved, agenciesfile)
			agenciesfile.close()
			return True
		else:
			return False


	def check(self):
		agenciesfile = open("agencies.txt", mode='r')
		agenciesarr = []
		json_agencies = json.load(agenciesfile)
		agenciesfile.close()

		for agency in json_agencies:
			agenciesarr.append(agency)

		for agency in agenciesarr:
			if(self.agencyname == agency['name']):
				return agency['id']
		return 0


class Tours(object):
	def __init__(self):
		self.tours = []

	def show(self):
		toursfile = open("tours.txt", mode='r')
		json_tours = json.load(toursfile)
		toursfile.close()

		for tour in json_tours:
			self.tours.append(tour)

		return self.tours


class Dependencies(object):
	def __init__(self):
		self.dependencies = []

	def show(self):
		dependenciesfile = open("dependencies.txt", mode='r')
		json_dependencies = json.load(dependenciesfile)
		dependenciesfile.close()

		for dependency in json_dependencies:
			self.dependencies.append(dependency)

		return self.dependencies



class Agencies(object):
	def __init__(self):
		self.agencies = []

	def show(self):
		agenciesfile = open("agencies.txt", mode='r')
		json_agencies = json.load(agenciesfile)
		agenciesfile.close()

		for agency in json_agencies:
			self.agencies.append(agency)

		return self.agencies

class Dependency(object):
	def __init__(self, agencyname, tourname):
		self.agencyname = agencyname
		self.tourname = tourname

	def __str__(self):
		return "agencyname=%d, tourname=%s" % (self.agencyname, self.tourname)

	def add(self):
		dependenciesfile = open("dependencies.txt", mode='r')
		dependenciesarr = []

		json_dependencies = json.load(dependenciesfile)
		dependenciesfile.close()

		for dependency in json_dependencies:
			dependenciesarr.append(dependency)

		id=0
		for dependency in dependenciesarr:
			if(self.tourname == dependency['tourname'] and self.agencyname == dependency['agencyname']):
				return False
			id=dependency['id']
		id+=1
		dependenciesarr.append({'id': id , 'tourname': self.tourname , 'agencyname': self.agencyname })

		dependenciesfile = open("dependencies.txt", mode='w')
		json.dump(dependenciesarr,dependenciesfile)
		dependenciesfile.close()
		return True


	def findagency(self):
		dependenciesfile = open("dependencies.txt", mode='r')
		dependenciesarr = []

		json_dependencies = json.load(dependenciesfile)
		dependenciesfile.close()

		for dependency in json_dependencies:
			dependenciesarr.append(dependency)
		output = []
		id=0
		for dependency in dependenciesarr:
			if(self.agencyname == dependency['agencyname']):
				output.append(dependency['tourname'])
				id=dependency['id']
		if id!=0:
			return output
		else:
			return False

	def findtour(self):
		dependenciesfile = open("dependencies.txt", mode='r')
		dependenciesarr = []

		json_dependencies = json.load(dependenciesfile)
		dependenciesfile.close()

		for dependency in json_dependencies:
			dependenciesarr.append(dependency)
		output = []
		id=0
		for dependency in dependenciesarr:
			if(self.tourname == dependency['tourname']):
				output.append(dependency['agencyname'])
				id=dependency['id']
		if id!=0:
			return output
		else:
			return False

	def delete(self):
		dependenciesfile = open("dependencies.txt", mode='r')
		dependenciesarr = []

		json_dependencies = json.load(dependenciesfile)
		dependenciesfile.close()

		for dependency in json_dependencies:
			dependenciesarr.append(dependency)

		id=0
		saved = []
		for dependency in dependenciesarr:
			if(self.tourname == dependency['tourname'] and self.agencyname == dependency['agencyname']):
				id=dependency['id']
			else:
				saved.append(dependency)
		if id!=0:
			dependenciesfile = open("dependencies.txt", mode='w')
			json.dump(saved,dependenciesfile)
			dependenciesfile.close()
			return True
		else:
			return False

	def deleteall(self):
		dependenciesfile = open("dependencies.txt", mode='r')
		dependenciesarr = []

		json_dependencies = json.load(dependenciesfile)
		dependenciesfile.close()

		for dependency in json_dependencies:
			dependenciesarr.append(dependency)

		id=0
		saved = []
		for dependency in dependenciesarr:
			if(self.tourname == dependency['tourname'] or self.agencyname == dependency['agencyname']):
				id=dependency['id']
			else:
				saved.append(dependency)
		if id!=0:
			dependenciesfile = open("dependencies.txt", mode='w')
			json.dump(saved,dependenciesfile)
			dependenciesfile.close()
			return True
		else:
			return False
class Tour(object):
	def __init__(self, tourid, tourname):
		self.tourid = tourid
		self.tourname = tourname

	def __str__(self):
		return "tourid=%d, tourname=%s" % (self.tourid, self.tourname)

	def add(self):
		toursfile = open("tours.txt", mode='r')
		toursarr = []

		json_tours = json.load(toursfile)
		toursfile.close()

		for tour in json_tours:
			toursarr.append(tour)
		id=0
		for tour in toursarr:
			if(self.tourname == tour['name']):
				return False
			id=tour['id']
		id+=1
		toursarr.append({'id': id , 'name': self.tourname })

		toursfile = open("tours.txt", mode='w')
		json.dump(toursarr, toursfile)
		toursfile.close()
		return True

	def delete(self):
		toursfile = open("tours.txt", mode='r')
		toursarr = []

		json_tours = json.load(toursfile)
		toursfile.close()

		for tour in json_tours:
			toursarr.append(tour)
		id = 0
		saved = []
		for tour in toursarr:
			if(self.tourname == tour['name']):
				id=tour['id']
			else:
				saved.append(tour)

		if(id!=0):
			toursfile = open("tours.txt", mode='w')
			json.dump(saved, toursfile)
			toursfile.close()
			return True
		else:
			return False

	def check(self):
		toursfile = open("tours.txt", mode='r')
		toursarr = []
		json_tours = json.load(toursfile)
		toursfile.close()

		for tour in json_tours:
			toursarr.append(tour)

		for tour in toursarr:
			if(self.tourname == tour['name']):
				return tour['id']
		return 0
