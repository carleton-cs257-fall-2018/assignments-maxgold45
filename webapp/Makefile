upload:
	scp api.py goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp
	scp website.py goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp
	scp -r templates goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp
	scp -r static goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp
	scp Makefile goldbergm@perlman.mathcs.carleton.edu:/var/www/html/cs257/goldbergm/webapp

login:
	ssh goldbergm@perlman.mathcs.carleton.edu;

runwebsite:
	python3 api.py perlman.mathcs.carleton.edu 5110;
	python3 website.py perlman.mathcs.carleton.edu 5210 5110;







