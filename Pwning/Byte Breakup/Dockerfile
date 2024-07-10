FROM ubuntu:20.04

# Install necessary packages
RUN apt-get update && \
    apt-get install -y xinetd libc6 file libc-bin

# Create a new user 'ctfuser' with restricted permissions
RUN useradd -m -s /bin/rbash ctfuser

# Copy the challenge binary, xinetd configuration, and flag file to the challenge directory
COPY vuln /vuln
COPY byte_breakup.xinetd /byte_breakup.xinetd
COPY flag.txt /flag.txt

# Set permissions for flag.txt so only 'ctfuser' can read it
RUN chown ctfuser:ctfuser /flag.txt
RUN chmod 400 /flag.txt

# Copy xinetd binary from system path to challenge directory
RUN cp /usr/sbin/xinetd /xinetd

# Ensure the challenge binary and xinetd are executable
RUN chmod +x /vuln
RUN chmod +x /xinetd

# Add xinetd configuration
RUN cp /byte_breakup.xinetd /etc/xinetd.d/byte_breakup

# Add a banner fail message
RUN echo "Connection failed" > /etc/banner_fail.txt

# Expose the port the challenge will run on
EXPOSE 1337

# Start xinetd to run the challenge service
CMD ["/usr/sbin/xinetd", "-dontfork"]
