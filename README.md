# Docker commands

- If the container is set to run from the terminal and mounting the current directory: `docker run --name=*name* -it -v .:/app/ *image_name*`
- This will allow:
  - Any changes in the IDE to be reflected in the container and viceversa
  - Any output files from the container's script to be accessible from the host
- In order to mounr the host current directory in PyCharm with Dockerf as the interpreter:
  - Setup docker interpreter from the image
  - Select `...`
  - Use the "Pat Mapping feature" to set the host and the container's directories
