FROM ubuntu:20.04

# Install necessary packages
RUN dpkg --add-architecture i386 && \
    apt-get update && \
    apt-get install -y libc6:i386 file libc-bin xinetd

# Copy the challenge binary, xinetd configuration, and flag file to the challenge directory
COPY seed_spring /seed_spring
COPY seed_spring.xinetd /seed_spring.xinetd
COPY flag.txt /flag.txt

# Copy xinetd binary from system path to challenge directory
RUN cp /usr/sbin/xinetd /xinetd

# Ensure the challenge binary and xinetd are executable
RUN chmod +x /seed_spring
RUN chmod +x /xinetd

# Add xinetd configuration
RUN cp /seed_spring.xinetd /etc/xinetd.d/seed_spring

# Add a banner fail message
RUN echo "Connection failed" > /etc/banner_fail.txt

# Expose the port the challenge will run on
EXPOSE 1008

# Start xinetd to run the challenge service
CMD ["/xinetd", "-dontfork"]
