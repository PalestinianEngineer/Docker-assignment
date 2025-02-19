# Docker-assignment
To build the images:

In the sender directory, run:
sudo docker build -t sender ./sender

In the receiver directory, run:
sudo docker build -t receiver ./receiver

In the root directory (docker-assignment), run:
sudo docker-compose up --build


(for some wierd reason, I can't run the commands unless I include sudo before them)