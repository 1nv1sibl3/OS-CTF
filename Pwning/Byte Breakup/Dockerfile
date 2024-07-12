FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && \
    apt-get install -y libc6 file libc-bin xinetd

# Set the working directory to /home
WORKDIR /home

# Copy the challenge binary, xinetd configuration, and flag file to the challenge directory
COPY vuln /home/vuln
COPY vuln.xinetd /vuln.xinetd
COPY flag.txt /home/flag.txt

# Copy xinetd binary from system path to challenge directory
RUN cp /usr/sbin/xinetd /xinetd

# Ensure the challenge binary and xinetd are executable
RUN chmod +x /home/vuln
RUN chmod +x /xinetd

# Add xinetd configuration
RUN cp /vuln.xinetd /etc/xinetd.d/vuln

# Add a banner fail message
RUN echo "Connection failed" > /etc/banner_fail.txt

# Expose the port the challenge will run on
EXPOSE 1008

# Create a script that allows 'cat' and '/home/challenge' commands
RUN echo '#!/bin/bash\nif [[ "$1" == "cat" || "$1" == "/home/vuln" ]]; then shift; exec "$0" "$@"; else echo "Command not allowed"; exit 1; fi' > /usr/local/bin/restricted_shell && \
    chmod +x /usr/local/bin/restricted_shell

# Create a sub-user who will use the restricted shell
RUN useradd -m -d /home/hecker -s /usr/local/bin/restricted_shell hecker

# Start xinetd to run the challenge service
CMD ["/xinetd", "-dontfork"]
