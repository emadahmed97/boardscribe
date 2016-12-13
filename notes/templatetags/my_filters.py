from django.template.defaultfilters import register
from django import template
from django.contrib.auth.models import Group
from notes.models import Classes,Notes

register = template.Library() 


@register.filter(name='lookup')
def lookup(dict, index):
	
	x = str(index).replace("-"," ")

	x = x.title()
	
	return x

@register.filter(name='has_group') 
def has_group(user, group_name):
	group_name = group_name.title()



	for item in user.groups.all():

		if group_name == str(item):

			return "successful"

	return "unsuccessful"

@register.filter(name='notedate')
def notedate(dict, index):
	try:
		print index.title()
		x = index.title().replace("-"," ")
		date = Notes.objects.get(title=x)
		return date.pub_date
		
	except:
		print "no note"
		return None


