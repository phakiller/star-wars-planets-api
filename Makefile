build:
		docker build -t star-wars-planets .
run:
		docker-compose up --remove-orphans
go:
		make build && make run