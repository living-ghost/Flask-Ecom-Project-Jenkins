Docker:
=
Steps to set up docker and build first image to run

step 1: download docker desktop
step 2: open powershel as administrator
step 3: run cmd wsl --install
step 4: run wsl --set-default-version 2
step 5: check docker version now : docker --version
step 6: docker run hello-world ( This command downloads a test image and runs it in a container. If successful, you should see         message indicating that Docker is working correctly.)
step 7: docker build -t flask-app .
step 8: docker run -d -p 80:80 flask-app