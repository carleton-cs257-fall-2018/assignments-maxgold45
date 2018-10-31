upload:
	scp api.py goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp
	scp website.py goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp
	scp -r templates goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp
	scp -r static goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp
	scp Makefile goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp

download:
	scp goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp/api.py api.py
	scp goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp/website.py website.py 
	scp -r goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp/templates templates
	scp -r goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp/static static
	scp goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp/Makefile Makefile

login:
	ssh goldbergm@perlman.mathcs.carleton.edu;

api:
	python3 api.py perlman.mathcs.carleton.edu 5110;

website:
	python3 website.py perlman.mathcs.carleton.edu 5210 5110;







