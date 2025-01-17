Objective:
To create a simple Docker image using a Dockerfile. To understand how a volume works.

Instructions:
cd exo4 - Create a Dockerfile: 
Start with an instruction using the alpine:latest image.
Create a directory /data using an instruction
Set the entry point so that you can easily interact with the container.

Build the Docker Image and tag the image as my-volume-app.
Create a named volume myvol.
Run the Docker Container using the my-volume-app image, mounting the myvol volume to /data. Use the --rm flag to clean up the container after it stops.
Verify and list all Docker volumes and note the presence of the named volume.
Interact with the container: Create a file in the /data folder. 
Stop the container, and then start a new container using the same image, mounting the same volume myvol. Verify that the content of the /data folder persists.
