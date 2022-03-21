all: build
build:
	zip -r app_build.zip *
	echo '#!/usr/bin/env python3' | cat - app_build.zip > pstat
	chmod +x pstat
install:
	sudo install ./pstat /usr/bin/
uninstall:
	sudo rm /usr/bin/pstat
clean:
	rm app_build.zip
	rm pstat
test:
	zip -r app_build.zip *
	echo '#!/usr/bin/env python3' | cat - app_build.zip > pstat
	chmod +x pstat
	./pstat -V 
	./pstat -i 
	./pstat -I 
	./pstat -f 
	./pstat -m 
	./pstat -M 
	./pstat -p 
	./pstat -u 
	./pstat -v 
	./pstat -lp
	./pstat -w 
	./pstat -mi
	./pstat -nd