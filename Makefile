
test: stop
	docker build -t regex_test .
	docker run -dit --name=regex_test_container regex_test /bin/bash

stop:
	docker ps -aq --filter name=regex_test_container | xargs docker stop; true

clean: stop
	docker rm regex_test_container; true
	docker image rm regex_test; true
