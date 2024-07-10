FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && \
    apt-get install -y xinetd file libc-bin 

# Copy the challenge binary, xinetd configuration, flag file to the challenge directory
COPY server /server
COPY buffer_buffet.xinetd /buffer_buffet.xinetd
COPY flag.txt /flag.txt

# Copy xinetd binary from system path to challenge directory
RUN cp /usr/sbin/xinetd /xinetd

# Ensure the challenge binary and xinetd are executable
RUN chmod +x /server
RUN chmod +x /xinetd

# Add xinetd configuration
RUN cp /buffer_buffet.xinetd /etc/xinetd.d/buffer_buffet

# Add a banner fail message
RUN echo "Connection failed" > /etc/banner_fail.txt

# Expose the port the challenge will run on
EXPOSE 1337

# Start xinetd to run the challenge service
CMD ["/xinetd", "-dontfork"]
